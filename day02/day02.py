import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 02 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    hor = 0
    dep = 0
    for line in inputs:
        if line == '': break
        mov, val = line.split()
        val = int(val)
        if mov == 'forward':
            hor += val
        elif mov == 'down':
            dep += val
        elif mov == 'up':
            dep -= val
    return hor * dep

def part_two():
    hor = 0
    dep = 0
    aim = 0
    for line in inputs:
        if line == '': break
        mov, val = line.split()
        val = int(val)
        if mov == 'forward':
            hor += val
            dep += aim * val
        elif mov == 'down':
            aim += val
        elif mov == 'up':
            aim -= val
        else:
            print('oops')
    return hor * dep

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

