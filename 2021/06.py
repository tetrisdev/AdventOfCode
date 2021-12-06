def simulate(input,days) -> int:
    fish = [0]*9
    input = [int(x) for x in input[0].split(',')]
    for f in input:
        fish[f] += 1
    for i in range(days):
        fish.append(fish.pop(0))
        fish[6] += fish[8]
    return sum(fish)
def solutionA(input):
    print(simulate(input,80))

def solutionB(input):
    print(simulate(input,256))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input06')
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()