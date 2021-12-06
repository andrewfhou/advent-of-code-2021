import time
import collections

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 06 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = [int(x) for x in file.read().strip().split(',')]
print('%.6fms\n' % (CURR_MS() - START_READ))

def get_fish(days):
    timers = collections.Counter(inputs)
    for _ in range(days):
        born = timers[0]

        for i in range(8):
            timers[i] = timers[i + 1]
        timers[8] = born
        timers[6] += born
    return sum(timers.values())

def part_one():
    return get_fish(80)

def part_two():
    return get_fish(256)

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

