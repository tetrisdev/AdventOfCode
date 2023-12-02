valid = {'red':12,'green':13,'blue':14}

def validate(game):
    pulls_validated = [int(cubes.split(' ')[1]) <= valid[cubes.split(' ')[2]] for pull in game for cubes in pull.split(',')]
    return not False in pulls_validated

def getPower(game):
    pullsdictList = [{cube.split(' ')[2]:cube.split(' ')[1] for cube in pull.split(',')}for pull in game]
    r = max([int(pull['red']) if 'red' in pull else 0 for pull in pullsdictList])
    g = max([int(pull['green']) if 'green' in pull else 0 for pull in pullsdictList])
    b = max([int(pull['blue']) if 'blue' in pull else 0 for pull in pullsdictList])
    return r*g*b

def solutionB(input):
    games = [line.split(':')[1].split(';') for line in input]
    powers = list(map(getPower,games))
    print(sum(powers))
    
def solutionA(input):
    games = [line.split(':')[1].split(';') for line in input]
    validated = list(map(validate,games))
    validGameIDs = [i+1 for i in range(len(validated)) if validated[i] == True]
    print(sum(validGameIDs))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('2023\input02.txt')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()