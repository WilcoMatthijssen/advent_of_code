import re


file_input = open("2023/input/day_1.txt").read()

get_stuff = lambda text: sum(int(line[0]+line[-1]) for line in re.sub("[a-z]", "", text).split('\n'))

print(get_stuff(file_input))


print(get_stuff(file_input
    .replace("one",   "o1e").replace("two",   "t2o").replace("three", "t3e")
    .replace("four",  "f4r").replace("five",  "f5e").replace("six",   "s6x")
    .replace("seven", "s7n").replace("eight", "e8t").replace("nine",  "n9e")
    ))


