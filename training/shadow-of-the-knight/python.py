import sys
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]
possible = [[0, w-1], [0, h-1]]

def debug_print(str):
    print >> sys.stderr, str
    
def center(vect):
    if np.mod(vect[-1] - vect[0], 2) == 0:
        return (vect[0] + vect[-1]) / 2
    else:
        return center([vect[0], vect[-1]-1])
    
def choose_next(possible):
    
    return [center([possible[0][0], possible[0][1]]), center([possible[1][0], possible[1][1]])]
    
def update_possible(possible, pose, bomb):
    
    x = [possible[0][0], possible[0][1]]
    y = [possible[1][0], possible[1][1]]
    
    if bomb[0] == 'U':
        y = [y[0],pose[1]]
    elif bomb[0] == 'D':
        y = [pose[1]+1,y[-1]]
    else:
        y = [pose[1], pose[1]]
        
    if bomb[-1] == 'L':
        x = [x[0],pose[0]]
    elif bomb[-1] == 'R':
        x = [pose[0]+1,x[-1]]
    else:
        x = [pose[0], pose[0]]
        
    debug_print(x)
    debug_print(y)
        
    return [x, y]
    
# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    debug_print((x0, y0))
    debug_print(bomb_dir)
    debug_print(possible)
    possible = update_possible(possible, [x0, y0], bomb_dir)
    debug_print(possible)
    res=choose_next(possible)
    debug_print(res)
    x0, y0 = res
    
    print str(res[0]) + " " + str(res[1])