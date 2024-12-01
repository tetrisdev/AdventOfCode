from icecream import ic
import re
import math
def solveEQ(a,b,c):
    x1 = (-b + math.sqrt(pow(b,2)-4*a*c))/2*a
    x2 = (-b - math.sqrt(pow(b,2)-4*a*c))/2*a
    x1 = math.ceil(abs(x1))
    x2 = math.floor(abs(x2))
    return (x1,x2)

def solveRace(race):
    # x = -y^2 + jy (y time held, j sek left) -> solve for y
    a,b,c = 1 , race[0],race[1]
    solution = solveEQ(a,b,c+1)
    return (solution[1]+1) - solution[0]

def solutionB(input):
    time = int(''.join(re.findall('\d+',input[0])))
    distance = int(''.join(re.findall('\d+',input[1])))
    solutionB = solveRace((time,distance))
    ic(solutionB)
    
def solutionA(input):
    times = list(map(int,re.findall('\d+', input[0])))
    distances = list(map(int,re.findall('\d+', input[1])))
    solutionsA = list(map(solveRace,zip(times,distances)))
    ic(math.prod(solutionsA))

def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('2023/input06.txt')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()