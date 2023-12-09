file_input = [list(map(int, line.split())) for line in open("2023/input/day_9.txt")]
do_stuff = lambda arr: do_stuff(arr+[[a-b for a,b in zip(arr[-1][1:], arr[-1])]]) if any(arr[-1]) else arr
print(sum(sum(a[-1] for a in do_stuff([arr])) for arr in file_input))
print(sum(sum(a[-1] for a in do_stuff([list(reversed(arr))])) for arr in file_input))

