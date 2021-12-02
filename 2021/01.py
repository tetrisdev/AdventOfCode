from itertools import *

def solutionA(input):
    print("A: %s" % len(list(filter(lambda x: x,[x < y for x,y in pairwise(input)]))))

def solutionB(input):
    nums = list(zip(input,input[1:],input[2:]))
    nums = [sum(x) for x in nums]
    print("B: %s" % len(list(filter(lambda x: x,[x < y for x,y in pairwise(nums)]))))

def parseInput(filepath: str):
    with open(filepath) as file:
        lines = [int(x) for x in file.readlines()]
    return lines

def main():
    input = parseInput('input01')
    solutionA(input)
    solutionB(input)
    
if __name__ == '__main__':
    main()