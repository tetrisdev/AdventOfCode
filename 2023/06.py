from icecream import ic
import re

def solutionB(input):
    ic()

def solutionA(input):
    ic()

def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('input01')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()