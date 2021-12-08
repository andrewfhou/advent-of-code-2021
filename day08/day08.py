import time
import itertools

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 08 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open('input.txt') as file:
    inputs = file.read().splitlines()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    ret = 0
    for line in inputs:
        out = line.split(' | ')[1].split(' ')
        for digit in out:
            l = len(digit)
            if len(digit) in (2,3,4,7):
                ret += 1
    return ret

def part_two():
    m = {'acedgfb':8, 'cdfbe':5, 'gcdfa':2, 'fbcad':3, 'dab':7, 'cefabd':9,
             'cdfgeb':6, 'eafb':4, 'cagedb':0, 'ab':1}
    m = {''.join(sorted(x)) : v for x, v in m.items()}

    ret = 0
    for line in inputs:
        a, b = line.split(' | ')
        a = a.split(' ')
        b = b.split(' ')
        for perm in itertools.permutations('abcdefg'):
            perm_map = {a : b for a, b in zip(perm, 'abcdefg')}
            an = [''.join(perm_map[c] for c in x) for x in a]
            bn = [''.join(perm_map[c] for c in x) for x in b]
            if all(''.join(sorted(x)) in m for x in an):
                bn = [''.join(sorted(x)) for x in bn]
                ret += int(''.join(str(m[x]) for x in bn))
                break
    return ret

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

