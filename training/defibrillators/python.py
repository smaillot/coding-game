import sys
import math

def convFloat(s):
    return float('.'.join(s.split(',')))

defib=[]
lon = convFloat(raw_input())
lat = convFloat(raw_input())
n = int(raw_input())
for i in range(n):
    defib.append(raw_input())

def dist(lonB,latB):
    return 6371*math.sqrt(((lonB-lon)*math.cos(math.radians((lonB+lon)/2)))**2+(latB-lat)**2)


names=[i.split(';')[1] for i in defib]
dist=[dist(convFloat(i.split(';')[4]),convFloat(i.split(';')[5])) for i in defib]

print names[dist.index(min(dist))]
