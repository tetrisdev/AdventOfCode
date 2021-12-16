import numpy as np
from numpy.core.numeric import zeros_like

def arrayAround(location:tuple,array:np.array) -> np.array:
    arr = zeros_like(array)
    x,y = location
    offsets = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(0,0)]
    for offset in offsets:
      ox,oy = offset
      if x + ox in range(len(arr[0])) and y + oy in range(len(arr)):  
        arr[x+ox, y+oy] = 1
    return arr

def solutionA(input):
    steps = 100
    input = [[int(x) for x in list(line)] for line in input]
    array = np.array(input)
    flashes = 0
    for i in range(steps):
        array += 1
        flashLocations = np.where(array == 10)
        flashLocations = list(zip(flashLocations[0],flashLocations[1]))
        while len(flashLocations) > 0:
            location = flashLocations.pop()
            array += arrayAround(location,array)
            flashes += 1
            flashLocationsNew = np.where(array == 10)
            flashLocations += list(filter(lambda x: x not in flashLocations,list(zip(flashLocationsNew[0],flashLocationsNew[1]))))
        array[array > 9] = 0
    print(flashes)
def solutionB(input):
    steps = 0
    input = [[int(x) for x in list(line)] for line in input]
    arrayOct = np.array(input)
    while(not np.all(arrayOct == 0)):
        arrayOct += 1
        flashLocations = np.where(arrayOct == 10)
        flashLocations = list(zip(flashLocations[0],flashLocations[1]))
        while len(flashLocations) > 0:
            location = flashLocations.pop()
            arrayOct += arrayAround(location,arrayOct)
            flashLocationsNew = np.where(arrayOct == 10)
            flashLocations += list(filter(lambda x: x not in flashLocations,list(zip(flashLocationsNew[0],flashLocationsNew[1]))))
        arrayOct[arrayOct > 9] = 0
        steps += 1
    print(steps)
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines =  [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('input11')
    #input = ['5483143223','2745854711','5264556173','6141336146','6357385478','4167524645','2176841721','6882881134','4846848554','5283751526']
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()