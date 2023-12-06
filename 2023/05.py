from itertools import filterfalse, pairwise
from icecream import ic
import re
import time

def adjustOldMappings(newMappings, oldMaps):
    newMappingsAdjusted = [(oldMap[0],oldMap[1],'Old') for oldMap in oldMaps]
    for newMapping in newMappings:
        newStart, newEnd = newMapping[0]
        newStartAdjusted,newEndAdjusted = newMapping[0]
        for oldMapping in oldMaps:
            oldStart, oldEnd = oldMapping[0]
            oldStart += oldMapping[1]
            oldEnd += oldMapping[1]
            #Adjust Old Mappings with new Values if range is somewhere in there
            if oldStart <= newStart and oldEnd >= newEnd:
                oldMappingPL = ((oldMapping[0][0],newStart-oldMapping[1]),oldMapping[1], 'Old')
                oldMappingMid = ((newStart-oldMapping[1],newEnd-oldMapping[1]),oldMapping[1] + newMapping[1],'')
                oldMappingPR = ((newEnd-oldMapping[1],oldMapping[0][1]),oldMapping[1], 'Old')
                temp = [oldMappingPL,oldMappingMid,oldMappingPR]
                for mapping in temp:
                    if not mapping[0][0] + 1 >= mapping[0][1]:
                        newMappingsAdjusted.append(mapping)
            elif newStart <= oldStart and oldEnd <= newEnd:
                oldMappingAdjusted = (oldMapping[0],oldMapping[1] + newMapping[1],'')
                newMappingsAdjusted.append(oldMappingAdjusted)
            elif oldStart < newEnd <= oldEnd:
                oldMappingPL = ((oldMapping[0][0],newEnd-oldMapping[1]),oldMapping[1]+newMapping[1],'')
                oldMappingPR = ((newEnd-oldMapping[1],oldMapping[0][1]),oldMapping[1], 'Old')
                newMappingsAdjusted.append(oldMappingPL)
                newMappingsAdjusted.append(oldMappingPR)
            elif oldEnd > newStart >= oldStart:
                oldMappingPL = ((oldMapping[0][0],newStart-oldMapping[1]),oldMapping[1], 'Old')
                oldMappingPR = ((newStart-oldMapping[1],oldMapping[0][1]),oldMapping[1]+newMapping[1],'')
                newMappingsAdjusted.append(oldMappingPL)
                newMappingsAdjusted.append(oldMappingPR)
            #Adjust new value of Range so it doesn't overlap with older ranges
            if oldMapping[0][0] <= newEnd < oldMapping[0][1]:
                newEndAdjusted = oldMapping[0][0]
            if oldMapping[0][0] < newStart <= oldMapping[0][1]:
                newStartAdjusted = oldMapping[0][1]
        if not newStartAdjusted >= newEndAdjusted:
            newMappingsAdjusted.append(((newStartAdjusted,newEndAdjusted),newMapping[1],''))
    newMappingsAdjusted.sort(key=lambda x: x[0][0])
    return newMappingsAdjusted

def collapseOverlap(maps):
    filtered_data = {}
    for item in maps:
        key = item[0][0]
        end = item[0][1]
        if key in filtered_data:
            if item[2] == 'Old' or filtered_data[key][0][1] < end:
                if filtered_data[key][2] == 'Old' and end < filtered_data[key][0][1]:
                    filtered_data[key] = item
                continue
        filtered_data[key] = item

    result = list(filtered_data.values())
    return result

def mappingGenerator(maps):
    mappings = list()
    newMappings = list()
    maps = list(filterfalse(lambda line: not re.search(r'[a-z]',line) == None,maps))
    for line in maps:
        if line == '':
            mappings = adjustOldMappings(newMappings,mappings)
            #ic(mappings)
            mappings = collapseOverlap(mappings)
            newMappings = list()
            continue
        numbers = [int(n) for n in line.split(' ')]
        mapping = ((numbers[1],numbers[1] + numbers[2]),numbers[0]-numbers[1])
        newMappings.append(mapping)
    mappings = adjustOldMappings(newMappings,mappings)
    mappings = collapseOverlap(mappings)
    #ic(mappings)
    mappings = [(mapping[0],mapping[1]) for mapping in mappings]
    return mappings

def findMinLocation(seedRanges,lowestMappings):
    for range1 in lowestMappings:
        for range2 in seedRanges:
            intersection_start = max(range1[0][0][0], range2[0])
            intersection_end = min(range1[0][0][1], range2[1])
            if intersection_start <= intersection_end:
                intersection_min = min(range(intersection_start, intersection_end + 1))
                return intersection_min + range1[0][1]
    return -1

def newSolutionA(input):
    seeds = [int(n) for n in re.findall(r'\d+',input[0])]
    mappings = mappingGenerator(input[2:])
    seedLocations = [seed + mapping[1] for seed in seeds for mapping in mappings if seed in range(mapping[0][0],mapping[0][1])]
    #ic(seedLocations)
    ic(min(seedLocations))

def newSolutionB(input):
    mappings = mappingGenerator(input[2:])
    seeds = [int(n) for n in re.findall(r'\d+',input[0])]
    seedRanges = list(pairwise(seeds))[0::2]
    seedRanges = [(n[0],n[0]+n[1]) for n in seedRanges]
    lowestMappings = [(mapping,mapping[0][0] + mapping[1]) for mapping in mappings]
    lowestMappings.sort(key=lambda x: x[1])
    min_location = findMinLocation(seedRanges,lowestMappings)
    ic(min_location)
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput(r'2023\input05.txt')
    newSolutionA(input)
    newSolutionB(input)
    
if __name__ == '__main__':
    main()