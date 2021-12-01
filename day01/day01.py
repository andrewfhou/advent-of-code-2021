import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 01 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = [int(n) for n in file.read().strip().split()]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    return sum(b > a for a, b in zip(inputs, inputs[1:]))

def part_two():
    wins = [sum(w) for w in zip(inputs, inputs[1:], inputs[2:])]
    return sum(b > a for a, b in zip(wins, wins[1:]))

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

