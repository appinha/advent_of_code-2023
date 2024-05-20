from __future__ import annotations
import sys
from typing import NamedTuple

sys.path.insert(0, "..")
import aoc_lib as lib
from aoc_lib import ROW, COL
from aoc_lib.imports import *


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: str):
        cards = process_input(raw_input)
        result = 0

        for card in cards:
            winning_qty = -1
            for number in card.card_numbers:
                if number in card.winning_numbers:
                    winning_qty += 1
            if winning_qty >= 0:
                result += 2**winning_qty

        return result

    def solve_part_2(self, raw_input: str): ...


class Card(NamedTuple):
    id: int
    winning_numbers: list[int]
    card_numbers: list[int]


def process_input(raw_input: str):
    cards: list[Card] = []

    for line in raw_input:
        name, table = line.split(":")
        winning_numbers, card_numbers = table.split("|")
        id = lib.find_all_integers(name)
        winning_numbers = lib.find_all_integers(winning_numbers)
        card_numbers = lib.find_all_integers(card_numbers)
        cards.append(Card(id, winning_numbers, card_numbers))

    return cards
