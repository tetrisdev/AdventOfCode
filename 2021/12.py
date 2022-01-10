from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Cave():
    name: str
    neighbours: List(Cave) = field(compare=False, default_factory=list)
    visits: int = field(compare=False, default=0)

    def add_neighbour(self, cave: Cave):
        if cave in self.neighbours:
            return
        self.neighbours.append(cave)

    def visit(self):
        self.visits += 1

    def unvisit(self):
        self.visits -= 1


def generateGraph(input) -> dict:
    caves = {}
    for line in input:
        offset = (1, -1)
        path = [Cave(c) for c in line.split('-')]
        for i, cave in enumerate(path):
            neighbour = path[i+offset[i]]
            if neighbour in caves.values():
                neighbour = caves[neighbour.name]
            if cave in caves.values():
                cave = caves[cave.name]
            cave.add_neighbour(neighbour)
            caves[cave.name] = cave
    return caves


def traverse(cave: Cave) -> int:
    if cave.name == "end":
        return 1
    cave.visit()
    sum = 0
    for neighbour in cave.neighbours:
        if neighbour.name.islower() and neighbour.visits > 0:
            continue
        sum += traverse(neighbour)
    cave.unvisit()
    return sum


def traverseTwice(cave: Cave) -> int:
    if cave.name == "end":
        return 1
    cave.visit()
    sum = 0
    for neighbour in cave.neighbours:
        if neighbour.name.islower() and neighbour.visits > 1 or neighbour.name == "start":
            continue
        if neighbour.name.islower() and neighbour.visits == 1:
            sum += traverse(neighbour)
        else:
            sum += traverseTwice(neighbour)
    cave.unvisit()
    return sum


def solutionA(input):
    graph = generateGraph(input)
    print(traverse(graph["start"]))


def solutionB(input):
    graph = generateGraph(input)
    print(traverseTwice(graph["start"]))


def parseInput(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        lines = [x.strip('\n') for x in lines]
    return lines


def main():
    input = parseInput('input12')
    # input = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
    solutionA(input)
    solutionB(input)


if __name__ == '__main__':
    main()
