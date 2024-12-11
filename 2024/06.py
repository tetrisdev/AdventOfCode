from icecream import ic
from aocd import get_data
import re

directions = {"^": (-1, 0,'>'), "v": (1, 0,'<'), ">": (0, 1,'v'), "<": (0, -1,'^')}

def findGuard(input):
    for x, line in enumerate(input):
        match = re.search(r'([v^<>])', line)
        if match:
            return (x,match.start())
    return (-1,-1)        

def findLoop(maze,traveledPath) -> bool:
    x,y = traveledPath[-1][:2]
    loopPath = traveledPath.copy()
    while 0 <= x < len(maze) and 0 <= y < len(maze[x]):
        currentGuard = maze[x][y]
        guardTuple = directions[currentGuard]
        futureX = x + guardTuple[0]
        futureY = y + guardTuple[1]
        if futureX < 0 or futureX >= len(maze) or futureY < 0 or futureY >= len(maze[futureX]):
            return False
        if maze[futureX][futureY] == "#":
            maze[x][y] = guardTuple[2]
            continue
        maze[futureX][futureY] = currentGuard
        maze[x][y] = "X"
        updatePath = (x,y,currentGuard)
        if updatePath in loopPath:
            return True
        else:
            loopPath.append((x,y,currentGuard))
        x,y = futureX,futureY
    return False

def solutionA(input):
    x,y = findGuard(input)
    input = [list(line) for line in input]
    traveledPath = []
    while 0 <= x < len(input) and 0 <= y < len(input[x]):
        currentGuard = input[x][y]
        guardTuple = directions[currentGuard]
        futureX = x + guardTuple[0]
        futureY = y + guardTuple[1]
        if futureX < 0 or futureX >= len(input) or futureY < 0 or futureY >= len(input[futureX]):
            input[x][y] = "X"
            break
        if input[futureX][futureY] == "#":
            input[x][y] = guardTuple[2]
            continue
        input[futureX][futureY] = currentGuard
        input[x][y] = "X"
        traveledPath.append((x,y,currentGuard))
        x,y = futureX,futureY
    path = [1 for line in input for char in line if char == "X"]
    ic(sum(path))
    return traveledPath
    
def solutionB(traveledPath,input):
    origx,origy = findGuard(input)
    input = [list(line) for line in input]
    number_of_loops = 0
    traveledCoords = [pos[:2] for pos in traveledPath]
    for i,pos in enumerate(traveledPath):
        #ic(i,len(traveledPath))
        alteredMaze = input.copy()
        alteredMaze[origx][origy] = "."
        x,y,guard = pos
        alteredMaze[x][y] = directions[guard][2]
        posObsX = x + directions[guard][0]
        posObsY = y + directions[guard][1]
        alteredMaze[posObsX][posObsY] = "#"
        if (posObsX,posObsY) != (origx,origy) and (posObsX,posObsY) not in traveledCoords[:i+1] and findLoop(alteredMaze,traveledPath[:i+1]):
            number_of_loops += 1
            ic(number_of_loops)
    ic(number_of_loops)
def main():
    input = get_data(day=6, year=2024).split('\n')
    #input = ["....#.....",
    #         ".........#",
    #         "..........",
    #         "..#.......",
    #         ".......#..",
    #         "..........",
    #         ".#..^.....",
    #         "........#.",
    #         "#.........",
    #         "......#..."]
    traveledPath =solutionA(input)
    solutionB(traveledPath, input)

if __name__ == '__main__':
    main()