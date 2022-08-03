# Problem 5

_The problem is [the Slant puzzle](https://www.puzzle-slant.com/) and instances are taken/adapted from the game._


Hello Great Builder!
One last mission for you, again regarding islands and bridges.
This time, we will be as much anti-green as possible.
We will cover the map with bridges, all of them diagonals, and not necessarily connecting islands.
The only requirements regard the number of bridges reaching islands, and the avoiding of cycles.
Can you do such an environmental monster for us?


## Input format

The first line contains one integers, the number `S` of rows and columns in the map.
The next `S+1` lines contain `S+1` integers each, denoting an empty point (`-1`) or an island that must be reached by `B` bridges (with `B >= 0`).


## Output format

`S` lines of `S` characters each.
Characters must be `\` or `/`, depending on the bridge to be built on that cell.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` does not exceed 20
* `B` does not exceed 4


## Example

Instance:

```
5
-1 0 2 1 -1 -1 
1 3 -1 -1 1 -1 
-1 2 1 -1 -1 -1 
-1 1 -1 2 -1 -1 
-1 2 -1 -1 3 0 
-1 -1 -1 2 -1 -1 
```

Possible output:

```
\/\\\
\\\\/
\\///
\////
\/\/\
```

Checker output:

```
o 0 2 1 o o
 \ / \ \ \ 
1 3 o o 1 o
 \ \ \ \ / 
o 2 1 o o o
 \ \ / / / 
o 1 o 2 o o
 \ / / / / 
o 2 o o 3 0
 \ / \ / \ 
o o o 2 o o
CORRECT!
```
