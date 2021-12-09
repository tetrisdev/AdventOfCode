from functools import reduce

def generateArray(input):
    array = []
    for l in input:
        array.append([[int(x),False] for x in list(filter(lambda x: x != '\n',[l[i:i+1] for i in range(0, len(l),1)]))])
    return array

def findLowPoints(arr) -> list:
    points = []
    for i,nums in enumerate(arr):
        for j,x in enumerate(nums):
            low = True
            if j > 0 and low:
                low = x[0] < nums[j-1][0]
            if j < len(nums)-1 and low:
                low = x[0] < nums[j+1][0]
            if i > 0 and low:
                low = x[0] < arr[i-1][j][0]
            if i < len(arr)-1 and low:
                low = x[0] < arr[i+1][j][0]
            if low:
                points.append((x[0],i,j))
    return points

def calcBasin(arr,x) -> int:
    around = []
    num,i,j = x
    arr[i][j][1] = True
    if j > 0:
        comp = arr[i][j-1][0]
        if num < comp and comp != 9 and not arr[i][j-1][1]:
            around.append((comp,i,j-1))
            arr[i][j-1][1] = True
    if j < len(arr[i])-1:
        comp = arr[i][j+1][0]
        if num < comp and comp != 9 and not arr[i][j+1][1]:
            around.append((comp,i,j+1))
            arr[i][j+1][1] = True
    if i > 0:
        comp = arr[i-1][j][0]
        if num < comp and comp != 9 and not arr[i-1][j][1]:
            around.append((comp,i-1,j))
            arr[i-1][j][1] = True
    if i < len(arr)-1:
        comp = arr[i+1][j][0]
        if num < comp and comp != 9 and not arr[i+1][j][1]:
            around.append((comp,i+1,j))
            arr[i+1][j][1] = True
    sum = 0
    for i in around:
        sum += calcBasin(arr,i)
    return sum + 1

def solutionA(input):
    arr = generateArray(input)
    risk = [x[0]+1 for x in findLowPoints(arr)]
    print(sum(risk))
    
def solutionB(input):
    arr = generateArray(input)
    points = findLowPoints(arr)
    scores = list(map(lambda x: calcBasin(arr,x),points))
    scores.sort(reverse=True)
    score = reduce(lambda x,y: x*y,scores[:3])
    print(score)
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input09')
    #input = ['2199943210','3987894921','9856789892','8767896789','9899965678']
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()