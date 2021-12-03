from collections import Counter

def solutionA(input):
    bits = []
    for index,str in enumerate(input[0]):
        bits.append((mostCommon(input,index),leastCommon(input,index)))
    gamma = int(''.join([x[0] for x in bits]),2)
    epsilon = int(''.join([x[1] for x in bits]),2)
    print(gamma * epsilon)
    
def solutionB(input):
    oxygen = input
    co2 = input
    for index,str in enumerate(input[0]):
        oxygen = list(filter(lambda x: x[index] == mostCommon(oxygen,index),oxygen))
        co2 = list(filter(lambda x: x[index] == leastCommon(co2,index),co2))
    print(int(oxygen[0],2) * int(co2[0],2))

def mostCommon(input,index):
    bits = [x[index] for x in input]
    return Counter(bits).most_common(1)[0][0]

def leastCommon(input,index):
    bits = [x[index] for x in input]
    return Counter(bits).most_common()[-1][0]
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input03')
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()