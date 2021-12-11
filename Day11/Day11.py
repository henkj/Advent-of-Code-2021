def processFlash(row, col, energyMatrix, truthMatrix):
    if row < 0 or col < 0 or row > len(energyMatrix)-1 or col > len(energyMatrix[0])-1:
        return 0
    if truthMatrix[row][col] == True:
        return 0
    energyMatrix[row][col] += 1
    if not energyMatrix[row][col] > 9:
        return 0
    truthMatrix[row][col] = True
    sum = 1
    sum += processFlash(row-1, col-1, energyMatrix, truthMatrix)   # topleft
    sum += processFlash(row-1, col, energyMatrix, truthMatrix)     # top
    sum += processFlash(row-1, col+1, energyMatrix, truthMatrix)   # topright
    sum += processFlash(row, col-1, energyMatrix, truthMatrix)     # left
    sum += processFlash(row, col+1, energyMatrix, truthMatrix)     # right
    sum += processFlash(row+1, col-1, energyMatrix, truthMatrix)   # botleft
    sum += processFlash(row+1, col, energyMatrix, truthMatrix)     # bot
    sum += processFlash(row+1, col+1, energyMatrix, truthMatrix)   # botright
    energyMatrix[row][col] = 0
    return sum



def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        truthMatrix = [[False for col in row] for row in lines]
        energyMatrix = [[int(col) for col in row] for row in lines]
        rowLength = len(energyMatrix)
        colLength = len(energyMatrix[0])

        flashCount = 0
        for step in range(100):
            for i in range(rowLength):
                for j in range(colLength):
                    energyMatrix[i][j] += 1

            for i in range(rowLength):
                for j in range(colLength):
                    if energyMatrix[i][j] > 9:
                        flashCount += processFlash(i, j, energyMatrix, truthMatrix)
            
            truthMatrix = [[False for col in row] for row in lines] # reset
        
        print(flashCount)

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        truthMatrix = [[False for col in row] for row in lines]
        energyMatrix = [[int(col) for col in row] for row in lines]
        rowLength = len(energyMatrix)
        colLength = len(energyMatrix[0])
        sizeOfMatrix = rowLength * colLength

        flashCount = 0
        step = 0
        while flashCount != sizeOfMatrix:
            step += 1
            for i in range(rowLength):
                for j in range(colLength):
                    energyMatrix[i][j] += 1

            for i in range(rowLength):
                for j in range(colLength):
                    if energyMatrix[i][j] > 9:
                        flashCount = processFlash(i, j, energyMatrix, truthMatrix)
            
            truthMatrix = [[False for col in row] for row in lines] # reset
        
        print(step)

part1('Day11/input/input.txt')
part2('Day11/input/input.txt')