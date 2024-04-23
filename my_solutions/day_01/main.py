import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input):
        result = 0
        for row in raw_input:
            result += find_calibration_value_p1(row)
        return result

    def solve_part_2(self, raw_input):
        result = 0
        for row in raw_input:
            result += find_calibration_value_p2(row)
        return result


numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def find_calibration_value_p1(string):

    def find_calibration_digit(string):
        for char in string:
            if char.isdigit():
                return char

    first_digit = find_calibration_digit(string)
    last_digit = find_calibration_digit(string[::-1])
    return int("{}{}".format(first_digit, last_digit))


def find_calibration_value_p2(string):

    def find_calibration_digit(string, is_reversed = False):
        for i in range(0, len(string)):
            digit = match_string_to_digit(string[i:i + 5], is_reversed)
            if digit:
                return digit

    def match_string_to_digit(string, is_reversed):
        for i in range(0, 2):
            if string[i].isdigit():
                return string[i]

        if is_reversed:
            string = string[::-1]
        for digit, word in numbers.items():
            if word in string:
                return digit

    first_digit = find_calibration_digit(string)
    last_digit = find_calibration_digit(string[::-1], True)
    return int("{}{}".format(first_digit, last_digit))

