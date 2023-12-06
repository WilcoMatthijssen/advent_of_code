input_file = open("2022/input/day_5.txt").readlines()

rules = map(lambda string: eval(string.replace("move", "").replace("from", ",").replace("to", ",")), input_file[10:])
crates1 = [""] + [*map(lambda row: "".join(row).replace(" ", "")[::-1], [*zip(*input_file[:8])][1::4])]
crates2 = [*crates1]

for amount, src, dest in rules:
    crates1[dest] += crates1[src][ -amount:][::-1]
    crates1[src ]  = crates1[src][:-amount ]
    
    crates2[dest] += crates2[src][ -amount:]
    crates2[src ]  = crates2[src][:-amount ]

print(''.join(x[-1] for x in crates1 if x))
print(''.join(x[-1] for x in crates2 if x))
