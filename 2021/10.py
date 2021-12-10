def findCorrupted(input) -> list:
    close= [')',']','}','>']
    stack = []
    corruptedLines = []
    for l in input:
        corrupted = False
        for c in l:
            if c not in close:
                stack.append(c)
            else:
                match c:
                    case ')':
                        if stack[-1] != '(':
                            corrupted = True 
                    case ']':
                        if stack[-1] != '[':
                            corrupted = True
                    case '}':
                        if stack[-1] != '{':
                            corrupted = True
                    case '>':
                        if stack[-1] != '<':
                            corrupted = True
                if corrupted:
                    break
                else: stack.pop()  
        corruptedLines.append((corrupted,c))    
    return corruptedLines

def solutionA(input):
    scores = {')': 3,']': 57, '}':1197,'>':25137}
    corruptedLines = findCorrupted(input)
    score = [scores[x[1]] for x in list(filter(lambda x: x[0],corruptedLines))]                      
    print(sum(score))
    
def solutionB(input):
    corruptedLines = findCorrupted(input)
    incompleteLines = [x[0] for x in list(filter(lambda x: not x[1][0], list(zip(input,corruptedLines))))]
    close = {'[':']','{':'}','(':')','<':'>'}
    scoreDict = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for l in incompleteLines:
        stack = []
        for c in l:
            if c in close.keys():
                stack.append(close[c])
            elif c == stack[-1]:
                stack.pop()
        stack.reverse()        
        closingScore = [scoreDict[x] for x in stack]
        score = 0
        for x in closingScore:
            score *= 5
            score += x
        scores.append(score)   
    scores.sort()     
    print(scores[int(len(scores)/ 2)])
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
    return lines

def main():
    input = parseInput('input10')
    solutionA(input)
    solutionB(input)
if __name__ == '__main__':
    main()