import sys
import math

# Save humans, destroy zombies!

def dist(x,y,X,Y):
    return math.sqrt(math.pow(X-x,2)+math.pow(Y-y,2))

def closestID(x,y,list):
    min=99999
    best=0
    for i in range(len(list)):
        if dist(x,y,list[i][1],list[i][2]) < min:
            min = dist(x,y,list[i][1],list[i][2])
            best = i
    return best

def closestDist(x,y,list):
    min=99999
    best=0
    for i in range(len(list)):
        if dist(x,y,list[i][1],list[i][2]) < min:
            min = dist(x,y,list[i][1],list[i][2])
            best = i
    return min

def canSave(x,y,human,zombies):
    return (max(0,dist(x,y,human[1],human[2])-2000)/1000)>(closestDist(human[1],human[2],zombies)/400)

def saveRatio(x,y,human,zombies):
    return (closestDist(human[1],human[2],zombies)/400)/(max(0.00001,dist(x,y,human[1],human[2])-2000)/1000)

# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    human=[]
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        human.append([human_id, human_x, human_y])
    zombie_count = int(input())
    zombies=[]
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append([zombie_id, zombie_x, zombie_y])

    target_x=human[0][1]
    target_y=human[0][2]
    min_ratio = 0
    for i in range(len(human)):
        if saveRatio(x,y,human[i],zombies) > min_ratio:
            min_ratio = saveRatio(x,y,human[i],zombies)
            target_x=human[i][1]
            target_y=human[i][2]

    print(str(target_x) + ' ' + str(target_y))
