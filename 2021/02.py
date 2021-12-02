def solutionA(input):
    commands = [(x,int(y)) for x,y in [x.split(" ") for x in input]]
    depth = 0
    horizont = 0
    for command in commands:
        match command[0]:
            case "forward":
                horizont += command[1]
            case "down":
                depth += command[1]
            case "up":
                depth -= command[1]
    print(depth * horizont)
    
def solutionB(input):
    commands = [(x,int(y)) for x,y in [x.split(" ") for x in input]]
    depth = 0
    horizont = 0
    aim = 0
    for command in commands:
        match command[0]:
            case "forward":
                horizont += command[1]
                depth += aim * command[1]
            case "down":
                aim += command[1]
            case "up":
                aim -= command[1]
    print(depth * horizont)
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input02')
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()