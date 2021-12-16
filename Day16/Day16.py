import sys

def processPackage(n, binary):
    versionSum = 0
    version = binary[n:n+3]
    intVersion = int(version, 2)
    type = binary[n+3:n+6]
    
    if int(type, 2) == 4:
        i = n+6
        while binary[i] == '1':
            i += 5
        n = i + 5
    else:
        n += 6
        if binary[n] == '0':
            length = 15
        else:
            length = 11
        lengthOfSubPackages = int(binary[n+1:n+1+length], 2)
        n += length + 1
        endOfSubPackages = n + lengthOfSubPackages
        while n < endOfSubPackages:
            packVersion, n = processPackage(n, binary)
            versionSum += packVersion
    return intVersion + versionSum, n

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        hex = lines[0]
        binary = bin(int(hex,16))[2:].zfill(len(hex)*4)

        # binary = binary[2:]
        n = 0
        addedVersions = 0
        while n < len(binary)-8:
            versionSum, n = processPackage(n, binary)
        print(versionSum)


def processPackage2(n, binary):
    values = []
    version = binary[n:n+3]
    type = binary[n+3:n+6]
    typeInt = int(type, 2)
    sum = 0
    product = 1
    if typeInt == 4:
        i = n+6
        binString = ""
        while binary[i] == '1':
            binString += binary[i+1:i+5]
            i += 5
        binString += binary[i+1:i+5]    
        n = i + 5
        return int(binString, 2), n
    else:
        n += 6
        if binary[n] == '0':
            length = 15
        else:
            length = 11
        lengthOfSubPackages = int(binary[n+1:n+1+length], 2)
        n += length + 1
        if length == 15:
            endOfSubPackages = n + lengthOfSubPackages
            while n < endOfSubPackages:
                value, n = processPackage2(n, binary)
                values.append(value)
                sum += value
                product *= value
        else:
            for i in range(lengthOfSubPackages):
                value, n = processPackage2(n, binary)
                values.append(value)
                sum += value
                product *= value
        if typeInt == 0:
            return sum, n
        elif typeInt == 1:
            return product, n
        elif typeInt == 2:
            values.sort()
            return values[0], n
        elif typeInt == 3:
            values.sort()
            return values[-1], n
        elif typeInt == 5: 
            if values[0] > values[1]:
                return 1, n
            else:
                return 0, n
        elif typeInt == 6:
            if values[0] < values[1]:
                return 1, n
            else:
                return 0, n
        elif typeInt == 7:
            if values[0] == values[1]:
                return 1, n
            else:
                return 0, n
        

    return value, n

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        
        hex = lines[0]
        binary = bin(int(hex,16))[2:].zfill(len(hex)*4)

        # binary = binary[2:]
        n = 0
        addedVersions = 0
        while n < len(binary)-8:
            value, n = processPackage2(n, binary)
        print(value)


part1('Day16/input/input.txt')
part2('Day16/input/input.txt')