from __future__ import annotations
import sys
import re
from math import sqrt, floor

sys.path.insert(0, "..")
import aoc_lib as lib
from aoc_lib import ROW, COL
from aoc_lib.imports import *


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: str):
        times_and_distances = process_input_1(raw_input)

        all_opt_times = []
        for time, distance in times_and_distances:
            all_opt_times.append(find_total_beat_times(time, distance))

        return lib.prod(all_opt_times)

    def solve_part_2(self, raw_input: str):
        time, distance = process_input_2(raw_input)
        return find_total_beat_times(time, distance)


def process_input_1(raw_input: str):
    times = lib.find_all_integers(raw_input[0])
    distances = lib.find_all_integers(raw_input[1])
    return [(times[i], distances[i]) for i in range(len(times))]


def extract_digits(string: str):
    return "".join(re.findall(r"\d", string))


def process_input_2(raw_input: str):
    return [int(extract_digits(line)) for line in raw_input]


def find_total_beat_times(time: int, distance: int):
    min_time = (time - sqrt(time**2 - 4 * distance)) / 2
    min_hold_time = floor(min_time + 1)
    return time - 2 * min_hold_time + 1
