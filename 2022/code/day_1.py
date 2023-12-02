sorted_totals = sorted(eval(open("2022/input/day_1.txt").read().replace('\n','+').replace("++", ',')))

print(f"highest: {sorted_totals[-1]}, highest three: {sum(sorted_totals[-3:])}")
