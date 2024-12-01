from collections import Counter
from icecream import ic

def solutionA(listA, listB):
    listA.sort()
    listB.sort()
    dist = [abs(x - y) for x,y in zip(listA,listB) ]
    ic(sum(dist))

def solutionB(listA, listB):
    # reduce the list by counting the number of times a number appears
    occurances = Counter(listB)
    similarity = [x * occurances[x] for x in listA if x in occurances]
    ic(sum(similarity))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('2024\\input01.txt')
    listA = [int(line.split(" ")[0]) for line in input]
    listB = [int(line.split(" ")[-1]) for line in input]
    solutionA(listA, listB)
    solutionB(listA, listB)

if __name__ == '__main__':
    main()