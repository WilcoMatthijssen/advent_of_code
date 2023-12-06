from collections import defaultdict
from itertools import accumulate


# dirs = defaultdict(int)

# for line in open("2022/day_7/day_7_input.txt"):
#     match line.split():
#         case '$', 'cd', '/': curr = ['']
#         case '$', 'cd', '..': curr.pop()
#         case '$', 'cd', x: curr.append(x+'/')
#         case '$', 'ls': pass
#         case 'dir', _: pass
#         case size, _:
#             for p in accumulate(curr):
#                 dirs[p] += int(size)

# print(dirs)
# print(sum(s for s in dirs.values() if s <= 100_000),
#       min(s for s in dirs.values() if s >= dirs[''] - 40_000_000))

lines = [*filter(lambda line: not line.startswith("dir") and not line.startswith("$ ls"), open("2022/input/day_7.txt"))]
dirs = defaultdict(int)

for line in lines:
    if line.startswith("$ cd /"):# line == "$ cd /":
        curr = ['']
    elif line.startswith("$ cd .."):#line == "$ cd ..":
        curr.pop()
    elif line.startswith("$ cd"):
        curr.append(line.split()[-1]+'/')
    else:
        for p in accumulate(curr):
            dirs[p] += int(line.split()[0])
print(sum(s for s in dirs.values() if s <= 100_000))
print(min(s for s in dirs.values() if s >= dirs[''] - 40_000_000))