#!/usr/bin/env python3

"""
Example input:

7 7
1 0 2 0 1 0 2 
0 0 0 0 0 0 0 
0 0 5 0 0 0 4 
0 0 0 0 0 0 0 
0 0 0 2 0 0 4 
0 0 0 0 0 0 0 
3 0 5 0 0 0 1 
15
2 2 2 6
4 3 4 6
2 2 6 2
6 0 6 2
0 2 2 2
6 2 6 6
4 3 4 6
2 2 6 2
6 0 6 2
0 4 0 6
0 0 6 0
2 6 4 6
0 2 2 2
0 6 2 6
2 6 4 6

"""

import sys

from igraph import Graph


def add_bridge_h(r, c):
    if res[r][c] == '.':
        res[r][c] = '─'
    elif res[r][c] == '─':
        res[r][c] = '═'
    elif str(res[r][c]) in '═│║':
        res[r][c] = '*'
        errors.append(f'Too many bridges in {(r, c)}')
    else:
        errors.append(f'A bridge over island at {(r, c)}')


def add_bridge_v(r, c):
    if res[r][c] == '.':
        res[r][c] = '│'
    elif res[r][c] == '│':
        res[r][c] = '║'
    elif str(res[r][c]) in '║─═':
        res[r][c] = '*'
        errors.append(f'Too many bridges in {(r, c)}')
    else:
        errors.append(f'A bridge over island at {(r, c)}')


try:
    errors = []
    rows, cols = [int(x) for x in input().split()]

    grid = []
    for _ in range(rows):
        grid.append([int(x) for x in input().split()])

    res = []
    for r in range(2*rows-1):
        res.append(['.' for _ in range(2*cols-1)])
    island_graph = Graph()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                res[2*r][2*c] = 0
                island_graph.add_vertex(f"{(r, c)}")

    connections = int(input())
    for _ in range(connections):
        r, c, r_, c_ = [int(x) for x in input().split()]
        if not 0 <= r <= rows or not 0 <= c <= cols or not 0 <= r_ <= rows or not 0 <= c_ <= cols:
            sys.exit(f"Wrong bridge {(r, c, r_, c_)}")
        if grid[r][c] == 0:
            sys.exit(f"Bridge {(r, c, r_, c_)} doesn't start from an island")
        if grid[r_][c_] == 0:
            sys.exit(f"Bridge {(r, c, r_, c_)} doesn't terminate into an island")
        if r != r_ and c != c_:
            sys.exit(f"Bridge {(r, c, r_, c_)} is not straight")
        if r == r_ and c == c_:
            sys.exit(f"Bridge {(r, c, r_, c_)} doesn't connect two islands")
        
        island_graph.add_edge(f"{(r, c)}", f"{(r_, c_)}")
        res[2*r][2*c] += 1
        res[2*r_][2*c_] += 1
        if r == r_:
            for i in range(2*min(c, c_)+1, 2*max(c, c_)):
                add_bridge_h(2*r, i)
        else:
            assert c == c_
            for i in range(2*min(r, r_)+1, 2*max(r, r_)):
                add_bridge_v(i, 2*c)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0 and res[2*r][2*c] != grid[r][c]:
                errors.append(f'Wrong number of bridges in island {(r, c)}')
                res[2*r][2*c] = grid[r][c]

    if not island_graph.is_connected():
        errors.append(f"Islands are not connected")
        errors.append(str(island_graph.clusters()))

    for r in res:    
        print(''.join([str(x) for x in r]))

    if errors:
        print('\n'.join(errors))
        sys.exit('WRONG!')

    print("CORRECT!")

except Exception as e:
    sys.exit(e)
    