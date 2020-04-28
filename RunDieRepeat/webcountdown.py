#!/usr/bin/env python3
# USAGE: ./webcountdown.py $min
import sys
from datetime import datetime, timedelta
DECALAGE_HORAIRE = 2
min = int(sys.argv[1])
c = int((datetime.now() + timedelta(minutes=min, hours=DECALAGE_HORAIRE)).timestamp())
print(f'https://www.webcountdown.net/?c={c}')
