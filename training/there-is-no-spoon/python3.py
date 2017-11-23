import sys
import math



line=[]
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line.append(input())

def right(x,y):
    a = -1
    b = -1
    l=[i for i in line[y]]
    for i in range(x+1,width):
        if l[i]=='0':
            a=i
            b=y
            break
    return str(a)+' '+str(b)

def down(x,y):
    a = -1
    b = -1
    c=[[j for j in i][x] for i in line]
    for i in range(y+1,height):
        if c[i]=='0':
            a=x
            b=i
            break
    return str(a)+' '+str(b)


for j in range(height):
    l=[i for i in line[j]]
    for i in range(width):
        if l[i]=='0':
            print(str(i)+' '+str(j)+' '+right(i,j)+' '+down(i,j))