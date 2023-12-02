file_input = open("2022/input/day_10.txt")


from functools import reduce
xs = [*reduce(lambda old, new: old + [old[-1]] + ([old[-1] + int(new[5:])] if new[5:] else []), file_input, [1])]
    
# Part 1
print(sum(i * xs[i - 1] for i in (20, 60, 100, 140, 180, 220)))
