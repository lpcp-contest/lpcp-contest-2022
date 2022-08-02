# Problem 1

Hello Great Builder!
Your mission is to build some walls to protect a few point-of-interests on a given map.
Each point-of-interest requires some area free-of-walls in order to be functional (for example, barraks requires more space than houses).
Building walls is expensive, so the amount of walls must be minimized.
Moreover, we don't really care about locations that are not point-of-interests, as they possibly host people who are not sympathetic to our cause...
at the end of the day, better if they are left to their fate out of our walls!

The map comprises RxC cells, some of them marked with a positive integer D to denote a point-of-interest that requires D free-of-walls cells around them;
more specifically, no path of length D (Manhattan distance) originating from the point-of-interest can include walls.
All point-of-interests must be inside the perimeter of the walls, the number of walls must be minimized, and as a second optimization criteria we prefer to minimize the amount of cells inside the perimeter of the walls.


## Special evaluation rules

You will get 0 points if your solution provides a wrong answer in any tested instance (as usual).
Otherwise, you will get 1 point for each solved instance, unless another participant can provide a better solution than yours.

Stated differently, we don't strictly require to provide an optimal solution.
We will assign the point to the best solution we receive.


## Input format

The first line contains two integers, the number `R` of rows, and the number `C` of columns in the map.
The following `R` lines contain `C` integers each, denoting ordinary cells (`0`) or point-of-interests (`D`, with `D > 0`).


## Output format

A line with an integer `N` followed by `N` lines made of two integers `I`,`J`, each pair representing a wall.
`I` ranges from `1` to `R`, and `J` ranges from `1` to `C`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `R` and `C` do not exceed 60
* `D` does not exceed 8
* no point-of-interest in the first and last 8 rows and columns


## Example

Instance:

```
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
```

Possible output:

```
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
```

Checker output:

```
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXX*XXX*X*XXXXXXXX
XXXXXXX*.***.*.*XXXXXXX
XXXXXX*.........*XXXXXX
XXXXX*..3.2.3.3..*XXXXX
XXXX*....1...2..*XXXXXX
XXX*...........*XXXXXXX
XX*.....6....3..*XXXXXX
XXX*...........*XXXXXXX
XXXX*....1....2.*XXXXXX
XXXXX*..3..**1.*XXXXXXX
XXXXXX*...*XX**XXXXXXXX
XXXXXXX*.*XXXXXXXXXXXXX
XXXXXXXX*XXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX

walls: 34
cells inside: 91

CORRECT!
```
