from itertools import product

instructions = []
with open('input.txt') as f:
    instructions = f.read().replace(',', ' ').splitlines()

def Direct(string):
    for i,v in enumerate(string):
        if v.isdigit():
            direction = string[:i-1]
            break
    direction = dict(direction = direction)
    return direction


def Positions(string):
    pos = []
    pos_names = ['start_x', 'start_y', 'end_x', 'end_y']
    for s in string.split():
        if s.isdigit():
            pos.append(int(s))
    pos = dict(zip(pos_names, pos))
    return pos

instructions_dict = []
for i,v in enumerate(instructions):
    instructions_dict.append({**Direct(v), **Positions(v)})

matrix = {}
x = tuple(range(1000))
for ele in product(x,x):
    matrix[ele] = 0

for instruction in instructions_dict:
    x = tuple(range(instruction['start_x'], instruction['end_x']+1))
    y = tuple(range(instruction['start_y'], instruction['end_y']+1))
    if instruction['direction'] == 'turn on':
        for position in product(x, y):
            matrix[position] += 1
    elif instruction['direction'] == 'turn off':
        for position in product(x, y):
            if matrix[position] > 0:
                matrix[position] -= 1
            elif matrix[position] == 0:
                matrix[position] = 0
    elif instruction['direction'] == 'toggle':
        for position in product(x,y):
            matrix[position] += 2

print(sum(matrix.values()))