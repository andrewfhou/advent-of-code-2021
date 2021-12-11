import time
import itertools

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 11 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    lines = file.read().splitlines()
    inputs = [[int(x) for x in line] for line in lines]
print('%.6fms\n' % (CURR_MS() - START_READ))

def neighbors(p):
    for d in itertools.product(range(-1, 2), repeat=2):
        if d == (0, 0):
            continue
        x = p[0] + d[0]
        y = p[1] + d[1]
        if (0 <= x < len(inputs[0])) and (0 <= y < len(inputs)):
            yield (x, y)

def step():
    seen = set()
    flashes = list()
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            inputs[i][j] += 1
            if inputs[i][j] > 9 and (i, j) not in seen:
                flashes.append((i, j))
                seen.add((i, j))
    while flashes:
        pos = flashes.pop(0)
        for i, j in neighbors(pos):
            try:
                if (i, j) not in seen:
                    inputs[i][j] += 1
                    if inputs[i][j] > 9:
                        flashes.append((i, j))
                        seen.add((i, j))
            except: pass
    for i, j in list(seen):
        inputs[i][j] = 0
    return len(seen), all(x == 0 for x in itertools.chain(*inputs))

def part_one():
    return sum([step()[0] for i in range(100)])

def part_two():
    steps = 101
    while True:
        if step()[1]:
            return steps
        steps += 1

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

