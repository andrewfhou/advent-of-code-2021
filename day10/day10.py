import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 10 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().splitlines()
print('%.6fms\n' % (CURR_MS() - START_READ))

corr_scores = { ')' : 3,
           ']' : 57,
           '}' : 1197,
           '>' : 25137 }

matches = { '(' : ')',
            '[' : ']',
            '{' : '}',
            '<' : '>' }

incomplete = list()

def part_one():
    score = 0
    for line in inputs:
        corrupt = False
        stack = list()
        for c in line:
            if c in ('(', '[', '{', '<'):
                stack.append(c)
            else:
                x = stack.pop()
                if matches[x] != c:
                    corrupt = True
                    score += corr_scores[c]
        if not corrupt:
            incomplete.append(line)
    return score

inc_scores = { '(' : 1,
               '[' : 2,
               '{' : 3,
               '<' : 4 }

def part_two():
    scores = list()
    for line in incomplete:
        score = 0
        stack = list()
        for c in line:
            if c in ('(', '[', '{', '<'):
                stack.append(c)
            else:
                x = stack.pop()
        while len(stack) > 0:
            c = stack.pop()
            score *= 5
            score += inc_scores[c]
        scores.append(score)
    return sorted(scores)[(int) ((len(scores) - 1) / 2) ]

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

