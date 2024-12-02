from collections import Counter
from icecream import ic
from aocd import get_data

def solutionA(listA, listB):
    listA.sort()
    listB.sort()
    dist = [abs(x - y) for x,y in zip(listA,listB)]
    ic(sum(dist))

def solutionB(listA, listB):
    occurances = Counter(listB)
    similarity = [x * occurances[x] for x in listA if x in occurances]
    ic(sum(similarity))
    
def main():
    input = get_data(day=1, year=2024).split('\n')
    listA = [int(line.split(" ")[0]) for line in input]
    listB = [int(line.split(" ")[-1]) for line in input]
    solutionA(listA, listB)
    solutionB(listA, listB)

if __name__ == '__main__':
    main()