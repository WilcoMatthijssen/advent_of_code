
from functools import reduce 
import operator
import re

a = re.split("[(TimeDstanc:)\s\n]+",open("2023/input/day_6.txt").read())[1:]
print(reduce(operator.mul,[sum(i*(t-i)>d for i in range(t)) for t, d in zip(map(int,a[:len(a)//2]),map(int,a[len(a)//2:]))],1))
print(sum(i*(int("".join(a[:len(a)//2]))-i)>int("".join(a[len(a)//2:])) for i in range(int("".join(a[:len(a)//2])))))

