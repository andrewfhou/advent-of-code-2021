import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 04 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
file = open('input.txt')
nums = [int(x) for x in file.readline().strip().split(",")]
boards = [
    [[int(i) for i in l.split()] for l in x.splitlines()]
    for x in file.read().strip().split("\n\n")
]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    for n in nums:
        for b in boards:
            for i, row in enumerate(b):
                for j, cell in enumerate(row):
                    if cell == n:
                        b[i][j] = None
            for row in b:
                if all(x is None for x in row):
                    score = sum(i for r in b for i in r if i is not None)
                    return score * n
            for col in zip(*b):
                if all(x is None for x in col):
                    score = sum(i for r in b for i in r if i is not None)
                    return score * n

def part_two():
    wins = []
    win = None

    for n in nums:
        if sum(x not in wins for x in boards) == 1:
            win = next(i for i, x in enumerate(boards) if x not in wins)
        for bdx, b in enumerate(boards):
            for i, row in enumerate(b):
                for j, cell in enumerate(row):
                    if cell == n:
                        b[i][j] = None
            for row in b:
                if all(x is None for x in row):
                    if bdx == win:
                        score = sum(i for r in b for i in r if i is not None)
                        return score * n
                    wins.append(b)
            for col in zip(*b):
                if all(x is None for x in col):
                    if bdx == win:
                        score = sum(i for r in b for i in r if i is not None)
                        return score * n
                    wins.append(b)

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

