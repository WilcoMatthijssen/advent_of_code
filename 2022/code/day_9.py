rope = [0] * 10
seen = [{x} for x in rope]
dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

for line in open("2022/input/day_9.txt"):
    for _ in range(int(line[2:])):
        rope[0] += dirs[line[0]]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += sign(dist)
                seen[i].add(rope[i])

print(len(seen[1]), len(seen[-1]))