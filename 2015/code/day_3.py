file = open("2015/input/day_3.txt").read()

x = 0
y = 0

positions = {"0,0"}

for c in file:
    if c == "<":
        x -= 1
    elif c == ">":
        x += 1
    elif c == "^":
        y += 1
    elif c == "v":
        y -= 1
    positions |={f"{x},{y}"}

print(len(positions))
x = 0
y = 0

xx = 0
yy = 0

positions = {"0,0"}

for i, c in enumerate(file):
    if i%2:
        if c == "<":
            x -= 1
        elif c == ">":
            x += 1
        elif c == "^":
            y += 1
        elif c == "v":
            y -= 1
        positions |={f"{x},{y}"}
    else:
        if c == "<":
            xx -= 1
        elif c == ">":
            xx += 1
        elif c == "^":
            yy += 1
        elif c == "v":
            yy -= 1
        positions |={f"{xx},{yy}"}




print(len(positions))


