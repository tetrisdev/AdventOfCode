from dataclasses import dataclass
from itertools import combinations
from collections import Counter

@dataclass
class Vent:
    start: tuple
    end: tuple

    def pointOnLine(self, point:tuple) -> bool:
        x1,y1 = self.start
        x2,y2 = self.end
        x3,y3 = point
        crossproduct = (y3 - y1) * (x2 - x1) - (x3 - x1) * (y2 - y1)
        if crossproduct != 0:
            return False

        dotproduct = (x3 - x1) * (x2 - x1) + (y3 - y1)*(y2 - y1)
        if dotproduct < 0:
            return False
        
        squaredlengthba = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
        if dotproduct > squaredlengthba:
            return False
        return True

    def intersection(self,vent) -> tuple:
        Aself = self.end[1] - self.start[1]
        Bself = self.start[0] - self.end[0]
        Cself = Aself * self.start[0] + Bself * self.start[1]
        A2 = vent.end[1] - vent.start[1]
        B2 = vent.start[0] - vent.end[0]
        C2 = A2 * vent.start[0] + B2 * vent.start[1]
        det = Aself * B2 - A2 * Bself
        if det != 0:
            x = int((B2 * Cself - Bself*C2) / det)
            y = int((Aself * C2 - A2 * Cself) / det)
            if self.pointOnLine((x,y)) and vent.pointOnLine((x,y)):
                    return (x,y)

def generateVents(input) -> list:
    tuples = [(int(x),int(y)) for x,y in [x.split(',') for coords in [p.split('->') for p in input] for x in coords]]
    return [Vent(p1,p2) for p1,p2 in zip(*[iter(tuples)]*2)]

def solutionA(input):
    vents = generateVents(input)
    straight = list(filter(lambda v: v.start[0] == v.end[0] or v.start[1] == v.end[1],vents))
    points = []
    for v in straight:  
        x1,y1 = v.start
        x2,y2 = v.end
        for x in range(x1 if x1<x2 else x2,x2+1 if x2 > x1 else x1+1,1):
            for y in range(y1 if y1<y2 else y2,y2+1 if y2 > y1 else y1+1,1):
                if v.pointOnLine((x,y)):
                    points.append((x,y))
    print(len(list(filter(lambda x: x[1] >= 2,zip(Counter(points),Counter(points).values())))))
    
def solutionB(input):
    # Needs Optimization for iterating through diagonal Lines.
    vents = generateVents(input)
    points = []
    for v in vents:  
        x1,y1 = v.start
        x2,y2 = v.end
        for x in range(x1 if x1<x2 else x2,x2+1 if x2 > x1 else x1+1,1):
            for y in range(y1 if y1<y2 else y2,y2+1 if y2 > y1 else y1+1,1):
                if v.pointOnLine((x,y)):
                    points.append((x,y))
    print(len(list(filter(lambda x: x[1] >= 2,zip(Counter(points),Counter(points).values())))))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input05')
    #input = ['0,9 -> 5,9','8,0 -> 0,8','9,4 -> 3,4','2,2 -> 2,1','7,0 -> 7,4','6,4 -> 2,0','0,9 -> 2,9','3,4 -> 1,4','0,0 -> 8,8','5,5 -> 8,2']
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()