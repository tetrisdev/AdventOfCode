from collections import Counter
from icecream import ic
from aocd import get_data

def solutionA(levels):
    safe = [all(i < 0 and abs(i) <= 3 for i in array) or all(i > 0 and abs(i) <= 3 for i in array) for array in levels]
    #ic(safe,levels)
    return safe  
    
def solutionB(levels):
    subsets = [[level[:i] + level[i+1:] for i in range(len(level))] for level in levels]
    differences = [[[y-x for x,y in zip(array[0:-1],array[1:])]for array in level] for level in subsets]
    safe = [any(solutionA(array)) for array in differences]
    ic(sum(safe))

def main():
    input = get_data(day=2, year=2024).split('\n')
    input = [line.split(" ") for line in input]
    input = [[int(x) for x in line] for line in input]
    levels = [[y-x for x,y in zip(array[0:-1],array[1:])] for array in input]
    ic(sum(solutionA(levels)))
    solutionB(input)


if __name__ == '__main__':
    main()