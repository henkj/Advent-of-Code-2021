import sys

def checkNeighbour(value, row, col, matrix, visited, distances):
    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1:
        return
    if visited[row][col]:
        return
    if distances[row][col] > value + matrix[row][col]:
        distances[row][col] = value + matrix[row][col]
    return 

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        matrix = [[int(col) for col in row] for row in lines]
        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        distances = [[sys.maxsize for i in range(len(matrix[0]))] for j in range(len(matrix))]
        distances[0][0] = matrix[0][0]
        
        endVisited = False
        row = 0
        col = 0

        while not endVisited:
            checkNeighbour(distances[row][col], row-1, col, matrix, visited, distances)
            checkNeighbour(distances[row][col], row, col-1, matrix, visited, distances)
            checkNeighbour(distances[row][col], row+1, col, matrix, visited, distances)
            checkNeighbour(distances[row][col], row, col+1, matrix, visited, distances)

            visited[row][col] = True
            if row == len(matrix)-1 and col == len(matrix[0])-1:
                distance = distances[row][col]
                endVisited = True

            shortest = sys.maxsize
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if not visited[i][j]:
                        if distances[i][j] < shortest:
                            shortest = distances[i][j]
                            row = i
                            col = j
        


        print(distance-distances[0][0])

def multiplyMatrix(matrix):
    newMatrix = [[0 for col in range(5*len(matrix[0]))] for row in range(5*len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            origValue = matrix[i][j]
           # newMatrix[i][j] = value
            for n in range(5):
                for m in range(5):
                    value = origValue + (n+m)
                    while value > 9:
                        value -= 9
                    row = i + n * len(matrix)
                    col = j + m * len(matrix[0])
                    newMatrix[row][col] = value
    return newMatrix
            
def checkNeighbour2(value, row, col, matrix, visited, distances, toCheck):
    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1:
        return
    if visited[row][col]:
        return
    if distances[row][col] > value + matrix[row][col]:
        if distances[row][col] == sys.maxsize:
            toCheck.append((row, col))
        distances[row][col] = value + matrix[row][col]
    return             

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        matrix = [[int(col) for col in row] for row in lines]
        matrix = multiplyMatrix(matrix)

        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        distances = [[sys.maxsize for i in range(len(matrix[0]))] for j in range(len(matrix))]
        distances[0][0] = matrix[0][0]
        
        endVisited = False
        row = 0
        col = 0

        toCheck = [(0, 0)]

        while not endVisited:
            checkNeighbour2(distances[row][col], row-1, col, matrix, visited, distances, toCheck)
            checkNeighbour2(distances[row][col], row, col-1, matrix, visited, distances, toCheck)
            checkNeighbour2(distances[row][col], row+1, col, matrix, visited, distances, toCheck)
            checkNeighbour2(distances[row][col], row, col+1, matrix, visited, distances, toCheck)

            visited[row][col] = True
            toCheck.remove((row, col))
            if row == len(matrix)-1 and col == len(matrix[0])-1:
                distance = distances[row][col]
                endVisited = True

            shortest = sys.maxsize
            for tuple in toCheck:
                if distances[tuple[0]][tuple[1]] < shortest:
                    shortest = distances[tuple[0]][tuple[1]]
                    row = tuple[0]
                    col = tuple[1]

        print(distance-distances[0][0])

part1('Day15/input/input.txt')
part2('Day15/input/input.txt')