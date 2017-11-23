import sys
import math



line=[]
width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
for i in xrange(height):
    line.append(raw_input())

def right(x,y):
    a = -1
    b = -1
    l=[i for i in line[y]]
    print >> sys.stderr, '\nRIGHT : '
    print >> sys.stderr, 'ligne : '+str(l)
    print >> sys.stderr, str(range(x+1,width))
    for i in range(x+1,width):
        print >> sys.stderr, 'x = '+str(i)
        if l[i]=='0':
            a=i
            b=y
            print >> sys.stderr, 'MAJ ! '+str(a)+' '+str(b)
            break
    return str(a)+' '+str(b)

def down(x,y):
    a = -1
    b = -1
    c=[[j for j in i][x] for i in line]
    print >> sys.stderr, '\nDOWN : '
    print >> sys.stderr, 'colonne : '+str(c)
    print >> sys.stderr, str(range(y+1,height))
    for i in range(y+1,height):
        print >> sys.stderr, 'y = '+str(i)
        if c[i]=='0':
            a=x
            b=i
            print >> sys.stderr, 'MAJ ! '+str(a)+' '+str(b)
            break
    return str(a)+' '+str(b)


for j in range(height):
    print >> sys.stderr, '\nline '+str(j)
    l=[i for i in line[j]]
    for i in range(width):
        print >> sys.stderr, 'analysing '+str(i)+' '+str(j)
        if l[i]=='0':
            print >> sys.stderr, '\nFOUND '+str(i)+' '+str(j)+' '+right(i,j)+' '+down(i,j)
            print str(i)+' '+str(j)+' '+right(i,j)+' '+down(i,j)