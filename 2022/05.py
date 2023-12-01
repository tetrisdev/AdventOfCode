
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [x.strip('\n') for x in lines]
    return lines

def main():
    input = parseInput('input01')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()