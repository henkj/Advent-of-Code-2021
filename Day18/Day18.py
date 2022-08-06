import sys
import re

def processPair(pair, depth, leftVal, rightVal):

    if isinstance(pair[0], int) and isinstance(pair[1], int) and depth > 4:
        return True, pair

    processPair(pair[0], depth+1, leftVal, rightVal)
    processPair(pair[1], depth+1, leftVal, rightVal)
    
    return False, None

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        listOfPairs = []
        for line in lines:
             listOfPairs.append(eval(line))
        
        for pair in listOfPairs:
            processPair(pair, 1, -1, -1)
            

part1('Day18/input/testinput.txt')
#part2('Day17/input/input.txt')