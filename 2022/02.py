def solveA(line):
    line = line.strip('\n')
    chars = line.split(' ')
    chars = list(map(ord,chars))
    chars[0] = chars[0] + 23
    chars = list(map(lambda x: (x%7)-3,chars))
    winner = abs(chars[1]-chars[0])
    if winner == 0:
        chars[0] = 3
    elif winner == 1:
        if chars[0] > chars[1]:
            chars[0] = 0
        else: 
            chars[0] = 6
    else:
        if chars[0] < chars[1]:
            chars[0] = 0
        else:
            chars[0] = 6
    return sum(chars)

def solveB(line):
    line = line.strip('\n')
    chars = line.split(' ')
    chars = list(map(ord,chars))
    chars[0] = ((chars[0] + 23) % 7) - 3       
    chars[1] = (chars[1] % 4) * 3
    if chars[1] == 6:
        chars[0] = (chars[0] + 1) % 3
    elif chars[1] == 0:
        chars[0] = (chars[0] + 2) % 3
    if chars[0] == 0:
        chars[0] = 3 
    return sum(chars)

def solutionA(input):
    sol = sum(map(solveA,input))
    print(sol)

def solutionB(input):
    sol = sum(map(solveB,input))
    print(sol)
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input02')
    #input = ["A X","A Y","A Z","B X","B Y","B Z","C X","C Y","C Z"]
    #input = ["B Z"]
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()