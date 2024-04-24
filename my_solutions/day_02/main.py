import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from aoc_lib.imports import *


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input):
        games = process_input(raw_input)

        result = 0
        for game in games:
            is_valid_game = True
            for colour, qty in game.maximums.items():
                if qty > limits[colour]:
                    is_valid_game = False
                    break
            if is_valid_game:
                result += game.id

        return result


    def solve_part_2(self, raw_input):
        ...


limits = { "red": 12, "green": 13, "blue": 14 }


class Game:
    def __init__(self, id, sets):
        self.id = id
        self.maximums = self.get_maximums(sets)

    def __repr__(self):
        return f"{self.id}: {self.maximums}"

    def get_maximums(self, sets):
        maximums = { "red": 0, "green": 0, "blue": 0 }
        for s in sets:
            for cube in s:
                if maximums[cube.colour] < cube.qty:
                    maximums[cube.colour] = cube.qty
        return maximums


class CubeQty(NamedTuple):
    colour: str
    qty: int


def process_input(raw_input):

    def process_cube(cube):
        qty, colour = cube.split(" ")
        return CubeQty(colour, int(qty))

    def process_set(cube_set):
        cube_set = cube_set.split(", ")
        cube_set = [process_cube(cube) for cube in cube_set]
        return cube_set

    games = []

    for row in raw_input:
        game, sets = row.split(": ")
        game_id = lib.find_all_integers(game)[0]
        sets = sets.split("; ")
        sets = [process_set(s) for s in sets]
        games.append(Game(game_id, sets))

    return games
