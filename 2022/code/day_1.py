sorted_totals = sorted(eval(open("2022/input/day_1.txt").read().replace('\n','+').replace("++", ',')))

print(sorted_totals[-1])
print(sum(sorted_totals[-3:]))
