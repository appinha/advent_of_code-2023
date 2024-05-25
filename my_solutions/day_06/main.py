from __future__ import annotations
import sys
from math import sqrt, floor

sys.path.insert(0, "..")
import aoc_lib as lib
from aoc_lib import ROW, COL
from aoc_lib.imports import *


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: str):
        times_and_distances = process_input(raw_input)

        all_opt_times = []
        for time, distance in times_and_distances:
            min_time = (time - sqrt(time**2 - 4 * distance)) / 2
            min_hold_time = floor(min_time + 1)
            opt_times = time - 2 * min_hold_time + 1
            all_opt_times.append(opt_times)

        return lib.prod(all_opt_times)

    def solve_part_2(self, raw_input: str): ...


def process_input(raw_input: str):
    times = lib.find_all_integers(raw_input[0])
    distances = lib.find_all_integers(raw_input[1])
    return [(times[i], distances[i]) for i in range(len(times))]
