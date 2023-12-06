from itertools import chain, filterfalse, pairwise
from icecream import ic
import re
import time

def adjustOldMappings(newMappings, oldMaps):
    newMappingsAdjusted = list()
    for newMapping in newMappings:
        if len(oldMaps) == 0:
            newMappingsAdjusted.append(newMapping)
            continue
        newStart, newEnd = newMapping[0]
        adjusted = False
        for oldMapping in oldMaps:
            oldStart, oldEnd = oldMapping[0]
            #Adjust Old Mappings with new Values if range is somewhere in there
            if oldMapping[0][0] + oldMapping[1] <= newMapping[0][0] and oldMapping[0][1] + oldMapping[1] >= newMapping[0][1]:
                oldMappingPL = ((oldMapping[0][0],newMapping[0][0]-oldMapping[1]),oldMapping[1], 'MidLeft')
                oldMappingMid = ((newMapping[0][0]-oldMapping[1],newMapping[0][1]-oldMapping[1]),oldMapping[1] + newMapping[1],'Mid')
                oldMappingPR = ((newMapping[0][1]-oldMapping[1],oldMapping[0][1]),oldMapping[1], 'MidRight')
                temp = [oldMappingPL,oldMappingMid,oldMappingPR]
                for mapping in temp:
                    if not mapping[0][0] + 1 >= mapping[0][1]:
                        newMappingsAdjusted.append(mapping)
            elif newMapping[0][0] <= oldMapping[0][0] + oldMapping[1] and oldMapping[0][1] + oldMapping[1] <= newMapping[0][1]:
                oldMappingAdjusted = (oldMapping[0],oldMapping[1] + newMapping[1],'Complete Overlap')
                newMappingsAdjusted.append(oldMappingAdjusted)
            elif oldMapping[0][0] + oldMapping[1] < newMapping[0][1] <= oldMapping[0][1] + oldMapping[1]:
                oldMappingPL = ((oldMapping[0][0],newMapping[0][1]-oldMapping[1]),oldMapping[1]+newMapping[1],'LeftNew')
                oldMappingPR = ((newMapping[0][1]-oldMapping[1],oldMapping[0][1]),oldMapping[1], 'LeftOld')
                newMappingsAdjusted.append(oldMappingPL)
                newMappingsAdjusted.append(oldMappingPR)
            elif oldMapping[0][1] + oldMapping[1] > newMapping[0][0] >= oldMapping[0][0] + oldMapping[1]:
                oldMappingPL = ((oldMapping[0][0],newMapping[0][0]-oldMapping[1]),oldMapping[1], 'RightOld')
                oldMappingPR = ((newMapping[0][0]-oldMapping[1],oldMapping[0][1]),oldMapping[1]+newMapping[1],'RightNew')
                newMappingsAdjusted.append(oldMappingPL)
                newMappingsAdjusted.append(oldMappingPR)
            #Adjust new value of Range so it doesn't overlap with older ranges
            if oldMapping[0][0] <= newMapping[0][1] < oldMapping[0][1]:
                newEnd = oldMapping[0][0]
            if oldMapping[0][0] < newMapping[0][0] <= oldMapping[0][1]:
                newStart = oldMapping[0][1]
        if not newStart >= newEnd:
            newMappingsAdjusted.append(((newStart,newEnd),newMapping[1]))
    ic(newMappingsAdjusted)
    return newMappingsAdjusted

def mappingGenerator(maps):
    mappings = list()
    newMappings = list()
    maps = list(filterfalse(lambda line: not re.search(r'[a-z]',line) == None,maps))
    for line in maps:
        if line == '':
            mappings = adjustOldMappings(newMappings,mappings)
            newMappings = list()
            continue
        numbers = [int(n) for n in line.split(' ')]
        mapping = ((numbers[1],numbers[1] + numbers[2]),numbers[0]-numbers[1])
        newMappings.append(mapping)

def evaluateMap(line: str,seed: tuple[int,bool]):
    mapping = [int(n) for n in line.split(' ')]
    if not mapping[1] <= seed[0] < mapping[1]+mapping[-1] or seed[1]:
        return seed
    converted = seed[0] - (mapping[1] - mapping[0])
    return converted,True

def mapSeedsToLocations(seeds, maps):
    for line in maps:
        if any(c.isdigit() for c in line):
            seeds = list(map(lambda x: evaluateMap(line,x),seeds))
        if line == '':
            seeds = [(seed[0],False) for seed in seeds]
    return [seed[0] for seed in seeds]

def solutionB(input):
    seeds = [int(n) for n in re.findall(r'\d+',input[0])]
    seeds = list(pairwise(seeds))[0::2]
    seeds = [list(range(seedRange[0],seedRange[0]+seedRange[1])) for seedRange in seeds]
    seeds = [(n,False) for n in list(chain.from_iterable(seeds))]
    locations = mapSeedsToLocations(seeds,input[2:])
    print(min(locations))
        
def solutionA(input):
    seeds = [(int(n),False) for n in re.findall(r'\d+',input[0])]
    locations = mapSeedsToLocations(seeds,input[2:])
    print(min(locations))

def newSolutionA(input):
    mappings = mappingGenerator(input[2:])
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput(r'2023\testinput05.txt')
    #solutionA(input)
    #solutionB(input)
    newSolutionA(input)

if __name__ == '__main__':
    main()