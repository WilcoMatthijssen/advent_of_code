import re

file_input = open("2023/input/day_2.txt").readlines()
get_max = lambda color, line: max(map(int, re.findall(f"([0-9]+) {color}",line)))
is_possible = lambda line: all([get_max("r",line)<13, get_max("b",line)<15, get_max("g",line)<14])
print(sum(int(re.findall(r"Game ([0-9]+):",l)[0]) for l in file_input if is_possible(l)))
print(sum(get_max("r",l) * get_max("b",l) * get_max("g",l) for l in file_input))

