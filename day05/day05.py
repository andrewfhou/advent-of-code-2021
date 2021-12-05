import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 05 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().splitlines()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    grid = dict()
    for line in inputs:
        a, b = line.split(' -> ')
        x1, y1 = [int(x) for x in a.split(',')]
        x2, y2 = [int(x) for x in b.split(',')]
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                if (x1, i) in grid.keys():
                    grid[(x1, i)] += 1
                else:
                    grid[(x1, i)] = 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2, = x2, x1
            for i in range(x1, x2 + 1):
                if (i, y1) in grid.keys():
                    grid[(i, y1)] += 1
                else:
                    grid[(i, y1)] = 1

    ret = 0
    for key in grid.keys():
        if grid[key] > 1:
            ret += 1
    return ret

def part_two():
    grid = dict()
    for line in inputs:
        a, b = line.split(' -> ')
        x1, y1 = [int(x) for x in a.split(',')]
        x2, y2 = [int(x) for x in b.split(',')]
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                if (x1, i) in grid.keys():
                    grid[(x1, i)] += 1
                else:
                    grid[(x1, i)] = 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2, = x2, x1
            for i in range(x1, x2 + 1):
                if (i, y1) in grid.keys():
                    grid[(i, y1)] += 1
                else:
                    grid[(i, y1)] = 1
        else:
            for i in range(0, abs(x2 - x1) + 1):
                x = 0
                y = 0

                if x1 < x2:
                    x = x1 + i
                else:
                    x = x1 - i
                if y1 < y2:
                    y = y1 + i
                else:
                    y = y1 - i
                if (x, y) in grid.keys():
                    grid[(x, y)] += 1
                else:
                    grid[(x, y)] = 1

    ret = 0
    for key in grid.keys():
        if grid[key] > 1:
            ret += 1
    return ret

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

