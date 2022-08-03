# Problem 4

_The problem is adapted from [Lightbot: Code Hour](https://lightbot.com/hour-of-code.html), we called it **RoBeep!**, and instances are taken/adapted from the game._


Hello RoBeep!
You have to program a small robot to turn on some light bulbs.
The robot moves in a grid, but cells may be of different heights.

The robot can move forward, turn left, turn right, jump, and *beep* to turn on/off light bulbs.
It's memory is quite limited, and can accommodate only a few instructions.
For the most challenging scenarios, an additional memory slot is provided to store an additional procedure.

In detail, the main procedure of the robot can execute the following actions:
* `nop`, no operation
* `forward`, move one step forward if the reaching cell is at the same height of the starting cell, otherwise the robot doesn't move
* `jump`, move on step forward if the reaching cell is one level below or above the starting cell, otherwise the robot doesn't move
* `right`, to rotate clockwise
* `left`, to rotate counterclockwise
* `beep`, to change the state of the light bulb in the cell hosting the robot, if any
* `subroutine`, to execute the subroutine from the first to the last instruction

The subroutine procedure is made of the same actions above, but it cannot call itself or the main procedure.


## Input format

The first line contains eight integers, `R C Ri Ci Di M S T`:
* `R`, the number of rows
* `C`, the number of columns
* `Ri`, the row where the robot is initially located
* `Ci`, the column where the robot is initially located
* `Di`, the initial direction of the robot (0 for up, 1 for right, 2 for down, 3 for left)
* `M`, the number of instructions that can be stored in the main procedure
* `S`, the number of instructions that can be stored in the subroutine
* `T`, the number of target cells, ie. those containing light bulbs, all of them initially turned off

The next `R` lines contains `C` integers each, denoting the height of cells (or `-1` for holes, i.e. unreachable cells).

The last `T` lines contain 2 integers each, representing the coordinates of light bulbs.


## Output format

Two lines listing the actions stored in the main procedure and in the subroutine.
Actions are separated by space, and the two lines are terminated by a period (preceded by space, ie. <code>&nbsp;.</code>; the space can be omitted for lines containing no actions).


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `R` and `C` do not exceed 5
* `M` and `S` do not exceed 12
* `T` does not exceed 4
* the height of cells does not exceed 4


## Example

Instance:

```
1 2 0 0 0 8 0 1
0 1
0 1
```

Possible output:

```
right jump beep right right left right nop .
.
```

Checker output:

```
^0  1.

MAIN: [right]  jump   beep   right   right   left   right   nop  
 SUB: 

>0  1.

MAIN:  right  [jump]  beep   right   right   left   right   nop  
 SUB: 

 0 >1.

MAIN:  right   jump  [beep]  right   right   left   right   nop  
 SUB: 

 0 >1o

MAIN:  right   jump   beep  [right]  right   left   right   nop  
 SUB: 

 0 v1o

MAIN:  right   jump   beep   right  [right]  left   right   nop  
 SUB: 

 0 <1o

MAIN:  right   jump   beep   right   right  [left]  right   nop  
 SUB: 

 0 v1o

MAIN:  right   jump   beep   right   right   left  [right]  nop  
 SUB: 

 0 <1o

MAIN:  right   jump   beep   right   right   left   right  [nop] 
 SUB: 

 0 <1o

MAIN:  right   jump   beep   right   right   left   right   nop  
 SUB: 

CORRECT!
```
