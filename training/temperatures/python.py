import sys
import math

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526
temps = [int(elem) for elem in temps.split()]
absv = [math.fabs(elem) for elem in temps]
mins = [temps[elem] for elem in [i for i, x in enumerate(absv) if x == min(absv)]]

if n != 0:
    result = max(mins)
else:
    result = 0

print result
