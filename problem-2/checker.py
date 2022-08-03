#!/usr/bin/env python3

"""
Example input:

3 4
13
fill_a
a_to_b
fill_a
a_to_b
drop_b
a_to_b
fill_a
a_to_b
drop_b
a_to_b
fill_a
a_to_b
fill_a

"""

import sys


def pretty_print(step, action, ca, cb, a, b):
    print(f'STEP {step:2} - {action:8}', end='')

    print('[', end='')
    print('■' * a, end='')
    print(' ' * (ca - a), end='')
    print(']', end=' ')

    print('[', end='')
    print('■' * b, end='')
    print(' ' * (cb - b), end='')
    print(']')


try:
    max_length = 70

    ca, cb = [int(x) for x in input().split()]
    length = int(input())

    do = []
    for _ in range(length):
        do.append(input().strip())

    if length > max_length:
        sys.exit(f"Longer than acceptable!")


    a, b = 0, 0
    seen = set((a,b))
    pretty_print(0, 'start', ca, cb, a, b)
    for step in range(len(do)):
        action = do[step]
        if action == 'fill_a':
            a = ca
        elif action == 'fill_b':
            b = cb
        elif action == 'drop_a':
            a = 0
        elif action == 'drop_b':
            b = 0
        elif action == 'a_to_b':
            d = min(a, cb-b)
            a -= d
            b += d
        elif action == 'b_to_a':
            d = min(b, ca-a)
            a += d
            b -= d
        else:
            sys.exit(f"Unknown action: {action}")
        
        pretty_print(step+1, action, ca, cb, a, b)
        if (a,b) in seen:
            sys.exit(f"Repeated configutation!")
        seen.add((a,b))


    print("CORRECT!")

except Exception as e:
    sys.exit(e)
    