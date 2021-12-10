def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        lines = [s.split(',') for s in lines]
        positions = [int(s) for s in lines[0]]
        positions.sort()
        
        median = positions[round(len(positions)/2)]
        
        fuelNeeded = 0
        for pos in positions:
            fuelNeeded += abs(pos-median)
    print(fuelNeeded)

def sumOfNumbers(number):
    if number % 2 == 0:
        return (number+1)*number/2
    else:
        return sumOfNumbers(number+1)-(number+1)

def getFuelNeeded(index, positions):
    fuelNeeded = 0
    for pos in positions:
        fuelNeeded += sumOfNumbers(abs(pos - index))
    return fuelNeeded


def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        lines = [s.split(',') for s in lines]
        positions = [int(s) for s in lines[0]]
        
        leastFuel = float('inf')
        for index in range(0,len(positions)):
            fuelNeeded = getFuelNeeded(index, positions)
            if fuelNeeded < leastFuel:
                leastFuel = fuelNeeded
                bestPos = index
        
        print("Best value: " + str(bestPos))
        print("Least fuel needed: " + str(leastFuel))
 



part1('Day07/input/input.txt')
part2('Day07/input/input.txt')