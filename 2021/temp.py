def solutionA(input):
    print("")
    
def solutionB(input):
    print("")
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput()
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()