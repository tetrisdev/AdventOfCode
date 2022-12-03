def prio(char):
    prio = ord(char)
    return prio - 96 if prio > 96 else prio - 38

def solveA(line):
	line = line.strip('\n')
	a = line[:len(line)//2]
	b = line[len(line)//2:]
	for c in a:
		if c in b:
			res = c
			break
	return prio(res)

def solveB(list):
    for c in list[0]:
        if c in list[1] and c in list[2]:
            res = c
            break
    return prio(res)

def solutionA(input):
	res = list(map(solveA,input))
	print(sum(res))
 
def solutionB(input):
	res = list(map(solveB,list(zip(*[iter(input)]*3))))
	print(sum(res))

def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
	input = parseInput('input03')
	#input = ["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]
	solutionA(input)
	solutionB(input)

if __name__ == '__main__':
    main()