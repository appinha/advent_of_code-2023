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

    def solve_part_2(self, raw_input: str):
        seeds, blocks = process_input(raw_input)
        seed_ranges = get_seed_ranges(seeds)

        location_ranges = []

        for seed_range in seed_ranges:
            new_ranges = [seed_range]
            for block in blocks:
                new_ranges = get_new_ranges(new_ranges, block)
            location_ranges += new_ranges

        location_mins = [loc_range[0] for loc_range in location_ranges]
        return min(location_mins)


def process_input(raw_input: str):
    seeds = lib.find_all_integers(raw_input[0])

    blocks: list[list[list[int]]] = []
    for raw_block in raw_input[1:]:
        raw_lines = raw_block.split("\n")
        lines = [lib.find_all_integers(rl) for rl in raw_lines[1:]]
        blocks.append(lines)

    return seeds, blocks


def get_limits(line: list[int]):
    dst_start = line[0]
    src_start = line[1]
    src_end = src_start + line[2]

    return dst_start, src_start, src_end


def get_new_value(seed: int, block: list[list[int]]):
    new_value = 0

    for line in block:
        dst_start, src_start, src_end = get_limits(line)

        if src_start <= seed < src_end:
            new_value = dst_start + (seed - src_start)
            break

    return new_value if new_value > 0 else seed


def get_seed_ranges(seeds: list[int]):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
    return seed_ranges


def split_seed_ranges(seed_ranges: tuple[int, int], block: list[list[int]]):
    for line in block:
        _, src_start, src_end = get_limits(line)

        new_ranges = []

        for s_range in seed_ranges:

            # |--map--|                           |--map--|
            #           |--seeds--|    |--seeds--|
            if src_end < s_range[0] or s_range[1] < src_start:
                new_ranges.append(s_range)
                continue

            #    |--map--|       |--map--|            |--map--|
            # |----seeds----|    |--seeds----|    |----seeds--|
            if s_range[0] <= src_start and src_end <= s_range[1]:
                if s_range[0] != src_start:
                    new_ranges.append((s_range[0], src_start - 1))
                new_ranges.append((src_start, src_end))
                if src_end != s_range[1]:
                    new_ranges.append((src_end + 1, s_range[1]))
                continue

            # |------map------|
            #    |--seeds--|
            if src_start <= s_range[0] and s_range[1] <= src_end:
                new_ranges.append((s_range[0], s_range[1]))
                continue

            #       |--map--|
            # |--seeds--|
            if src_start <= s_range[0]:
                new_ranges.append((s_range[0], src_end))
                new_ranges.append((src_end + 1, s_range[1]))
                continue

            # |--map--|
            #     |--seeds--|
            if s_range[1] <= src_end:
                new_ranges.append((s_range[0], src_start - 1))
                new_ranges.append((src_start, s_range[1]))
                continue

        seed_ranges = new_ranges

    return new_ranges


def shift_seed_ranges(seed_ranges: tuple[int, int], block: list[list[int]]):
    new_ranges = []

    for s_range in seed_ranges:
        shifted = False

        for line in block:
            dst_start, src_start, src_end = get_limits(line)
            diff = src_start - dst_start

            if src_start <= s_range[0] and s_range[1] <= src_end:
                new_ranges.append((s_range[0] - diff, s_range[1] - diff))
                shifted = True
                continue

        if not shifted:
            new_ranges.append(s_range)

    return new_ranges if new_ranges else seed_ranges


def get_new_ranges(seed_ranges: tuple[int, int], block: list[list[int]]):
    splitted_ranges = split_seed_ranges(seed_ranges, block)
    shifted_ranges = shift_seed_ranges(splitted_ranges, block)
    return shifted_ranges
