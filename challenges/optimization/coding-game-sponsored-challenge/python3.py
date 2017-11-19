import sys
import math
import numpy as np
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sizeX = int(input())
sizeY = int(input())
n = int(input())


def matlab(map,x,y):
    mat="["
    for j in range(sizeY):
        for i in range(sizeX):
            mat+=str(map[i][j])+' '
        if j != sizeY-1:
            mat+=";"
    mat+="]"
    return mat

def num(char):
    if char=='#':
        return 2
    if char=='_':
        return 1

def possible(wallUp,wallRight,wallDown,wallLeft):
    poss=[]
    if wallRight=='_':
        poss.append('A')
    elif wallDown=='_':
        poss.append('C')
    elif wallLeft=='_':
        poss.append('E')
    elif wallUp=='_':
        poss.append('D')
    return poss

def dist(x,y,xFant,yFant):
    return math.fabs(x-xFant)+math.fabs(y-yFant)

def distMov(x,y,xFant,yFant,mov):
    x2=x
    y2=y
    if mov=='A':
        x2+=1
    if mov=='C':
        y2+=1
    if mov=='E':
        x2-=1
    if mov=='D':
        y2-=1
    return dist(x2,y2,xFant,yFant)

def bestMove(x,y,xvFant,yvFant,movs):
    move=''
    best=0
    for i in range(len(xvFant)):
        for m in movs:
            if distMov(x,y,xvFant[i],yvFant[i],m) > best:
                best = distMov(x,y,xvFant[i],yvFant[i],m)
                move=m
    return m

def minDistFant(x,y,xvFant,yvFant):
    min=dist(x,y,xvFant[0],xvFant[0])
    for i in range(1,len(xvFant)):
        if dist(x,y,xvFant[i],xvFant[i]) < min:
            min =  dist(x,y,xvFant[i],xvFant[i])
    return min

x=[]
y=[]
for i in range(n):
    x.append(0)
    y.append(0)
c=0
XY=[]
map=[['0']*sizeY]*sizeX
map[1][5]=1
solution=[]#'E','E','E','E','E','E','E','C','C','C','E','E','E','E','E','C','C','C','A','A','A','A','A','A','A','A','A','A','A','A','A','A','D','D','D','A','A','A','D','D','D','A','A','A','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','A','A','A','A','A','D','D','D']#,'E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E','C','C','C','A','A','A','C','C','C','E','E','E','C','C','C','C','C','C','A','A','A','A','A','A','A','A','A']
# game loop
while True:
    wallUp = input()
    wallRight = input()
    wallDown = input()
    wallLeft = input()
    for i in range(n):
        x[i], y[i] = [int(j) for j in input().split()]

    XY.append(str(x[n-1]) + ',' + str(y[n-1]) + ':' + wallUp + wallRight + wallDown + wallLeft)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if c < len(solution):
        print(solution[c])
    else:
        if minDistFant(x[n-1],y[n-1],x[0:n-2],y[0:n-2]) > 5:
            print(random.sample(possible(wallUp,wallRight,wallDown,wallLeft), 1)[0])
        else:
            print(bestMove(x[n-1],y[n-1],x[0:n-2],y[0:n-2],possible(wallUp,wallRight,wallDown,wallLeft)))
    c+=1
