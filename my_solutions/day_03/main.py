from __future__ import annotations
import sys

sys.path.insert(0, "..")
import aoc_lib as lib
from aoc_lib import ROW, COL
from aoc_lib.imports import *


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = ""

    def solve_part_1(self, raw_input: str):
        schematic = lib.Grid(string=raw_input)

        curr_row = 0
        number = ""
        is_part_number = False
        part_numbers = []

        for location in schematic.locations:
            char: str = schematic.grid[location]

            if curr_row != location[0] or not char.isdigit():
                if is_part_number and number:
                    part_numbers.append(int(number))
                number = ""
                is_part_number = False
                curr_row = location[0]

            if char.isdigit():
                number += char
                if has_adj_symbol(schematic, location):
                    is_part_number = True

        return sum(part_numbers)

    def solve_part_2(self, raw_input: str): ...


def has_adj_symbol(schematic: lib.Grid.grid, location: tuple[int, int]):
    neighbour_locations = schematic.list_neighbours(location, include_diagonals=True)

    for loc in neighbour_locations:
        char: str = schematic.grid[loc]
        if char != "." and not char.isdigit():
            return True

    return False
