#!/usr/bin/env python3

"""
Example input:

23 23
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 3 0 2 0 3 0 3 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 0 0 0 2 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 6 0 0 0 0 3 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 0 0 0 0 2 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 3 0 0 0 0 1 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
34
6 15
16 7
7 10
7 16
12 3
17 8
11 4
10 5
13 4
11 16
8 17
10 17
13 16
15 13
18 9
15 16
6 13
16 15
7 12
14 5
12 17
17 10
8 7
14 17
9 6
7 11
15 6
9 18
16 14
15 12
6 9
16 11
7 8
7 14

"""

from multiprocessing.sharedctypes import Value
import sys


def enq(r, c):
    global attacks
    if r < 0 or c < 0:
        return
    if r >= rows or c >= cols:
        return
    if grid[r][c] not in [-1, -2]:
        if grid[r][c] > 0:
            errors.append(f'POI attacked in ({r+1}, {c+1})')
            return
        grid[r][c] = -2
        q.append((r,c))
        attacks += 1


try:
    rows, cols = [int(x) for x in input().split()]

    grid = []
    for _ in range(rows):
        grid.append([int(x) for x in input().split()])

    walls = int(input())
    for _ in range(walls):
        r, c = [int(x) for x in input().split()]
        if not 1 <= r <= rows or not 1 <= c <= cols:
            sys.exit(f"Wrong wall at {(r, c)}")
        if grid[r-1][c-1] != 0:
            sys.exit(f"Wrong wall at {(r, c)}")
        grid[r-1][c-1] = -1

    can_have_wall = []
    for _ in range(rows):
        can_have_wall.append([True for _ in range(cols)])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                for dr in range(-grid[r][c], grid[r][c] + 1):
                    for dc in range(-grid[r][c], grid[r][c] + 1):
                        if abs(dr) + abs(dc) < grid[r][c]:
                            can_have_wall[r+dr][c+dc] = False

    attacks = 0
    errors = []
    q = []
    for r in range(rows):
        enq(r, 0)
        enq(r, cols-1)
    for c in range(cols):
        enq(0, c)
        enq(rows-1, c)
    while q:
        r, c = q.pop()
        enq(r-1, c)
        enq(r+1, c)
        enq(r, c-1)
        enq(r, c+1)

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell > 0:
                print(cell, end='')
            elif cell == -1:
                if not can_have_wall[r][c]:
                    print('O', end='')
                    errors.append(f'Cannot have a wall in ({r+1}, {c+1})')
                else:
                    print('■', end='')
            elif cell == -2:
                print('⚔', end='')
            else:
                print('.', end='')
        print()

    print()
    print(f"walls: {walls}")
    print(f"cells inside: {rows * cols - walls - attacks}")
    print()

    if errors:
        print('\n'.join(errors))
        sys.exit('WRONG!')

    print("CORRECT!")

except Exception as e:
    sys.exit(e)