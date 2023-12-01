import re

def digitreplace(matchobj):
    numdict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    return numdict[matchobj.group(1)]

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