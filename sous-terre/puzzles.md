<!--
Ce fichier doit être exporté en PDf en 2x2 par A4

Idées en vrac:
- PJs découvrent 1 à 3 mots magiques (qu'ils inventent _in game_) qui chacun déclenche un effet différent
- portes activables à l'énonciation d'un mot magique
- basé sur contrôle du niveau d'eau
- se jeter dans le vide
- magie qui transforme la pierre en autre chose
- colosse à vaincre dans une salle
- énigme de réflection de la lumière
- pattern/format commun à plusieurs mécanismes : suite de 3 à 6 d6 (diégétique : indique placement de doigts de la main, 6 => paume)
- grille de sudoku sans lignes, avec des points représentant des d6
- pierre de rosette pour décrypter symbole chiffres <-> dés

Idées nécessitant un illustrateur / un peu de boulot de graphisme :
- palissade grillagée avec des trous correspondant à des faces de d6 (inspi The Witness)
- voute étoilées -> les étoiles indique des faces de d6

Tom Hermans advice:
  * A puzzle should be inviting and rewarding
  * Use the smallest amount of space and puzzle pieces for the puzzle will work
  * by teaching new things in every levels, puzzles become much more focused and elegant
  * Puzzles should be a little bit inaccessible if they want to evoke a feeling of mystery and sensation to drive the player
  * + continuity & foreshadowing

Mes contraintes créatives:
  * _environmental_ + se baser sur la faune / flore
  * la majorité des puzzles ne doit pas nécessiter d'item mais une simple connaissance des règles / de l'environnement / de mots magiques
  * faire découvrir aux joueurs des "raccourcis" pour des tâches laborieuses
  * certaines énigmes seront visuelles et incluses dans le jeu
-->

1|2|3|4|5|6
-|-|-|-|-|-
2|3|4|5|6|1
3|4|5|6|1|2
4|5|6|1|2|3
5|6|1|2|3|4
6|1|2|3|4|5

<script>
const SIZE = 6;
const DICE_SETUPS = {
    1: [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ],
    2: [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0],
    ],
    3: [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ],
    4: [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ],
    5: [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ],
    6: [
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
    ],
}
const tbody = document.getElementsByTagName('tbody')[0]
window.tbody = tbody
let k = 0
document.querySelectorAll('tr > *').forEach(cell => {
    let value = +cell.textContent
    if (k === 0) {
        console.log('Inserting');
        [...Array(3)].forEach(() => 
            tbody.appendChild(document.createElement('tr'))
        )
    }
    k = (k + 1) % SIZE
    DICE_SETUPS[value].forEach((row, i) => {
        row.forEach(isFill => {
            let td = document.createElement('td')
            if (isFill) td.classList.add('filled')
            tbody.children[tbody.children.length - 3 + i].appendChild(td)
        })
    })
    cell.parentNode.removeChild(cell)
});
</script>

<style>
table { border-spacing: .2rem; }
td { width: 1rem; height: 1rem; border-radius: 1rem; padding: 0; }
.filled { background-color: black; }
</style>
