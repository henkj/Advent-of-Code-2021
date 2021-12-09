def checkLowPoint(matrix, row, column):
    pointValue = matrix[row][column]
    if row != 0:
        if matrix[row-1][column] <= pointValue:
            return False
    if row != len(matrix)-1:
        if matrix[row+1][column] <= pointValue:
            return False
    if column != 0:
        if matrix[row][column-1] <= pointValue:
            return False
    if column != len(matrix[0])-1:
        if matrix[row][column+1] <= pointValue:
            return False
    return True

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        matrix = [[None for col in range(len(lines[0]))] for row in range(len(lines))]

        rows = len(matrix)
        cols = len(matrix[0])
        lowPoints = []

        for i, line in enumerate(lines):
            for j, point in enumerate(line):
                matrix[i][j] = point
        
        for i in range(rows):
            for j in range(cols):
                if checkLowPoint(matrix, i , j):
                    lowPoints.append(int(matrix[i][j])+1) # +1 for risk level

        sum = 0
        for riskLevel in lowPoints:
            sum += riskLevel

        print(sum)
      
def findSizeOfBasin(cords, pointMatrix, markedMatrix):
    row = cords[0]
    col = cords[1]
    if markedMatrix[row][col] == True:
        return 0
    if pointMatrix[row][col] == '9':
        return 0
    markedMatrix[row][col] = True
    count = 1
    if row != 0:
        count += findSizeOfBasin((row-1, col), pointMatrix, markedMatrix)
    if row != len(pointMatrix)-1:
        count += findSizeOfBasin((row+1, col), pointMatrix, markedMatrix)
    if col != 0:
        count += findSizeOfBasin((row, col-1), pointMatrix, markedMatrix)
    if col != len(pointMatrix[0])-1:
        count += findSizeOfBasin((row, col+1), pointMatrix, markedMatrix)
    return count
    

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        pointMatrix = [[None for col in range(len(lines[0]))] for row in range(len(lines))]
        markedMatrix = [[False for col in range(len(lines[0]))] for row in range(len(lines))]

        rows = len(pointMatrix)
        cols = len(pointMatrix[0])
        lowPoints = []

        for i, line in enumerate(lines):
            for j, point in enumerate(line):
                pointMatrix[i][j] = point
        
        for i in range(rows):
            for j in range(cols):
                if checkLowPoint(pointMatrix, i , j):
                    lowPoints.append((i,j)) 

        basins = []
        for coords in lowPoints:
            basins.append(findSizeOfBasin(coords, pointMatrix, markedMatrix))
        basins.sort()
        product = basins[len(basins)-1] * basins[len(basins)-2] * basins[len(basins)-3]
        
        print(product)
        

part1('Day9/input/input.txt')
part2('Day9/input/input.txt')