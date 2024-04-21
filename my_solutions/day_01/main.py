import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input):
        result = 0
        for row in raw_input:
            result += find_calibration_value(row)
        return result

    def solve_part_2(self, raw_input):
        ...

def find_calibration_value(string):
    first_digit = find_calibration_digit(string)
    last_digit = find_calibration_digit(string[::-1])
    return int("{}{}".format(first_digit, last_digit))


def find_calibration_digit(string):
    for char in string:
        if char.isdigit():
            return char