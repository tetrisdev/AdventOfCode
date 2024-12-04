from icecream import ic
from aocd import get_data

directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
# Searches for the Letters starting from the given position in a direction and returns them, recursively
def findLetters(depth, direction, x, y, input):
    if x < 0 or x >= len(input) or y < 0 or y >= len(input[x]):
        return ""
    if depth == 3:
        return input[x][y]
    depth += 1
    return input[x][y] + findLetters(depth, direction, x + direction[0], y + direction[1], input)

def solutionA(input):
    words = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            char = input[x][y]
            if char == 'X':
                for direction in directions:
                    words.append(findLetters(depth = 0, direction = direction, x = x, y = y, input = input))
    words = [1 for word in words if word == "XMAS"]
    ic(sum(words))
    
def solutionB(input):
    xmasCount = 0
    for x in range(len(input)):
        for y in range(len(input[x])):
            char = input[x][y]
            if char == 'A':
                xmasCount += validXMAS(x,y,input)
    ic(xmasCount)

def validXMAS(x, y, input) -> bool:
    #Check for boundaries and X's and A's
    for direction in directions[4:]:
        if x + direction[0] < 0 or x + direction[0] >= len(input) or y + direction[1] < 0 or y + direction[1] >= len(input[x]):
            return False
        if input[x + direction[0]][y + direction[1]] == 'X':
            return False
        if input[x + direction[0]][y + direction[1]] == 'A':
            return False
    # Opposite diagonals always need to be either 'M' or 'S' but not both at the same time
    if input[x + directions[4][0]][y + directions[4][1]] == 'M' and input[x + directions[-1][0]][y + directions[-1][1]] == 'M':
        return False
    if input[x + directions[5][0]][y + directions[5][1]] == 'M' and input[x + directions[6][0]][y + directions[6][1]] == 'M':
        return False   
    if input[x + directions[4][0]][y + directions[4][1]] == 'S' and input[x + directions[-1][0]][y + directions[-1][1]] == 'S':
        return False
    if input[x + directions[5][0]][y + directions[5][1]] == 'S' and input[x + directions[6][0]][y + directions[6][1]] == 'S':
        return False           
    return True
    
def main():
    input = get_data().split('\n')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()