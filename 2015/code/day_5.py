file = open("2015/input/day_5.txt").readlines()



is_gud = lambda line: sum(line.count(c) for c in "aeiou") > 2 and all(c not in line for c in ["ab", "cd", "pq", "xy"]) and any(x == y for x, y in zip(line[1:], line))
print(sum(is_gud(line) for line in file))


# if sum(1 for c in "aeiou" if c in "xazgov") >= 3:
#     print('YEE')