file_input = [list(map(int, i.split())) for i in open("2024/input/day_2.txt").readlines()]

remove_nth_item = lambda lst, n: lst[:n] + lst[n+1:]
isgud = lambda l: l<={1,2,3} or l<={-1,-2,-3}
first = lambda line: sum(isgud({a-b for a,b in zip(l, l[1:])}) for l in line)
second = lambda line: sum(first([l[:i] + l[i+1:] for i in range(len(l))]) != 0 for l in line)


print(first(file_input))
print(second(file_input))
