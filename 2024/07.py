from re import split
from icecream import ic
from aocd import get_data

def evaluateA(equation)->int:
    splitEquation = equation.split(':')
    toTest = int(splitEquation[0])
    numbers = [int(num) for num in splitEquation[1].split(' ')[1:]]
    if testEquationA(toTest, numbers):
        return toTest
    return 0

def testEquationA(toTest, numbers)->bool:
    dp = {numbers[0]}
    for num in numbers[1:]:
        next_dp = set()
        for value in dp:
            next_dp.add(value + num)
            next_dp.add(value * num)
        dp = next_dp  
    return toTest in dp

def evaluateB(equation)->int:
    splitEquation = equation.split(':')
    toTest = int(splitEquation[0])
    numbers = [int(num) for num in splitEquation[1].split(' ')[1:]]
    if testEquationB(toTest, numbers):
        return toTest
    return 0

def testEquationB(toTest, numbers)->bool:
    dp = {numbers[0]}
    for num in numbers[1:]:
        next_dp = set()
        for value in dp:
            next_dp.add(value + num)
            next_dp.add(value * num)
            next_dp.add(int(str(value) + str(num)))
        dp = next_dp  
    return toTest in dp

def solutionA(input):
    evaluatedTrue = [evaluateA(equation) for equation in input]
    ic(sum(evaluatedTrue))
    
def solutionB(input):
    evaluatedTrue = [evaluateB(equation) for equation in input]
    ic(sum(evaluatedTrue))
    
def main():
    input = get_data(day=7, year=2024).split('\n')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()