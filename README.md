Advent of Code 2024 🎄
======================

→ https://adventofcode.com/2024


Directory structure
-------------------

```
├ test.sh    — Test runner for entire repository
│
├ 01         - Day 1
│ ├ input    - Individual input puzzle (not included)
│ ├ sample   - Sample puzzle from the problem statement
│ ├ expected - Expected output for puzzle solvers
│ ├ run.py   - Puzzle solver (any executable file matching `^run.`)
│ └ run.hs   - There can be more than one solver per day
│
├ 02
│ ├ input
…
```

Architecture
------------

Solutions can be written in any language. Multiple solutions may be provided for a single day, for fun. A solution must be a file whose name starts with `run.` and is executable. [Shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix)) determine how each program should be run. All programs, regardless of implementation language, must read puzzles from standard input and write the solution to standard output. Barring exceptions, the output should consist of two lines, one for each part of the puzzle.

Calling a program with `STDIN` redirection:

```sh
./run.py < sample
```

Outputs:

```
1234  # solution to Part 1
5678  # solution to Part 2
```

### Compiling from source

When solving puzzles using a language that requires a compilation step, define the targets in a Makefile specific to that day. The test runner will handle the Makefile. Source files' names should match `source.<EXT>` and target binaries should match `run.<EXT>.bin`:

```
│
├ 01          - Day 1
│ ├ ...
│ ├ source.c  - Source code for puzzle solver
│ ├ Makefile  - Makefile specifying how to build from source
│ └ run.c.bin - Binary produced by `make`
```


Testing
-------

The following assumes that, in each day's directory, there is an `input` file and an `expected` file. The `input` file is not provided in this repository and should be your own puzzle input. The `expected` file is provided for my own record, but should be overwritten with your own expected solution output.

```
# Run all tests
./test.sh

# Run for a given day
./test.sh 04
```
