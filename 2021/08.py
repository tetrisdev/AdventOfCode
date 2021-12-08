from dataclasses import dataclass
from collections import Counter

@dataclass
class sevenSeg():
    decodingInput : list
    input : list
    decodedPanels : dict
    sevenSegNums = {"abcefg": 0,"cf":1,"acdeg":2,"acdfg":3,"bcdf":4,"abdfg":5,"abdefg":6,"acf":7,"abcdefg":8,"abcdfg":9}

    def decode(self):
        self.decodingInput.sort(key=len)
        self.decodedPanels[list(filter(lambda x: x not in self.decodingInput[0],self.decodingInput[1]))[0]] = "a"
        self.decodedPanels[Counter(self.decodingInput[3] + self.decodingInput[4] + self.decodingInput[5] + self.decodingInput[2]).most_common()[0][0]] = "d"
        self.decodedPanels[Counter(self.decodingInput[3] + self.decodingInput[4] + self.decodingInput[5] + self.decodingInput[2]).most_common()[-1][0]] = "e"
        seg235not1 =  list(filter(lambda x: x not in self.decodingInput[0],self.decodingInput[3] + self.decodingInput[4] + self.decodingInput[5]))
        self.decodedPanels[list(filter(lambda x: x not in self.decodedPanels.keys(),list(filter(lambda x: x!= False,[x[0] if x[1] <= 2 else False for x in Counter(seg235not1).most_common()]))))[0]] = "b"
        eg = list(filter(lambda x: x not in self.decodingInput[1] + self.decodingInput[2],self.decodingInput[9]))
        self.decodedPanels[list(filter(lambda x: x not in self.decodedPanels.keys(),eg))[0]] = "g"
        for num in self.decodingInput[3:6]:
            if len(list(filter(lambda x: x not in self.decodingInput[2], num))) == 3:
                two = num
            elif len(list(filter(lambda x: x not in self.decodingInput[0], num))) == 4:
                five = num
        self.decodedPanels[Counter(two + self.decodingInput[0]).most_common()[0][0]] = "c"
        self.decodedPanels[Counter(five + self.decodingInput[0]).most_common()[0][0]] = "f"
        for i, num in enumerate(self.input):
            self.input[i] = [self.decodedPanels[c] for c in num]
        self.input = [self.sevenSegNums[x] for x in [''.join(sorted(x)) for x in self.input]]
def generateSevenSeg(input) -> list:
    segs = []
    for seg in input:
        seg = seg.split('|')
        decodeSignals = list(filter(lambda x : len(x) != 0,[sorted(x) for x in seg[0].split(' ')]))
        numInput = list(filter(lambda x: len(x) != 0,[sorted(x) for x in seg[1].split(' ')]))
        decodeSignals = list(map(lambda x: list(filter(lambda y: y != '\n',x)),decodeSignals))
        numInput = list(map(lambda x: list(filter(lambda y: y != '\n',x)),numInput))
        segs.append(sevenSeg(decodeSignals,numInput,{}))
    return segs

def solutionA(input):
    segs = generateSevenSeg(input)
    for seg in segs:
        seg.decode()
    segs = [i for seg in segs for i in seg.input]
    count = Counter(segs)    
    print(count[1] + count[4] + count[7] + count[8])
    
def solutionB(input):
    segs = generateSevenSeg(input)
    for seg in segs:
        seg.decode()
        seg.input = int(''.join([str(x) for x in seg.input]))
    print(sum([seg.input for seg in segs]))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input08')
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()