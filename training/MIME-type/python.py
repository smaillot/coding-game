import sys
import math

n = int(raw_input())
q = int(raw_input())
MIME={None : 'UNKNOWN'}
for i in range(n):
    ext, mt = raw_input().split()
    MIME[ext.lower()]=mt
for i in range(q):
    fname = raw_input().lower()
    if (str(fname).split('.')[len(fname.split('.'))-1] in MIME) and (fname.find('.') != -1):
        print MIME[str(fname).split('.')[len(fname.split('.'))-1]]
    else:
        print 'UNKNOWN'
