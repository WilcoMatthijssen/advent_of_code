import math
file_input = open("2022/input/day_11.txt").read().splitlines()


monkOp = [line[19:] for line in file_input[2::7]]
monkTest = [int(line[21:]) for line in file_input[3::7]]
monkCondiments = [[int(a[29:]), int(b[30:])] for a, b in zip(file_input[4::7], file_input[5::7])]

def momkey(part):
    monkInspections = [0,0,0,0, 0,0,0,0]
    monkItems = [*map(lambda line: eval(f'[{line.split(": ")[1]}]'), file_input[1::7])]
    for i in list(range(8)) * part:
        for old in monkItems[i]:
            old = eval(f"({monkOp[i]}) {'// 3' if part == 20 else '% math.prod(monkTest)'}")
            monkItems[monkCondiments[i][old % monkTest[i] != 0]].append(old)
            monkInspections[i] += 1
        monkItems[i] = []
    return sorted(monkInspections)[-1]*sorted(monkInspections)[-2]

print(momkey(20))
print(momkey(10000))

