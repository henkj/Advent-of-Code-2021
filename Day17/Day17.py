import sys
import re

def checkHighestPoint(highestYVel):
    if highestYVel == 0:
        return 0
    return highestYVel + checkHighestPoint(highestYVel-1)
    

def fireProbe(xVel, yVel, targetArea):
    pos = [0, 0]
    while pos[0] <= targetArea[1] and pos[1] >= targetArea[2]:
        pos[0] += xVel
        if xVel != 0:
            xVel -= 1
        pos[1] += yVel
        yVel -= 1
        if pos[0] >= targetArea[0] and pos[0] <= targetArea[1] and pos[1] >= targetArea[2] and pos[1] <= targetArea[3]:
            return True
    return False

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        areaLine = lines[0]

        area = re.findall(r'-?\d+', areaLine)
        area = [int(nr) for nr in area]

        highestYVel = -999999
        for xVel in range(1000):
            for yVel in range(1000):
                success = fireProbe(xVel, yVel, area)
                if success:
                    successAchieved = True
                    if yVel > highestYVel:
                        highestYVel = yVel
                

        highestYValue = checkHighestPoint(highestYVel)
        print(highestYValue)


def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        areaLine = lines[0]

        area = re.findall(r'-?\d+', areaLine)
        area = [int(nr) for nr in area]

        count = 0
        successvectors = []
        for xVel in range(1000):
            for yVel in range(area[2],1000):
                success = fireProbe(xVel, yVel, area)
                if success:
                    count += 1
                    successvectors.append((xVel, yVel))
                    
                

        print(count)
        print(successvectors)

part1('Day17/input/input.txt')
part2('Day17/input/input.txt')