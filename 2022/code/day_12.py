file = open("2022/input/day_12.txt").read().splitlines()
for line in file:
    line.replace("\n", "")
from string import ascii_lowercase


conv = dict(zip(ascii_lowercase, range(1, 27))) | {"S":0, "E": 27}
field = {(i,j): conv[c] for i, line in enumerate(file) for j, c in enumerate(line)}
start = next((i, line.index("S")) for i, line in enumerate(file) if "S" in line)
print(start)



visited = {}
q = [(start, 0)]

while len(q):
    (x, y), steps = q.pop(0)
    visited |= {(x, y): steps}

    if field[x, y] == 27:
        print(steps)
        break
    for pos in ((x-1 ,y), (x+1 ,y), (x ,y-1), (x ,y+1)):
        yes = all(val[0] != pos for val in q)
        if (pos in field) and (pos not in visited) and yes and (field[x,y]+2 > field[pos]):
            q.append((pos,steps+1 ))

        

