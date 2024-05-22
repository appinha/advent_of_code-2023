<h1 align="center">
	🌟 Advent of Code 2023 🎄
</h1>

<p align="center">
	<i>My solutions for <b>Advent of Code 2023</b>.</i>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/appinha/advent_of_code-2023?color=blueviolet" />
	<img alt="Number of lines of code" src="https://img.shields.io/tokei/lines/github/appinha/advent_of_code-2023?color=blueviolet" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/appinha/advent_of_code-2023?color=blue" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/appinha/advent_of_code-2023?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/appinha/advent_of_code-2023?color=brightgreen" />
</p>

<h3 align="center">
	<a href="#-what-is-advent-of-code">What is <i>Advent of Code</i>?</a>
	<span> · </span>
	<a href="#-contents">Contents</a>
	<span> · </span>
	<a href="#%EF%B8%8F-usage">Usage</a>
	<span> · </span>
	<a href="#%EF%B8%8F-table-of-puzzles">Table of puzzles</a>
</h3>

---

## 🌟 What is _Advent of Code_?

    🚀 TLDR: an online event where a two-part programming puzzle is released each day from Dec 1st to the 25th.

[Advent of Code](http://adventofcode.com) is an online event created by [Eric Wastl](http://was.tl/). In his words:

> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

Source: https://adventofcode.com/about

## 📑 Contents

❗️ **Important:** This repo was created from the template [advent_of_code-template](https://github.com/appinha/advent_of_code-template), please refer to its documentation for more information.

My solutions for the puzzles are available in the folder [📁 my_solutions](my_solutions) and are organized into subfolders for each day of the event.

Inside each subfolder, the following files can be found:

- `input_test.txt` - contains input from tests given in the puzzle.
- `input.txt` - contains my personal input for the puzzle.
- `main.py` - Python code for solving the puzzle.
- `README.md` - contains a tldr of the puzzle.
- `solutions.txt` - contains the solutions to my inputs for the puzzle.

## 🛠️ Usage

### Requirements

- `Python 3.10`
- `termcolor`
- `make` (for running `Makefile`)

### Instructions

#### Solve puzzle for a certain day:

```shell
$ make d=1
```

#### Solve puzzle for a certain day and part:

```shell
$ make d=8 p=1
```

```shell
$ make d=8 p=2
```

#### Solve puzzle for testing input:

```shell
$ make test d=12
```

```shell
$ make test d=12 p=1
```

## 🗓️ Table of puzzles

| DAY							| PUZZLE TITLE	| PUZZLE SUMMARY
| :-:							| :-						| :-
| [📁 01](my_solutions/day_01)	| **Trebuchet?!**		| 📃 **Input:** the calibration document (a list of strings).<br />⭐ **Part One:** find the sum of all of the calibration values only considering the digits in the strings. <br />⭐ **Part Two:** find the sum of all of the calibration values considering both digits and numbers written in full.
| [📁 02](my_solutions/day_02)	| **Cube Conundrum**		| 📃 **Input:** information on the games played.<br />⭐ **Part One:** find the sum of the IDs of the games that would have been possible given the requirements. <br />⭐ **Part Two:** find the sum of the power of the minimum set of each game.
| [📁 03](my_solutions/day_03)	| **Gear Ratios**		| 📃 **Input:** the engine schematic, a visual representation of the engine.<br />⭐ **Part One:** find the sum of all of the part numbers in the engine schematic. <br />⭐ **Part Two:** find the sum of all of the gear ratios in the engine schematic.
| [📁 04](my_solutions/day_04)	| **Scratchcards**		| 📃 **Input:** a table with the scratchchards info (two lists of integer numbers).<br />⭐ **Part One:** find how many points are the scratchchards worth in total. <br />⭐ **Part Two:** find how many total scratchcards do you end up with.
| [📁 05](my_solutions/day_05)	| **If You Give A Seed A Fertilizer**		| 📃 **Input:** the latest Island Island Almanac.<br />⭐ **Part One:** find the lowest location number that corresponds to any of the initial seed numbers. <br />⭐ **Part Two:** same as part one, but with seed ranges.
