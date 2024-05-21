from __future__ import annotations
import sys

sys.path.insert(0, "..")
import aoc_lib as lib
from aoc_lib import ROW, COL
from aoc_lib.imports import *


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n\n"

    def solve_part_1(self, raw_input: str):
        seeds, blocks = process_input(raw_input)
        locations = []

        for seed in seeds:
            for block in blocks:
                seed = get_new_value(seed, block)
            locations.append(seed)

        return min(locations)

    def solve_part_2(self, raw_input: str): ...


def process_input(raw_input: str):
    seeds = lib.find_all_integers(raw_input[0])

    blocks: list[list[list[int]]] = []
    for raw_block in raw_input[1:]:
        raw_lines = raw_block.split("\n")
        lines = [lib.find_all_integers(rl) for rl in raw_lines[1:]]
        blocks.append(lines)

    return seeds, blocks


def get_new_value(seed: int, block: list[list[int]]):
    new_value = 0

    for line in block:
        dst_start = line[0]
        src_start = line[1]
        src_end = src_start + line[2]

        if src_start <= seed < src_end:
            new_value = dst_start + (seed - src_start)
            break

    return new_value if new_value > 0 else seed
