import sys

def applyRules(input, rules):
    result = ""
    for i in range(len(input)-1):
        toAppend = pair = input[i] + input[i+1]
        char = rules.get(pair)
        if char != None:
            if result == "":
                toAppend = input[i] + char + input[i+1]
            else:
                toAppend = char + input[i+1]
        result += toAppend
    return result
    

def findDiffHighLow(amount):
    lowestAmount = sys.maxsize
    highestAmount = 0
    for char, count in amount.items():
        if count > highestAmount:
            highestAmount = count
        if count < lowestAmount:
            lowestAmount = count
    return highestAmount-lowestAmount

def solve(input, iterations):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        input = lines[0]
       
        ruleLines = lines[2:]
        rules = {}

        for rule in ruleLines:
            temp = rule.split(" -> ")
            rules[temp[0]] = temp[1]
        
        for i in range(iterations):
            input = applyRules(input, rules)
        
        amount = {}
        for char in input:
            count = amount.get(char)
            if count == None:
                amount[char] = 1
            else:
                amount[char] += 1

        value = findDiffHighLow(amount)    
        print(value)

def part1(input):
    solve(input, 10)

def applyRules2(dict, rules, charCount):
    dictCopy = dict.copy() 
    for key, value in dictCopy.items():
        if rules.get(key) != None and value > 0:
            char = rules[key]
            dict[key] -= value
            
            element1 = key[0] + char
            element2 = char + key[1]
            
            addToCharCount(charCount, char, value)

            if dict.get(element1) == None:
                dict[element1] = value
            else:
                dict[element1] += value
            
            if dict.get(element2) == None:
                dict[element2] = value
            else:
                dict[element2] += value
    return dict

def addToCharCount(charCount, char, value = 1):
    if charCount.get(char) == None:
        charCount[char] = value
    else:
        charCount[char] += value

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        input = lines[0]
        dict = {}
        charCount = {}
        for i in range(len(input)-1):
            if i == 0:
                addToCharCount(charCount, input[i])
            addToCharCount(charCount, input[i+1])
            pair = input[i] + input[i+1]
            if dict.get(pair) == None:
                dict[pair] = 1
            else:
                dict[pair] += 1
       
        ruleLines = lines[2:]
        rules = {}

        for rule in ruleLines:
            temp = rule.split(" -> ")
            rules[temp[0]] = temp[1]
        
        for i in range(40):
            dict = applyRules2(dict, rules, charCount)
        
        value = findDiffHighLow(charCount)    
        print(value)


part1('Day14/input/input.txt')
part2('Day14/input/input.txt')