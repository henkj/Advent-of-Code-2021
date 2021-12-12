
def smallCave(input):
    if input.islower():
        return True
    return False

def visited(node, visitMap):
    if visitMap.get(node) == None:
        return False
    return True

def processNode(node, visitMap, connections):
    visitMapCopy = visitMap.copy()
    if node == "end":
        return 1
    if smallCave(node):
        if visited(node, visitMapCopy):
            return 0
        else:
            visitMapCopy[node] = True
    endNodes = 0
    for connection in connections:
        if connection[0] == node:
            endNodes += processNode(connection[1], visitMapCopy, connections)
        if connection[1] == node:
            endNodes += processNode(connection[0], visitMapCopy, connections)
    return endNodes

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        pathCount = 0
        connections = []
        visitMap = {}
        for line in lines:
            connections.append(line.split('-'))
        
        pathCount += processNode("start", visitMap, connections)

        print(pathCount)

def smallCaveVisitedTwice(visitMapCopy):
    for node, visits in visitMapCopy.items():
        if visits == 2:
            return True 
    return False

def processNode2(node, visitMap, connections):
    visitMapCopy = visitMap.copy()
    if node == "end":
        return 1
    if node == "start" and visited(node, visitMapCopy):
        return 0
    if smallCave(node):
        if visited(node, visitMapCopy):
            if smallCaveVisitedTwice(visitMapCopy):
                return 0
            else:
                visitMapCopy[node] = 2
        else:
            visitMapCopy[node] = 1
    endNodes = 0
    for connection in connections:
        if connection[0] == node:
            endNodes += processNode2(connection[1], visitMapCopy, connections)
        if connection[1] == node:
            endNodes += processNode2(connection[0], visitMapCopy, connections)
    return endNodes

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        pathCount = 0
        connections = []
        visitMap = {}
        for line in lines:
            connections.append(line.split('-'))
        
        pathCount += processNode2("start", visitMap, connections)

        print(pathCount)


part1('Day12/input/input.txt')
part2('Day12/input/input.txt')