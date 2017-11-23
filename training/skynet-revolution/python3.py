import sys
import math

n, l, e = [int(i) for i in input().split()]
n1=[]
for i in range(l):
    n1.append([int(j) for j in input().split()])
ei=[]
for i in range(e):
    ei.append(int(input()))  
    
print(str(n)+' '+str(l)+' '+str(e), file=sys.stderr)
print(str(n1), file=sys.stderr)
print(str(ei), file=sys.stderr)


def form(i):
    return str(i[0])+' '+str(i[1])
    
def adjLinks(node):
    o=[]
    for i in n1:
        if i[0]==node or i[1]==node:
            o.append(i)
    return o
    
def adjNodes(node):
    o=[]
    for i in adjLinks(node):
        if i[0]==node:
            o.append(i[1])
        else:
            o.append(i[0])
    return o

def link(a,b):
    return [i for i in adjLinks(a) if (i[0]==b or i[1]==b)][0]

def distList(a):
    d=[999]*n
    d[a]=0
    it=0
    while (999 in d) and (it<10):
        for i in [i for i in range(len(d)) if d[i]!=999]:
            for j in adjNodes(i):
                if d[j]==999 or d[j]>d[i]+1:
                    d[j]=d[i]+1
        it+=1
        print(d, file=sys.stderr)
        print(str(it)+' / '+str(n), file=sys.stderr)
    return d

def dist(a,b):
    return distList(a)[b]

def closestEnd(si):
    a=[dist(si,i) for i in range(n) if (i in ei)]
    print(a, file=sys.stderr)
    return ei[a.index(min(a))]
    
def closestNode(nodes,node):
    a=[dist(i,node) for i in nodes]
    return nodes[a.index(min(a))]

def isolatedEnd(end):
    return adjNodes(end)==[]

def selLink(e,si):
    return link(e,closestNode(adjNodes(e),si))

while True:
    si = int(input())
    print('End targeted : '+str(closestEnd(si)), file=sys.stderr)
    nextLink=selLink(closestEnd(si),si)
    print(form(nextLink))
    n1.remove(nextLink)
    for i in ei:
        if isolatedEnd(i):
            ei.remove(i)