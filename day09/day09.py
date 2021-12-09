import time
from collections import Counter

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 09 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = [[int(c) for c in x] for x in file.read().strip().split()]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    ret = 0
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if i > 0 and inputs[i][j] >= inputs[i - 1][j]:
                continue
            if i < len(inputs) - 1 and inputs[i][j] >= inputs[i + 1][j]:
                continue
            if j > 0 and inputs[i][j] >= inputs[i][j - 1]:
                continue
            if j < len(inputs[0]) - 1 and inputs[i][j] >= inputs[i][j + 1]:
                continue
            ret += inputs[i][j] + 1
    return ret

def find_basin(i, j):
    down = None
    for (di, dj) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if di in range(len(inputs)) and dj in range(len(inputs[0])):
            if inputs[i][j] > inputs[di][dj]:
                down = (di, dj)
    if down is None:
        return (i, j)
    return find_basin(*down)

def part_two():
    basins = list()
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if inputs[i][j] != 9:
                basins.append(find_basin(i, j))
    ret = 1
    for basin, common in Counter(basins).most_common(3):
        ret *= common
    return ret

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

