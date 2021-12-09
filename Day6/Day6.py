
def processFish(fishStatus):
    newFishStatus = []
    newSpawns = 0
    for lanternFish in fishStatus:
        if lanternFish == 0:
            newFishStatus.append(6)
            newSpawns += 1
        else:
            newFishStatus.append(lanternFish-1)
    for n in range(0,newSpawns):
        newFishStatus.append(8)
    return newFishStatus

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        line = lines[0]
        fish = [int(s) for s in line.split(',')]
        
        i = 0
        while(i < 80):
            fish = processFish(fish)
            i += 1
            #print(fish)
        print(len(fish))
        
def fishSpawned(fish, time):
    if fish < time:
        return 0
    else:
        return

def processFish2(fishStatus):
    newSpawns = 0
    for n in range(0,9):
        if n == 0:
            newSpawns = fishStatus[0]
            fishStatus[0] = 0
        else:
            fishStatus[n-1] = fishStatus[n]
            fishStatus[n] = 0
        
    fishStatus[8] = newSpawns
    fishStatus[6] += newSpawns    
    return fishStatus

def part2(input):
    fishCount = [0]*9
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        line = lines[0]
        fish = [int(s) for s in line.split(',')]

        for lanternfish in fish:
            fishCount[lanternfish] += 1

        i = 0
        while(i < 256):
            fishCount = processFish2(fishCount)
            i += 1
            #print(fish)

        count = 0
        for countedFish in fishCount:
            count += countedFish
        print(count)



#part1('Advent of Code 2021/Day6/testinput.txt')
#part1('Advent of Code 2021/Day6/input.txt')

#part2('Advent of Code 2021/Day6/testinput.txt')
part2('Advent of Code 2021/Day6/input.txt')