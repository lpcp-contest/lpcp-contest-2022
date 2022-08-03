#!/usr/bin/env python3

"""
Example input:

1 2 0 0 0 8 0 1
0 1
0 1
right jump beep right left left left nop .
.

"""

import fileinput
import re
from sympy import E
import sys


def pretty_print():
    for x in range(rows):
        l = []
        for y in range(cols):
            c = [' ', str(grid[x][y]) if grid[x][y] != -9 else ' ', ' ']
            if (rx, ry) == (x, y):
                if rd == UP:
                    c[0] = '^'
                elif rd == RIGHT:
                    c[0] = '>'
                elif rd == DOWN:
                    c[0] = 'v'
                else:
                    assert rd == LEFT
                    c[0] = '<'
            if target[x][y] == 1:
                c[2] = 'o'
            elif target[x][y] == -1:
                c[2] = '.'
            l.append(''.join(c))
        print(''.join(l))

    print()

    print("MAIN: ", end='')
    main_i = ip[1] if ip[0] == main else sip
    for i in range(len(main)):
        if i == main_i:
            print(f"[{main[i]}]", end=' ')
        else:
            print(f" {main[i]} ", end=' ')
    print()

    print(" SUB: ", end='')
    sub_i = ip[1] if ip[0] == subroutine else -1
    for i in range(len(subroutine)):
        if i == sub_i:
            print(f"[{subroutine[i]}]", end=' ')
        else:
            print(f" {subroutine[i]} ", end=' ')
    print()

    print()


try:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


    def forward():
        global rx, ry
        if rd == UP:
            if rx > 0 and grid[rx][ry] == grid[rx-1][ry]:
                rx -= 1
        elif rd == RIGHT:
            if ry < cols-1 and grid[rx][ry] == grid[rx][ry+1]:
                ry += 1
        elif rd == DOWN:
            if rx < rows-1 and grid[rx][ry] == grid[rx+1][ry]:
                rx += 1
        else:
            assert rd == LEFT
            if ry > 0 and grid[rx][ry] == grid[rx][ry-1]:
                ry -= 1


    def jump():
        global rx, ry
        if rd == UP:
            if rx > 0 and abs(grid[rx][ry] - grid[rx-1][ry]) == 1:
                rx -= 1
        elif rd == RIGHT:
            if ry < cols-1 and abs(grid[rx][ry] - grid[rx][ry+1]) == 1:
                ry += 1
        elif rd == DOWN:
            if rx < rows-1 and abs(grid[rx][ry] - grid[rx+1][ry]) == 1:
                rx += 1
        else:
            assert rd == LEFT
            if ry > 0 and abs(grid[rx][ry] - grid[rx][ry-1]) == 1:
                ry -= 1


    rows, cols, rx, ry, rd, main_size, subroutine_size, n_targets = [int(x) for x in input().split()]

    grid = []
    for _ in range(rows):
        grid.append([int(x) if int(x) >= 0 else -9 for x in input().split()])
        assert len(grid[-1]) == cols

    target = []
    for _ in range(rows):
        target.append([0 for _ in range(cols)])
    for _ in range(n_targets):
        r, c = [int(x) for x in input().split()]
        target[r][c] = -1

    main = [x.strip() for x in input().split()]
    subroutine = [x.strip() for x in input().split()]
    if len(main) -1 != main_size:
        sys.exit("wrong length for main procedure")
    if len(subroutine) -1 != subroutine_size:
        sys.exit("wrong length for subroutine")
    if main[-1] != '.':
        sys.exit("main procedure must terminate with a full stop preceded by space, ie. ' .'")
    if subroutine[-1] != '.':
        sys.exit("subroutine must terminate with a full stop preceded by space, ie. ' .'")
    main = main[:-1]
    subroutine = subroutine[:-1]

    for x in main:
        if x not in ['nop', 'forward', 'left', 'right', 'jump', 'beep', 'subroutine']:
            sys.exit(f"Unknown action {x} in main")
    for x in subroutine:
        if x not in ['nop', 'forward', 'left', 'right', 'jump', 'beep']:
            sys.exit(f"Unknown or invalid action {x} in subroutine")

    ip = (main, 0)
    sip = None
    pretty_print()
    while ip != (main,len(main)):
        if ip == (subroutine, len(subroutine)):
            ip = (main, sip)
            sip = None
        else:
            a = ip[0][ip[1]]
            if a == 'subroutine':
                sip = ip[1]
                ip = (subroutine, -1)
            elif a == 'forward':
                forward()    
            elif a == 'left':
                rd = (rd - 1) % 4
            elif a == 'right':
                rd = (rd + 1) % 4
            elif a == 'jump':
                jump()
            elif a == 'beep':
                target[rx][ry] *= -1
            elif a == 'nop':
                pass
        ip = (ip[0], ip[1]+1)
        pretty_print()


    for x in range(rows):
        for y in range(cols):
            if target[x][y] == -1:
                sys.exit(f"Missed target at {(x, y)}")    

    print("CORRECT!")

except Exception as e:
    sys.exit(e)
    