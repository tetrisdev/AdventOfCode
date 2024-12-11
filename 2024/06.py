from collections import Counter
from icecream import ic
from aocd import get_data
import re

directions = {"^": (-1, 0,'>'), "v": (1, 0,'<'), ">": (0, 1,'v'), "<": (0, -1,'^')}
missingObstacleAddition = {'^': (1, -1), 'v': (-1, 1), '>': (1, 1), '<': (-1, -1)}

def findGuard(input):
    for x, line in enumerate(input):
        match = re.search(r'([v^<>])', line)
        if match:
            return (x,match.start())
    return (-1,-1)        

def findCorner(obstacleA, obstacleB, obstacleC):
    encounteredDirections = [obstacleA[2], obstacleB[2], obstacleC[2]]
    missingDir = list(set(directions.keys()) - set(encounteredDirections))
    x = obstacleC[0] + missingObstacleAddition[missingDir[0]][0]
    y = obstacleA[1] + missingObstacleAddition[missingDir[0]][1]
    return (x,y)
    
def solutionA(input):
    x,y = findGuard(input)
    input = [list(line) for line in input]
    encounteredObstacles = []
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
            encounteredObstacles.append((futureX,futureY,currentGuard))
            continue
        input[futureX][futureY] = currentGuard
        input[x][y] = "X"
        traveledPath.append((x,y,currentGuard))
        x,y = futureX,futureY
    path = [1 for line in input for char in line if char == "X"]
    ic(sum(path))
    return encounteredObstacles, traveledPath
    
def solutionB(encounteredObstacles, traveledPath, input):
    origx,origy = findGuard(input)
    possibleInsertions = []
    # go through encounteredObstacles with window of 3 and make squares with all the viable options. This should find most insertable obstacles. Still missing: Obstacles that change the path to encounter one before that.
    for obstacleA, obstacleB, obstacleC in zip(encounteredObstacles[:-2], encounteredObstacles[1:-1], encounteredObstacles[2:]):
        insertedX, insertedY = findCorner(obstacleA, obstacleB, obstacleC)
        if insertedX == origx or insertedY == origy or input[insertedX][insertedY] == "#":
            continue
        possibleInsertions.append((insertedX,insertedY))
    
    pathCoords = [(x,y)  for x,y,_ in traveledPath]
    counts = Counter(pathCoords)
    intersections = [(x,y,_) for x,y,_ in traveledPath if counts[(x,y)] > 1]
    ic(intersections)
    ic(set(possibleInsertions))
    
def main():
    input = get_data(day=6, year=2024).split('\n')
    input = ["....#.....",
             ".........#",
             "..........",
             "..#.......",
             ".......#..",
             "..........",
             ".#..^.....",
             "........#.",
             "#.........",
             "......#..."]
    encounteredObstacles, traveledPath = solutionA(input)
    solutionB(encounteredObstacles,traveledPath, input)

if __name__ == '__main__':
    main()