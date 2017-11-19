import sys
import math

n = int(raw_input())
pi=[int(raw_input()) for i in range(n)]
pi=sorted(pi)

print min([pi[i]-pi[i-1] for i in range(1,len(pi))])
