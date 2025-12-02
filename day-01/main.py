"""
https://adventofcode.com/2025/day/1
"""

from dataclasses import dataclass
from enum import Enum

TEST_DATA = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


class Direction(str, Enum):
    L = "L"
    R = "R"


@dataclass
class Move:
    direction: Direction
    steps: int

    @classmethod
    def parse(cls, v: str) -> "Move":
        direction: Direction = Direction(v[0])
        steps: int = int(v[1:])
        return cls(direction=direction, steps=steps)


class Dial:
    def __init__(self, init: int = 50):
        self.current = init

    def move(self, step: Move):
        if step.direction == Direction.R:
            self.current = (self.current + step.steps) % 100
        if step.direction == Direction.L:
            self.current = (self.current - step.steps) % 100


class Solver:
    def __init__(self, dial: Dial, steps: list[Move]):
        self.dial = dial
        self.steps = steps
        self.result = 0

    def solve(self):
        for step in self.steps:
            self.dial.move(step)
            self.result += 1 if self.dial.current == 0 else 0


def solve(init: int, steps: list[Move]) -> tuple[int, int]:
    dial = Dial(init)
    solver: Solver = Solver(dial, steps)
    solver.solve()
    return solver.result, dial.current


def get_external_data(f_name: str) -> list[Move]:
    with open(f_name) as fp:
        data = [line.strip() for line in fp]
        steps: list[Move] = [Move.parse(cmd) for cmd in data]
        return steps


if __name__ == "__main__":
    print("--- Day 1: Secret Entrance ---")
    steps: list[Move] = [Move.parse(item) for item in TEST_DATA]
    steps = get_external_data("input.txt")
    print(solve(50, steps)[0])

    result = 0
    init = 50
    for step in steps:
        steps: list[Move] = [
            Move(direction=step.direction, steps=1) for _ in range(step.steps)
        ]
        res, init = solve(init, steps)
        result += res
    print(result)
