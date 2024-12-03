from icecream import ic
from aocd import get_data
import re

def solutionA(input):
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)',input)
    nums = [re.findall(r'\d+',instruction) for instruction in matches]
    mul = [int(x[0])*int(x[1]) for x in nums]
    ic(sum(mul))
    
def solutionB(input):
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))",input)
    sum = 0
    enabled = True
    for instruction in matches:
        if len(instruction[0]) > 0 and enabled:
            nums = re.findall(r'\d+',instruction[0])
            sum += int(nums[0])*int(nums[1])
        if len(instruction[1]) > 0:
            enabled = True
        if len(instruction[2]) > 0:
            enabled = False
    ic(sum)
    
def main():
    input = get_data()#.split('\n')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()