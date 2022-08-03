#!/usr/bin/env python3

"""
Example input:

5
-1 0 2 1 -1 -1 
1 3 -1 -1 1 -1 
-1 2 1 -1 -1 -1 
-1 1 -1 2 -1 -1 
-1 2 -1 -1 3 0 
-1 -1 -1 2 -1 -1 
\/\\\
\\\\/
\\///
\////
\/\/\

"""

import sys

from igraph import Graph


def increase(r, c):
    if isinstance(res[2*r][2*c], int):
        res[2*r][2*c] += 1


try:
    errors = []
    size = int(input())

    grid = []
    for _ in range(size+1):
        grid.append([int(x) for x in input().split()])

    island_graph = Graph()
    for r in range(size+1):
        for c in range(size+1):
            island_graph.add_vertex(f"{(r, c)}")

    res = []
    for r in range(2*size+1):
        res.append([' ' for _ in range(2*size+1)])
    for r in range(size+1):
        for c in range(size+1):
            if grid[r][c] >= 0:
                res[2*r][2*c] = 0
            else:
                res[2*r][2*c] = 'o'

    for r in range(size):
        line = input()
        if len(line) != size:
            sys.exit(f"Wrong length: {line}")
        for c in range(size):
            if line[c] not in '\\/':
                sys.exit(f"Unknown char in {line}")
            res[2*r+1][2*c+1] = line[c]
            if line[c] == '\\':
                increase(r, c)
                increase(r+1, c+1)
                island_graph.add_edge(f"{(r, c)}", f"{(r+1, c+1)}")
            else:
                increase(r, c+1)
                increase(r+1, c)
                island_graph.add_edge(f"{(r, c+1)}", f"{(r+1, c)}")


    for r in range(size+1):
        for c in range(size+1):
            if grid[r][c] > 0 and res[2*r][2*c] != grid[r][c]:
                errors.append(f'Wrong number of connections in {(r, c)}')
                res[2*r][2*c] = grid[r][c]

    cycle = island_graph.girth(return_shortest_circle=True)
    if cycle:
        cycle = ' '.join([island_graph.vs.find(x)["name"] for x in cycle])
        errors.append(f"Oops! I found a cycle: {cycle}")

    for r in res:    
        print(''.join([str(x) for x in r]))


    if errors:
        print('\n'.join(errors))
        sys.exit('WRONG!')

    print("CORRECT!")

except Exception as e:
    sys.exit(e)
    