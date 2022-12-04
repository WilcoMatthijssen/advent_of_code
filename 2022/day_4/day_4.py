

# part1 = lambda x: (int(x[0]) <= int(x[2]) and int(x[1]) >= (int(x[3]))) or (int(x[0]) >= int(x[2]) and int(x[1]) <= int(x[3]))
# print(sum(map(lambda z: part1(z.replace(',', '-').split('-')), open("2022/day_4/day_4_input.txt"))))


# part2 = lambda x: (set(range(int(x[0]), int(x[1])+1)) & set(range(int(x[2]), int(x[3])+1))) != set()
# print(sum(map(lambda z: part2(z.replace(',', '-').split('-')), open("2022/day_4/day_4_input.txt"))))





# def apply_set_op(string, op):
#     nums = [*map(int,string.replace(',', '-').split('-'))]
#     return op(set(range(nums[0], nums[1]+1)), set(range(nums[2], nums[3]+1)))

# print(sum(map(lambda line: apply_set_op(line, set.issubset) or apply_set_op(line, set.issuperset), open("2022/day_4/day_4_input.txt") )))
# print(sum(map(lambda line: any(apply_set_op(line, set.intersection)), open("2022/day_4/day_4_input.txt") )))





make_set = lambda a,b,c,d: (set(range(a, b+1)), set(range(c, d+1)))
input_set = list(map(lambda string: make_set(*map(int,string.replace(',', '-').split('-'))), open("2022/day_4/day_4_input.txt")))


print(sum(map(lambda sets: sets[0] <= sets[1] or sets[1] <= sets[0], input_set)))

print(sum(map(lambda sets: any(sets[0] & sets[1]), input_set)))



