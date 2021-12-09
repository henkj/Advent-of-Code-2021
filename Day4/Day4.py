class Board:
    
    def __init__(self, values):
        self.values = values
        self.foundNumbers = []
        self.foundNumbers.append([0]*5)
        self.foundNumbers.append([0]*5)
        self.foundNumbers.append([0]*5)
        self.foundNumbers.append([0]*5)
        self.foundNumbers.append([0]*5)
        self.lastNumber = -1

    def addInput(self, number):
        self.lastNumber = int(number)
        for i in range(0,5):
            for j in range(0,5):
                if self.values[i][j] == number:
                    self.foundNumbers[i][j] = 1

    def checkForBingo(self):
        def checkRow(nums):
            if nums[0] == 1 and nums[0] == nums[1] and nums[1] == nums[2] and nums[2] == nums[3] and nums[3] == nums[4]:
                return True
            return False

        for i in range(0,5):
            if checkRow(self.foundNumbers[i]):
                return True

            if checkRow([row[i] for row in self.foundNumbers]):
                return True
        return False

    def calcScore(self):
        sum = 0
        for i in range(0,5):
            for j in range(0,5):
                if self.foundNumbers[i][j] == 0:
                    sum += int(self.values[i][j])
        return sum*self.lastNumber

        
    
def createBoard(lines):
    list = []
    for line in lines[0:5]:
            innerList = []
            for num in line.split(' '):
                if num != ' ' and num != '':
                    innerList.append(num)
            list.append(innerList)
    return Board(list)

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        bingoInput = lines[0]
        lines = lines[2:]
        boards = []
        while len(lines) >= 5:
            boards.append(createBoard(lines[0:5]))
            lines = lines[6:]
        bingoInput = bingoInput.split(',')
        for number in bingoInput:
            for board in boards:
                board.addInput(number)
                bingo = board.checkForBingo()
                if bingo:
                    print(board.calcScore())
                    return

def findLosingBoard(boards, number):
    losingBoards = []
    for board in boards:
        board.addInput(number)
        bingo = board.checkForBingo()
        if not bingo:
            losingBoards.append(board)
    return losingBoards


def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        bingoInput = lines[0]
        lines = lines[2:]
        boards = []
        while len(lines) >= 5:
            boards.append(createBoard(lines[0:5]))
            lines = lines[6:]
        bingoInput = bingoInput.split(',')
    
        for number in bingoInput:
            if len(boards) > 1:
                boards = findLosingBoard(boards,number)
            else:
                boards[0].addInput(number)
                bingo = boards[0].checkForBingo()
                if bingo:
                    print(boards[0].calcScore())
                    return
            
        
    


#part1('Advent of Code 2021/Day4/testinput.txt')
part1('Advent of Code 2021/Day4/input.txt')

#part2('Advent of Code 2021/Day4/testinput.txt')
part2('Advent of Code 2021/Day4/input.txt')