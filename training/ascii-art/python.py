import sys
import math

l = int(raw_input())
h = int(raw_input())
t = raw_input()
row = []
for i in range(h):
    row.append(raw_input())

def NumLet2Art(numLet,line):
    line = row[line]
    return line[(numLet)*l:(numLet+1)*l]

def Let2Num(let):
    if ord(let) >= ord('a') and ord(let) <= ord('z'):
        return ord(let)-ord('a')
    elif ord(let) >= ord('A') and ord(let) <= ord('Z'):
        return ord(let)-ord('A')
    else:
        return 26

for i in range(h):
    line=""
    for j in range(len(t)):
        line+=NumLet2Art(Let2Num(t[j]),i)
    print line
