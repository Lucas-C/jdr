#!/usr/bin/python3

from collections import defaultdict

CELL_WIDTH = 17
CELL_FORMAT = '{:^' + str(CELL_WIDTH) + '}'

def generate_stats(dices, success_thresholds, fumble_threshold, ruleset_compute):
    stats = defaultdict(dict)
    for success_threshold in success_thresholds:
        for dice in dices:
            dice_value = int(dice[1:])
            stats[dice][success_threshold] = ruleset_compute(success_threshold, dice_value, fumble_threshold)
        stats['safest'][success_threshold] = find_positive_maxs(dices, key=lambda dice: stats[dice][success_threshold]['success'])
        stats['best4fumble'][success_threshold] = find_positive_maxs(dices, key=lambda dice: stats[dice][success_threshold]['fumble'])
    return stats

def print_stats(stats, dices, success_thresholds):
    ordered_columns = [''] + dices + ['safest', 'best4fumble']
    print('|'.join(CELL_FORMAT.format(col) for col in ordered_columns))
    for success_threshold in success_thresholds:
        print('-' * (len(ordered_columns) * (CELL_WIDTH + 1) - 1))
        first_row = [str(success_threshold)]
        first_row += ['success: {:.1f}%'.format(100 * stats[col][success_threshold]['success']) for col in dices]
        first_row += [','.join(stats[col][success_threshold]) for col in ['safest', 'best4fumble']]
        print('|'.join(CELL_FORMAT.format(col) for col in first_row))
        second_row = ['']
        second_row += ['fumble: {:.1f}%'.format(100 * stats[col][success_threshold]['fumble']) for col in dices]
        safest_dices = stats['safest'][success_threshold]
        second_row += ['{:.1f}%'.format(100 * stats[safest_dices[0]][success_threshold]['success'])] if safest_dices else ['']
        best4fumble_dices = stats['best4fumble'][success_threshold]
        second_row += ['{:.1f}%'.format(100 * stats[best4fumble_dices[0]][success_threshold]['fumble'])] if best4fumble_dices else ['']
        print('|'.join(CELL_FORMAT.format(col) for col in second_row))

def find_positive_maxs(seq, key):
    max_val = key(max(seq, key=key))
    if max_val > 0:
        return [e for e in seq if key(e) == max_val]
    return []

def compute_stats_for_rollbelow_rule(skill_level, dice_value, fumble_threshold):
    success = min(skill_level, dice_value) / dice_value
    if fumble_threshold(skill_level) > min(skill_level, dice_value):
        fumble = 0
    else:
        fumble = (min(skill_level, dice_value) - fumble_threshold(skill_level) + 1) / dice_value
    return {'success': success, 'fumble': fumble}

def compute_stats_for_rollabove_rule(difficulty, dice_value, fumble_threshold):
    if difficulty > dice_value:
        success = 0
    else:
        success = (dice_value - difficulty + 1) / dice_value
    if fumble_threshold == 'EQUAL_DIFFICULTY':
        fumble = 0 if not success else 1 / dice_value
    elif fumble_threshold(difficulty) > dice_value:
        fumble = 0
    else:
        fumble = (dice_value - fumble_threshold(difficulty) + 1) / dice_value
    return {'success': success, 'fumble': fumble}

skill_levels = [7, 8, 9, 10, 11, 12]
dices = ['d6', 'd8', 'd10', 'd12']
fumble_threshold = lambda _: 6
ruleset_compute = compute_stats_for_rollbelow_rule
print('\nROLL BELOW - Fumble: 6+')
print_stats(generate_stats(dices, skill_levels, fumble_threshold, ruleset_compute), dices, skill_levels)

skill_levels = [5, 6, 7, 8]
dices = ['d4', 'd6', 'd8']
fumble_threshold = lambda _: 4
ruleset_compute = compute_stats_for_rollbelow_rule
print('\nROLL BELOW - Fumble: 4+')
print_stats(generate_stats(dices, skill_levels, fumble_threshold, ruleset_compute), dices, skill_levels)

skill_levels = [3, 4, 5, 6, 7, 8, 9, 10, 11]
dices = ['d4', 'd6', 'd8', 'd10', 'd12']
fumble_threshold = lambda skill_level: skill_level - 1
ruleset_compute = compute_stats_for_rollbelow_rule
print('\nROLL BELOW - Fumble: (skill_level - 1)+')
print_stats(generate_stats(dices, skill_levels, fumble_threshold, ruleset_compute), dices, skill_levels)

skill_levels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dices = ['d4', 'd6', 'd8', 'd10', 'd12']
fumble_threshold = lambda skill_level: skill_level
ruleset_compute = compute_stats_for_rollbelow_rule
print('\nROLL BELOW - Fumble: skill_level+')
print_stats(generate_stats(dices, skill_levels, fumble_threshold, ruleset_compute), dices, skill_levels)

difficulties = [4, 6, 8, 10]
dices = ['d6', 'd8', 'd10', 'd12']
fumble_threshold = lambda difficulty: difficulty + 2
ruleset_compute = compute_stats_for_rollabove_rule
print('\nROLL ABOVE - Fumble: >difficulty+2')
print_stats(generate_stats(dices, difficulties, fumble_threshold, ruleset_compute), dices, difficulties)

difficulties = [4, 6, 8]
dices = ['d6', 'd8', 'd10', 'd12']
fumble_threshold = 'EQUAL_DIFFICULTY'
ruleset_compute = compute_stats_for_rollabove_rule
print('\nROLL ABOVE - Fumble: roll == difficulty')
print_stats(generate_stats(dices, difficulties, fumble_threshold, ruleset_compute), dices, difficulties)

