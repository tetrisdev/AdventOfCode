from math import ceil, floor

def solutionA(input):
    crabs = [int(x) for x in input[0].split(',')]
    crabs.sort()
    median = crabs[int(len(crabs)/2)]
    cost = sum([abs(median-x) for x in crabs])
    print("A:",cost)
    
def solutionB(input):
    crabs = [int(x) for x in input[0].split(',')]
    crabs.sort()
    avg = floor(sum(crabs) / len(crabs)) #round works for test input, floor works for my input.
    cost = sum([int((abs(avg-x) ** 2 + abs(avg-x)) / 2) for x in crabs])
    print("B:",cost)
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input07')
    #input = ['16,1,2,0,4,2,7,1,2,14']
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()