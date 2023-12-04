from collections import deque
from icecream import ic

def parseCard(card):
    winning = {int(num) for num in card.split('|')[0].split(' ') if num.isdigit()}
    mine = {int(num) for num in card.split('|')[1].split(' ') if num.isdigit()}
    return winning,mine

def parseCards(input):
    cards = [line.split(':')[1] for line in input]
    cards = [(parseCard(card)) for card in cards]
    return cards

def solutionB(input):
    cards = parseCards(input)
    startingList = [(i,len(card[0]&card[1])) for i,card in enumerate(cards)]
    to_evaluate = deque(startingList)
    done = deque()
    while(len(to_evaluate)>0):
        card = to_evaluate.pop()
        for i in range(1,card[1]+1):
            to_evaluate.append(startingList[card[0]+i])
        done.append(card)
    print(len(done))
        
def solutionA(input):
    cards = parseCards(input)
    winningValues = [card[0] & card[1] for card in cards]
    points = [int(1*pow(2,len(values)-1)) for values in winningValues]
    print(sum(points))
    
def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def main():
    input = parseInput('2023\input04.txt')
    solutionA(input)
    solutionB(input)

if __name__ == '__main__':
    main()