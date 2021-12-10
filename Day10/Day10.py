import math

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        lefts = ['(', '[', '{', '<']
        rights = [')', ']', '}', '>']

        illegals = []
        for line in lines:
            stack = []
            for char in line:
                if char in lefts:
                    stack.append(rights[lefts.index(char)])
                elif char in rights:
                    if len(stack) == 0:
                        illegals.append(char)
                        break

                    otherChar = stack.pop()
                    if otherChar != char:
                        illegals.append(char)
                        break
        sum = 0
        for char in illegals:
            if char == ')':
                sum += 3
            elif char == ']':
                sum += 57
            elif char == '}':
                sum += 1197
            elif char == '>':
                sum += 25137
        
        print(sum)
       
def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        lefts = ['(', '[', '{', '<']
        rights = [')', ']', '}', '>']

        sums = []
        for line in lines:
            stack = []
            illegals = []
            for char in line:
                if char in lefts:
                    stack.append(rights[lefts.index(char)])
                elif char in rights:
                    if len(stack) == 0:
                        illegals.append(char)
                        break

                    otherChar = stack.pop()
                    if otherChar != char:
                        illegals.append(char)
                        break

            if len(stack) != 0 and len(illegals) == 0:
                stack.reverse()
                sum = 0
                for char in stack:
                    if char == ')':
                        sum = sum * 5 + 1
                    elif char == ']':
                        sum = sum * 5 + 2
                    elif char == '}':
                        sum = sum * 5 + 3
                    elif char == '>':
                        sum = sum * 5 + 4
                sums.append(sum)
        sums.sort()
        print(sums[math.floor(len(sums)/2)])
        

part1('Day10/input/input.txt')
part2('Day10/input/input.txt')