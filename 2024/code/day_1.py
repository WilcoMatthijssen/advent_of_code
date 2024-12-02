file_input = [var.split() for var in open("2024/input/day_1.txt").readlines()]
lst1, lst2 = zip(*file_input)


cool = list(zip(sorted([int(i) for i in lst1]), sorted([int(i) for i in lst2])))
print(sum(abs(x-y) for x, y in cool))


lst1, lst2 = zip(*cool)
print(sum(i * lst2.count(i) for i in lst1))



