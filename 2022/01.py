def genList(input) -> list:
    q = []
    calories = 0
    for line in input:
        line = line.strip('\n')
        if line != "" :
            calories += int(line)
        else:
            q.append(calories) 
            calories = 0
    q.sort(reverse=True)
    return q

def solutionA(input):
    l = genList(input)
    print(l[0])
    
def solutionB(input):
    l = genList(input)
    print(l[0] + l[1] + l[2])
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input01')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()