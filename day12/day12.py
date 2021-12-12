import time
from collections import defaultdict, Counter

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 12 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split('\n')
    edges = defaultdict(list)
    for line in inputs:
        s, t = line.split('-')
        edges[s].append(t)
        edges[t].append(s)
print('%.6fms\n' % (CURR_MS() - START_READ))

def solve(edges, curr, prev, p2):
    if curr.islower():
        prev = prev + [curr]
    if curr == 'end':
        return 1
    total = 0
    for adj in edges[curr]:
        if (adj not in prev) or \
           (p2 and max(Counter(prev).values()) == 1 and adj != 'start'):
            total += solve(edges, adj, prev, p2)
    return total

def part_one():
    return solve(edges, 'start', [], False)

def part_two():
    return solve(edges, 'start', [], True)

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

