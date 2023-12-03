import re
import itertools

loc = {(y, x):[] for y, row in enumerate(list(open("2023/input/day_3.txt"))) for x, c in enumerate(row) if c in '/*#%@=-&$+'};[(loc[pos].append(int(x.group()))) for y, row in enumerate(list(open("2023/input/day_3.txt"))) for x in re.finditer('\d+', row) for pos in itertools.product((y-1, y, y+1), range(x.start()-1, x.end()+1)) & loc.keys()]

print(sum(map(sum, loc.values())))
print(sum(p[0]*p[1] for p in loc.values() if len(p)==2))

