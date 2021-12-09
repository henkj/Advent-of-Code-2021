def part1(input):
    with open(input) as f:
        input = []
        output = []
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        for line in lines:
            inputoutput = line.split('|')
            inputoutput = [s.split(" ") for s in inputoutput]
            input.append(list(filter(None,inputoutput[0])))
            output.append(list(filter(None, inputoutput[1])))
        
        count = 0
        for line in output:
            for value in line:
                if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
                    count += 1
        print(count)

def mostCommon(list):
    largest = 0
    letters = [0]*7
    index = -1
    for line in list:
        for char in line:
            if char == 'a':
                letters[0] += 1
            elif char == 'b':
                letters[1] += 1
            elif char == 'c':
                letters[2] += 1
            elif char == 'd':
                letters[3] += 1
            elif char == 'e':
                letters[4] += 1
            elif char == 'f':
                letters[5] += 1
            elif char == 'g':
                letters[6] += 1

    for n, value in enumerate(letters):
        if value > largest:
            largest = value
            index = n

    if index == 0:
        return 'a'
    elif index == 1:
        return 'b'
    elif index == 2:
        return 'c'
    elif index == 3:
        return 'd'
    elif index == 4:
        return 'e'
    elif index == 5:
        return 'f'
    elif index == 6:
        return 'g'
        
def decipher(input):
    top = ''
    topleft = ''
    topright = ''
    middle = ''
    botleft = ''
    bot = ''
    botright = ''

    numbers = [""] * 10

    # Get obvious numbers
    for value in input:
        if len(value) == 2:
            numbers[1] = value
        elif len(value) == 3:
            numbers[7] = value
        elif len(value) == 4:
            numbers[4] = value
        elif len(value) == 7:
            numbers[8] = value    
    
    # Get the top char (exist in 7 but not in 1)
    for char in numbers[7]:
        if char not in numbers[1]:
            top = char

    # Get the botright char (exist in all but 1)
    botright = mostCommon(input)

    # Only 2 misses botright char
    for value in input:
        if botright not in value:
            numbers[2] = value

    # 5 has three in common with 2, unlike anyone else
    for value in input:
        if value == numbers[2]:
            continue
        count = 0
        for letter in value:
            if letter in numbers[2]:
                count += 1
        if count == 3:
            numbers[5] = value

    # 3 has length of five (ignore picked strings)
    for value in input:
        if value in numbers:
            continue
        if len(value) == 5:
            numbers[3] = value
    
    # 6 is missing letter from 1 (ignore picked strings)
    for value in input:
        if value in numbers:
            continue
        for letter in numbers[1]:
            if letter not in value:
                numbers[6] = value

    # 0 does not includes all from 3 (ignore picked strings)
    for value in input:
        if value in numbers:
            continue
        count = 0
        for letter in numbers[3]:
            if letter not in value:
                numbers[0] = value

    # 9 is the only one left
    for value in input:
        if value not in numbers:
            numbers[9] = value


    return numbers

def findCorrectNumber(output, numberCodes):
    for n, code in enumerate(numberCodes):
        if len(code) != len(output):
            continue
        count = 0
        for letter in code:
            if letter in output:
                count += 1
        if count == len(code):
            return n

def part2(fileInput):
    with open(fileInput) as f:
        input = []
        output = []
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        for line in lines:
            inputoutput = line.split('|')
            inputoutput = [s.split(" ") for s in inputoutput]
            input.append(list(filter(None,inputoutput[0])))
            output.append(list(filter(None, inputoutput[1])))
        
        sum = 0
        for n,line in enumerate(input):
            outputString = ""
            numberCodes = decipher(line)
            for code in output[n]:
                outputString += str(findCorrectNumber(code,numberCodes))
            sum += int(outputString)
        
        print(sum)
        
    
        
        
        

#part1('Advent of Code 2021/Day8/testinput.txt')
#part1('Advent of Code 2021/Day8/input.txt')

#part2('Advent of Code 2021/Day8/testinput.txt')
part2('Advent of Code 2021/Day8/input.txt')