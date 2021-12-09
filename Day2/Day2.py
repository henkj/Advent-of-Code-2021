import re

def part1(input):
    with open(input) as f:
        lines = f.readlines()
    pos = 0
    depth = 0
    for line in lines:
        change = re.findall(r'\d+', line)[0]
        change = int(change)
        if line.startswith('forward'):
            pos += change
        elif line.startswith('up'):
            depth -= change
        else:
            depth += change
        #print('Position: ' + str(pos) + "  Depth: " + str(depth) )
    print(depth*pos)

def part2(input):
    with open(input) as f:
        lines = f.readlines()
    aim = 0
    pos = 0
    depth = 0
    for line in lines:
        change = re.findall(r'\d+', line)[0]
        change = int(change)
        if line.startswith('forward'):
            pos += change
            depth += (change*aim)
        elif line.startswith('up'):
            aim -= change
        else:
            aim += change
        #print('Position: ' + str(pos) + "  Depth: " + str(depth) + "  Aim: " + str(aim))
    print(depth*pos)


#part1('Day2/input/testinput.txt')
part1('Day2/input/input.txt')

#part2('Day2/input/testinput.txt')
part2('Day2/input/input.txt')