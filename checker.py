#!/usr/bin/env python3

import fileinput
import requests
import sys


CHECKER_SERVER = 'CHANGE_THIS'  # <<<


if len(sys.argv) != 3:
    sys.exit("ERROR: missing problem-ID and instance-ID in command parameters")

problem = int(sys.argv[1])
instance = int(sys.argv[2])

if problem < 1 or problem > 5:
    sys.exit("ERROR: invalid problem-ID")
if instance < 1 or instance > 10:
    sys.exit("ERROR: invalid instance-ID")

solution = ''.join(fileinput.input("-"))

url = f'{CHECKER_SERVER}/{problem}/{instance}/'

res = requests.post(url, data={"value": solution})
j = res.json()
if 'message' in j:
    print(j['message'])
else:
    print('WRONG RESPONSE RECEIVED!')
    print(res)
    print(j)
