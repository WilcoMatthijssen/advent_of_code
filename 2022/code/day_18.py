file_input = {*map(eval, open("2022/input/day_18.txt"))}

neighbors = lambda x,y,z: {(x+1,y,z),(x,y+1,z),(x,y,z+1),(x-1,y,z),(x,y-1,z),(x,y,z-1)}

print(sum((neighbor not in file_input) for pos in file_input for neighbor in neighbors(*pos)))





seen = set()
todo = [(-1,-1,-1)]

while todo:
    here = todo.pop()
    todo += [s for s in (neighbors(*here) - file_input - seen) if all(-1<=c<=25 for c in s)]
    seen |= {here}

print(sum((s in seen) for c in file_input for s in neighbors(*c)))

