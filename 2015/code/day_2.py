lines = open("2015/input/day_2.txt").readlines()

s = 0
for l in lines:
    l, w, h = l.split("x")
    l, w, h = int(l), int(w), int(h)
    s += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print(s)


print(sum(sum(sorted(int(i)*2 for i in l.split("x"))[:-1]) for l in lines) + sum(eval(l.replace("x","*")) for l in lines))

