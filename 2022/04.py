def solveA(pair):
	x,y = pair.split(',')
	x = set(range(int(x.split('-')[0]),int(x.split('-')[1])+1))
	y = set(range(int(y.split('-')[0]),int(y.split('-')[1])+1))
	union = x.union(y)
	if x == union or y == union:
		return 1
	return 0

def solveB(pair):
	x,y = pair.split(',')
	x = set(range(int(x.split('-')[0]),int(x.split('-')[1])+1))
	y = set(range(int(y.split('-')[0]),int(y.split('-')[1])+1))
	inter = x.intersection(y)
	if len(inter) > 0:
		return 1
	return 0
 
def solutionA(input):
	c = sum(list(map(solveA,input)))
	print(c)

def solutionB(input):
	c = sum(list(map(solveB,input)))
	print(c)
 
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [x.strip('\n') for x in lines]
    return lines

def main():
    input = parseInput('input04')
    #input = ['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8']
    #solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()