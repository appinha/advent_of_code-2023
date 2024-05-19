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

    def solve_part_2(self, raw_input: str):
        schematic = lib.Grid(string=raw_input)
        number_by_location, gears = get_numbers_and_gears(schematic)
        gear_ratios = []

        for gear in gears:
            numbers = []
            neighbours = schematic.list_neighbours(gear, include_diagonals=True)
            for neighbour in neighbours:
                number = number_by_location.get(neighbour)
                if number and number not in numbers:
                    numbers.append(number)
            if len(numbers) == 2:
                gear_ratios.append(lib.prod(numbers))

        return sum(gear_ratios)


def has_adj_symbol(schematic: lib.Grid, location: tuple[int, int]):
    neighbour_locations = schematic.list_neighbours(location, include_diagonals=True)

    for loc in neighbour_locations:
        char: str = schematic.grid[loc]
        if char != "." and not char.isdigit():
            return True

    return False


def get_numbers_and_gears(schematic: lib.Grid):
    curr_row = 0
    number = ""
    number_locations = []

    number_by_location = {}
    gears = []

    for location in schematic.locations:
        char: str = schematic.grid[location]

        if char == "*":
            gears.append(location)

        if curr_row != location[0] or not char.isdigit():
            if number:
                for location in number_locations:
                    number_by_location[location] = int(number)
            number = ""
            number_locations = []
            curr_row = location[0]

        if char.isdigit():
            number += char
            number_locations.append(location)

    return number_by_location, gears
