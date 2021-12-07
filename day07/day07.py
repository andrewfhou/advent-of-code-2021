import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 07 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = [int(x) for x in file.read().strip().split(',')]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    minx = min(inputs)
    maxx = max(inputs)
    best = 10000000000000000000
    for i in range(minx, maxx):
        cost = sum(abs(i - j) for j in inputs)
        best = min(cost, best)
    return best

def f(n):
    return (n * (n + 1)) // 2
def part_two():
    minx = min(inputs)
    maxx = max(inputs)
    best = 10000000000000000000
    for i in range(minx, maxx):
        cost = sum(f(abs(i - j)) for j in inputs)
        best = min(cost, best)
    return best

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

