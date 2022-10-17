#!/usr/bin/python3

import sys
import glob
import os
import re
from pathlib import Path
from datetime import date, datetime

import json

HOME = Path.home()
CWD = os.getcwd()

PROJECT = CWD
SRC_PATH = f'{PROJECT}/src/entidades'
RUNNER = f'{PROJECT}/runner'
CRON = f'{RUNNER}/cron'

# ensure path
Path(CRON).mkdir(parents=True, exist_ok=True)

# locate files
files_to_process = glob.glob(f'{SRC_PATH}/*/*.json')
print(f'{files_to_process}')

day = []
month = []
quarter = []
year = []

d = {
        "diaria": day,
        "mensual": month,
        "trimestral": quarter,
        "anual": year
    }

# create cron jobs
for f in files_to_process:
    j = open(f)
    data = json.load(j)
    #print(data)
    path = os.path.dirname(f)
    line = f"{data['entidad'].lower()}:{data['nombre']}:{data['ipynb']}.ipynb"
    print(line)
    d[data['periodicidad']].append(line)
    j.close()

print('Parpairing cron files...')

# write all
all = []
for k in d.keys():
    file = f'{PROJECT}/runner/cron/{k}.txt'
    print(f'> {file}')
    open(file, 'w+').write('\n'.join(d[k]))
    for element in d[k]:
        all.append(element)

print('Writting all')
open(f'{PROJECT}/runner/cron/all.txt', 'w+').write('\n'.join(all))

print('Done')    