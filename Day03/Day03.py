

def part1(input):
    with open(input) as f:
        lines = f.readlines()
    list = [0] * (len(lines[0])-1)
    for line in lines:
        length = len(line)
        for i in range(0,length-1):
            if int(line[i]) == 1:
               list[i] += 1
            else:
               list[i] -= 1
    binaryStr = ""
    for j in list:
        if j >= 0:
            binaryStr += "1"
        else:
            binaryStr += "0"
    reverseBinaryStr = ""
    for k in binaryStr:
        if k == "0":
            reverseBinaryStr += "1"
        else:
            reverseBinaryStr += "0"
    print(int(binaryStr, 2) * int(reverseBinaryStr, 2))
    

def reduceList(list, index, mostCommon):
    ones = []
    zeros = []
    if len(list) <= 1:
        return list
    
    for line in list:
        if int(line[index]) == 0:
            zeros.append(line)
        else:
            ones.append(line)
    if len(zeros) == len(ones):
        if mostCommon == True:
            return ones
        else:
            return zeros
    elif len(zeros) > len(ones):
        if mostCommon == True:
            return zeros
        else:
            return ones
    elif len(zeros) < len(ones):
        if mostCommon == True:
            return ones
        else:
            return zeros


def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
    index = 0
    length = len(lines[0])
    oxyGenRating = lines
    while index < length:
        oxyGenRating = reduceList(oxyGenRating, index, True)
        index += 1

    index = 0
    coScrubRating = lines
    while index < length:
        coScrubRating = reduceList(coScrubRating, index, False)
        index += 1
                
    print(int(oxyGenRating[0],2)*int(coScrubRating[0],2))

    


part1('Day03/input/input.txt')
part2('Day03/input/input.txt')