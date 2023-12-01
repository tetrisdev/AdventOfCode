import re

def digitreplace(matchobj):
    if matchobj.group(1) == 'one': return '1'
    elif matchobj.group(1) == 'two': return '2'
    elif matchobj.group(1) == 'three': return '3'
    elif matchobj.group(1) == 'four': return '4'
    elif matchobj.group(1) == 'five': return '5'
    elif matchobj.group(1) == 'six': return '6'
    elif matchobj.group(1) == 'seven': return '7'
    elif matchobj.group(1) == 'eight': return '8'
    elif matchobj.group(1) == 'nine': return '9'


def solutionB(input):
    textasDigits = [re.sub('(?=(one|two|three|four|five|six|seven|eight|nine))',digitreplace,line) for line in input]
    #print(textasDigits)
    solutionA(textasDigits)

def solutionA(input):
    no_chars = [re.sub('\D*','',line) for line in input]
    digits = [int(f'{line[0]}{line[-1]}') for line in no_chars]
    #print(digits)
    print(sum(digits))

def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('2023\input01.txt')
    #input = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
    #input = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()