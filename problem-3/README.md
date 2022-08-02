# Problem 3

Hello Great Builder!
Now that you had a couple of beers, it's time to work again on some construction project.

We have islands, and we have to connect them with bridges.
One or two bridges can connect islands that are in the same row or in the same column.
Bridges cannot go above islands, and cannot cross each other.

Looks at those numbers in each island...
they tell us how many bridges are expected to reach those islands!
And we expect that after the bridges are built, inhabitants of each island will have the possibility to reach all other islands with their cars (ie. there must be at least one path of bridges connecting each pair of islands).


## Input format

The first line contains two integers, the number `R` of rows, and the number `C` of columns in the map.
The following `R` lines contain `C` integers each, denoting water (`0`) or islands (`B`, with `B > 0`).


## Output format

A line with an integer `N` followed by `N` lines made of four integers `I J I' J'`, representing a bridge connection the islands in `(I,J)` and `(I',J')`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `R` and `C` do not exceed 50
* `B` does not exceed 8


## Example

Instance:

```
7 7
3 0 2 0 3 0 3 
0 1 0 0 0 2 0 
0 0 0 0 0 0 0 
6 0 0 0 0 3 0 
0 0 0 0 0 0 0 
0 1 0 0 0 0 2 
3 0 0 0 0 1 0 
```

Possible output:

```
15
0 2 0 4
0 0 3 0
0 4 0 6
3 0 6 0
1 5 3 5
3 0 3 5
5 1 5 6
0 4 0 6
0 0 0 2
3 0 3 5
6 0 6 5
0 6 5 6
0 0 3 0
1 1 1 5
3 0 6 0
```

Checker output:

```
3---2---3===3
║...........|
║.1-------2.|
║.........|.|
║.........|.|
║.........|.|
6=========3.|
║...........|
║...........|
║...........|
║.1---------2
║............
3---------1..
CORRECT!
```