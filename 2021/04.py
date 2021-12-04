from dataclasses import dataclass

@dataclass
class BingoBoard:
    id: int
    board: list
    size: int
    won: bool = False

    def win(self) -> bool:
        row = [0] * self.size
        col = [0] * self.size
        for counter, n in enumerate(self.board):
            if n[1] == True:
                row[int(counter/self.size)] += 1
                col[counter%self.size] += 1
        self.won = max(row) == self.size or max(col) == self.size
        return self.won
    
    def mark(self, num:int):
        if num not in [x[0] for x in self.board]:
            return
        self.board = [(k,v) if (k != num) else (k,True) for k,v in self.board]            

    def score(self) -> int:
        return sum([x[0] for x in self.board if x[1] == False])

def generateBoards(input) -> list:
    input = input[2:]
    counterID = 0
    boards = []
    board = []
    for l in input:
        if l == '\n':
            boards.append(BingoBoard(counterID,board,5))
            board = []
            counterID += 1
        else:
            board += [(int(x),False) for x in [l[i:i+2] for i in range(0,len(l),3)]]
    return boards

def runBingo(nums, boards) -> list:
    winners = []
    for i in nums:
        for b in boards:
            b.mark(i)
            if b.win():
                winners.append(b.score() * i)
                boards = list(filter(lambda x : not x.won ,boards))
    return winners

def solutionA(input):
    nums = [int(x) for x in input[0].split(',')]
    boards = generateBoards(input)
    print(runBingo(nums,boards)[0])

def solutionB(input):
    nums = [int(x) for x in input[0].split(',')]
    boards = generateBoards(input)
    print(runBingo(nums,boards)[-1])
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input04')
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()