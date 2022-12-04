sorted_totals = sorted(eval(open("2022/day_1/day_1_input.txt").read().replace('\n','+').replace("++", ',')))

print(f"highest: {sorted_totals[-1]}, highest three: {sum(sorted_totals[-3:])}")
