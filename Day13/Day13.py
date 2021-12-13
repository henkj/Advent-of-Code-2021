
def findCoord(coords, xValue, yValue):
    for coord in coords:
        if coord[0] == xValue and coord[1] == yValue:
            return True
    return False

def foldPaper(coords, instruction):
    copycoords = coords.copy()
    if instruction[0] == 'x':
        for coord in copycoords:
            if coord[0] > instruction[1]:
                yValue = coord[1]
                xValue = 2*instruction[1] - coord[0]
                coords.remove(coord)
                if not findCoord(coords, xValue, yValue):
                    coords.append((xValue, yValue))
    else:
        for coord in copycoords:
            if coord[1] > instruction[1]: 
                xValue = coord[0]
                yValue = 2*instruction[1] - coord[1]
                coords.remove(coord)
                if not findCoord(coords, xValue, yValue):
                    coords.append((xValue, yValue))
    return coords

def displayGrid(coords):
    coords.sort(key = lambda x: (x[1], x[0]))

    highestX = 0
    highestY = 0
    last = (0,0)
    string = ""

    for coord in coords:
        if coord[0] > highestX:
            highestX = coord[0]
        if coord[1] > highestY:
            highestY = coord[1]

    for coord in coords:
        if last[1] == coord[1]:
            if last[0] == coord[0]:
                string += '#'
            else:
                string += ' ' * (coord[0]-last[0]-1)
                string += '#'
                last = coord
        else:
            if last[0] != highestX:
                string += ' ' * (highestX-last[0]-1)
                print(string)
                string = ""
            else:
                print(string)
                string = ""
            string += ' ' * (coord[0]-1)
            string += '#'
            last = coord
    print(string)


def part1(input, part2=False):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        coords = []
        instructions = []
        

        for line in lines:
            if line == "":
                continue
            if line.find("fold") == -1:
                temp = line.split(',')
                coords.append((int(temp[0]), int(temp[1])))
            else:
                index = line.find("=")
                instructions.append((line[index-1:index], int(line[index+1:])))
    
        for i,instruction in enumerate(instructions):
            coords = foldPaper(coords, instruction)
            if i == 0 and not part2:
                print(len(coords))
        
        if part2:
            displayGrid(coords)

def part2(input):
    part1(input, True)           

part1('Day13/input/input.txt')
part2('Day13/input/input.txt')