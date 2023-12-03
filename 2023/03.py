from icecream import ic
import re

def parseEngineSchematic(schematic):
    width = len(schematic[0])+1
    numbers = {matchObj.span():matchObj.group(0) for matchObj in re.finditer(r'\d+','.'.join(schematic)+'.')}
    symbols = {matchObj.span():matchObj.group(0) for matchObj in re.finditer(r'[^\.\d]','.'.join(schematic)+'.')}
    return width,numbers,symbols
    
def solutionB(input):
    width,numbers,symbols = parseEngineSchematic(input)
    gearratios = list()
    for symbol in symbols:
        if symbols[symbol] == '*':
            positions = [symbol[1],symbol[0]-width,symbol[0]+width,symbol[1]+width,symbol[1]-width,symbol[0]-1,symbol[0]-width-1,symbol[0]+width-1]
            nums = {int(numbers[num]) for num in numbers for pos in positions if num[0] <= pos < num[1]}
            if(len(nums) == 2):
                gearratios.append(nums.pop()*nums.pop())
    print(sum(gearratios))
    
def solutionA(input):
    width,numbers,symbols = parseEngineSchematic(input)
    engineParts = [int(numbers[num]) for num in numbers for symbol in symbols if num[0]-width-1 <= symbol[0] <= num[1]-width or num[0]-1 <= symbol[0] <= num[1] or num[0]+width-1 <= symbol[0] <= num[1]+width]
    print(sum(engineParts))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput(r'2023\input03.txt')
    #input = ['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.','...$.*....','.664.598..']
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()