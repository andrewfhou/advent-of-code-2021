import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 03 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE...',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    gamma = ''
    for i in range(len(inputs[0])):
        bits = ''.join(x[i] for x in inputs)
        if bits.count('1') > bits.count('0'):
            gamma += '1'
        else:
            gamma += '0'
    return int(gamma, 2) * int(''.join('1' if x == '0' else '0' for x in gamma), 2)

def part_two():
    l = len(inputs[0])

    oxy = set(inputs)
    for i in range(l):
        bits = ''.join(x[i] for x in oxy)
        if bits.count('0') <= bits.count('1'):
            bit = '0'
        else:
            bit = '1'
        oxy = oxy - set(x for x in oxy if x[i] == bit)
        if len(oxy) == 1:
            oxy = max(oxy)
            break

    co2 = set(inputs)
    for i in range(l):
        bits = ''.join(x[i] for x in co2)
        if bits.count('0') > bits.count('1'):
            bit = '0'
        else:
            bit = '1'
        co2 = co2 - set(x for x in co2 if x[i] == bit)
        if len(co2) == 1:
            co2 = max(co2)
            break

    return int(oxy, 2) * int(co2, 2)

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

