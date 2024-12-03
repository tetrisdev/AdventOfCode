from collections import Counter
from icecream import ic
from aocd import get_data

def solutionA(levels):
    allPos = [all(i > 0 for i in array) for array in levels]
    allNeg = [all(i < 0 for i in array) for array in levels]
    otherCriteria = [all(i != 0 and abs(i) <=3 for i in array) for array in levels]
    #ic(levels,allPos,allNeg,otherCriteria)
    safe = [(neg == True and other == True) ^ (pos == True and other == True) for pos,neg,other in zip(allPos, allNeg, otherCriteria)]
    ic(sum(safe))
    
def solutionB(levels):
    safe = [checkSafety(array) for array in levels]
    ic(safe)

def checkSafety(level):
    errorCounter = 0
    for x,y in zip(level[0:-1],level[1:]):
        if (x > 0 and y < 0) or (x < 0 and y > 0):
            errorCounter += 1
        if abs(x) > 3 and abs(y) > 1:
            errorCounter += 1
    for x in level:
        if abs(x) > 3:
            errorCounter += 1
    errorCounter += Counter(level)[0]
    return errorCounter <= 1

def main():
    input = get_data(day=2, year=2024).split('\n')
    input =  ["7 6 4 2 1",
                "1 2 7 8 9",
                "9 7 6 2 1",
                "1 3 2 4 5",
                "8 6 4 4 1",
                "1 3 6 7 9"]
    input = [line.split(" ") for line in input]
    input = [[int(x) for x in line] for line in input]
    levels = [[y-x for x,y in zip(array[0:-1],array[1:])] for array in input]
    solutionA(levels)
    solutionB(levels)

if __name__ == '__main__':
    main()