#!/usr/bin/env python3
# USAGE: ./webcountdown.py $min
import sys
from datetime import datetime, timedelta
DECALAGE_HORAIRE = 1 # 1 à l'heure d'hiver / 2 à l'heure d'été
min = int(sys.argv[1])
c = int((datetime.now() + timedelta(minutes=min, hours=DECALAGE_HORAIRE)).timestamp())
print(f'https://www.webcountdown.net/?c={c}')
