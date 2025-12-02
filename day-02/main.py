"""
https://adventofcode.com/2025/day/2
"""

from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Token:
    start: int
    end: int


def generate_results(token: Token) -> Iterator[int]:
    for n in range(token.start, token.end + 1):
        s: str = f"{n}"
        if len(s) % 2 == 0:
            mid: int = len(s) // 2
            if s[:mid] == s[mid:]:
                yield n


def get_external_data(f_name: str) -> Iterator[Token]:
    with open(f_name) as fp:
        tokens: list[str] = [s.strip() for s in fp.read().split(",")]
        for t in tokens:
            d = t.split("-")
            yield Token(start=int(d[0]), end=int(d[1]))


if __name__ == "__main__":
    print("--- Day 2: Gift Shop ---")
    res: int = sum(
        sum(generate_results(token)) for token in get_external_data("input.txt")
    )
    print(res)
