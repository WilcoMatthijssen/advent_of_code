
import re
import itertools
import math


a = {key:(l,r) for key, l, r in (re.findall("[A-Z]+", line) for line in list(open("2023/input/day_8.txt"))[2:])}
search = lambda curr, end: next(i+1 for i, c in enumerate(itertools.cycle(list(open("2023/input/day_8.txt"))[0].strip())) if (curr := a[curr][c =="R"]).endswith(end))
print(search("AAA", "ZZZ"))  #part 1
print(math.lcm(*(search(start, "Z") for start in a if start.endswith('A')))) # part 2

