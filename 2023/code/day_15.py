file_input = open("2023/input/day_15.txt").read()
from functools import reduce

hashish = lambda curr, c: ((ord(c)+curr)*17) % 256
weed = lambda string: reduce(hashish, string, 0)
print(sum(weed(piece) for piece in file_input.split(',')))


l = {x:{} for x in range(256)}
for piece in file_input.split(','):
    if '-' not in piece:
        chars, i = piece.split('=')
        l[weed(chars)][chars] = i
    else:
        l[weed(piece.removesuffix("-"))].pop(piece.removesuffix("-"), None)

s = 0
for i, box in l.items():
    for mul, n in enumerate(box.values(), start=1):
        s += (i+1)*mul* int(n)
print(s)