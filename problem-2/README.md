# Problem 2

Blue Meth, Blue Sky, Heisenberg Blue...
movie directors often like to adapt scientific (or maybe scientif-ish) concepts in their creations.

You are asked to help some of those fellas, who were impressed by the [water jugs riddle in Die Hard 3](https://www.youtube.com/watch?v=BVtQNK_ZUJg&ab_channel=notnek01).

They want to shoot a similar scene, but in a pub, using beer instead of water (obviously, no beer will be wasted, and a drop essentially means that the main actors drink all the beer from a jug).
In order to do the scene as much comical as possible, they ask for the longest sequence of non-repeating configurations that can be achieved using two jugs.

Given the capacities of the two jugs, `A` and `B`, the possible actions are the following:
* `drop_a`, to empty the first jug;
* `drop_b`, to empty the second jub;
* `fill_a`, to fill the first jug;
* `fill_b`, to fill the second jug;
* `a_to_b`, to pour the second jug with the content of the first jug (either until the second jug is full, or until the first jug is empty);
* `b_to_a`, to pour the first jug with the content of the second jug (either until the first jug is full, or until the second jug is empty).

Note that they don't care if the final configuration can be achieved with a shorter sequence...
no one will note, they'll all be drunk for a while anyway.


## Special evaluation rules

You will get 0 points if your solution provides a wrong answer in any tested instance (as usual).
Otherwise, you will get 1 point for each solved instance, unless another participant can provide a better solution than yours.

Stated differently, we don't strictly require to provide an optimal solution.
We will assign the point to the best solution we receive.


## Input format

One line made of two integers, the capacities `A` and `B` of the two jugs.


## Output format

A line with an integer `N` followed by `N` lines, the sequence of actions.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `A` and `B` don't exceed 20
* one between `A` and `B` is odd, and one of them is even
* the longest sequence doesn't exceed 70


## Example

Instance:

```
3 4
```

Possible output:

```
13
fill_a
a_to_b
fill_a
a_to_b
drop_b
a_to_b
fill_b
b_to_a
drop_a
b_to_a
fill_b
b_to_a
fill_b
```

Checker output:

```
STEP  0 - start   [   ] [    ]
STEP  1 - fill_a  [■■■] [    ]
STEP  2 - a_to_b  [   ] [■■■ ]
STEP  3 - fill_a  [■■■] [■■■ ]
STEP  4 - a_to_b  [■■ ] [■■■■]
STEP  5 - drop_b  [■■ ] [    ]
STEP  6 - a_to_b  [   ] [■■  ]
STEP  7 - fill_b  [   ] [■■■■]
STEP  8 - b_to_a  [■■■] [■   ]
STEP  9 - drop_a  [   ] [■   ]
STEP 10 - b_to_a  [■  ] [    ]
STEP 11 - fill_b  [■  ] [■■■■]
STEP 12 - b_to_a  [■■■] [■■  ]
STEP 13 - fill_b  [■■■] [■■■■]
CORRECT!
```
