import sys
import math

def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    # Do extra parsing here if you need
    # eg. puzzle_input = puzzle_input[0].split(" ")
    return puzzle_input


def part1(puzzle_input):
    ans = 0
    for x in puzzle_input:
        ans += math.floor(int(x) // 3) - 2
    return ans


def part2(puzzle_input):
    ans = 0
    for x in puzzle_input:
        ans += rec((int(x)))
    return ans

def rec(num):
    ans = math.floor(int(num) // 3) - 2
    if ans <= 0:
        return 0

    return ans + rec(ans)

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))