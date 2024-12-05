from gettext import find
import itertools
import statistics
from icecream import ic
from aocd import get_data

def generateRules(input):
    rules = itertools.takewhile(lambda x: x != '', input)
    rulesDict = dict()
    for rule in rules:
        key = int(rule.split("|")[0])
        value = int(rule.split("|")[1])
        rulesDict.setdefault(key, [])
        rulesDict[key].append(value)
    return rulesDict

def checkUpdates(updates, rules):
    correctUpdates = []
    wrongUpdates = []
    for update in updates:
        correct = findWrongIndex(update, rules) == -1
        if correct:
            correctUpdates.append(update)
        else:
            wrongUpdates.append(update)
    return correctUpdates, wrongUpdates

def findWrongIndex(wrongUpdate, rules):
    for i,page in enumerate(wrongUpdate):
        if page not in rules:
            continue
        if len(set.intersection(set(wrongUpdate[:i]),set(rules[page]))) != 0:
            return i
    return -1

def solutionA(input):
    rules = generateRules(input)
    splitIndex = input.index("")
    toPrint = input[splitIndex+1:]
    updates = [[int(x) for x in page.split(',')] for page in toPrint]
    correctUpdates, wrongUpdates = checkUpdates(updates, rules)
    middlePages = [update[int(len(update)/2)] for update in correctUpdates]
    ic(sum(middlePages))
    solutionB(wrongUpdates, rules)
    
def solutionB(wrongUpdates, rules):
    for i,update in enumerate(wrongUpdates):
        while findWrongIndex(update, rules) != -1:
            wrongIndex = findWrongIndex(update, rules)
            swap = update[wrongIndex-1]
            update[wrongIndex-1] = update[wrongIndex]
            update[wrongIndex] = swap
        wrongUpdates[i] = update
    middlePages = [update[int(len(update)/2)] for update in wrongUpdates]
    ic(sum(middlePages))
def main():
    input = get_data(day=5, year=2024).split('\n')
    solutionA(input)
    #solutionB(input)

if __name__ == '__main__':
    main()