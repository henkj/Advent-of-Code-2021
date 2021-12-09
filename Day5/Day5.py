
import re

def updateCoordinates(nrList, usedCoordinates, considerDiagonals):
    def getAllCoordinates(x1, y1, x2, y2):
        cords = []
        if not considerDiagonals and x1 != x2 and y1 != y2:
            return cords
        while x1 != x2 or y1 != y2:
            cords.append((x1,y1))
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            elif y1 > y2:
                y1 -= 1
        cords.append((x1,y1))
        return cords

    cordList = getAllCoordinates(nrList[0],nrList[1],nrList[2],nrList[3])
    
    for cords in cordList:
        if cords in usedCoordinates.keys():
            usedCoordinates[cords] += usedCoordinates[cords]
        else:
            usedCoordinates[cords] = 1
    return     

def countOverlaps(usedCoordinates):
    count = 0
    for key, value in usedCoordinates.items():
        if value > 1:
            count += 1
    return count

def part1(input, considerDiagonals = False):
    usedCoordinates = {}
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        for line in lines:
            nrList = re.split("-|>| |,", line)
            nrList = list(filter(None, nrList))
            nrList = list(map(int,nrList))
            updateCoordinates(nrList, usedCoordinates, considerDiagonals)

    overlaps = countOverlaps(usedCoordinates)
    print("Overlaps: " + str(overlaps))
    return        

def part2(input):
    part1(input, True)



part1('Day5/input/input.txt')
part2('Day5/input/input.txt')