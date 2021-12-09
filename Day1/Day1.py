

def part1():
    with open('Day1/input/input.txt') as f:
      lines = f.readlines()
    prevLine = ""
    count = 0
    for line in lines:
        if prevLine != "" and int(line) > int(prevLine):
           count = count + 1
        prevLine = line
    print(count)

def part2():
    with open('Day1/input/input.txt') as f:
      lines = f.readlines()
    prevScore = ""
    count = 0
    for idx, value in enumerate(lines):
        if(idx < len(lines)-2):
            newScore = int(lines[idx]) + int(lines[idx+1]) + int(lines[idx+2])
            if(prevScore != "" and newScore > prevScore):
                count = count + 1
            prevScore = newScore
    print(count)

part1()
part2()