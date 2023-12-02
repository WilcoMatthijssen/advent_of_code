moves =open("2021/input/day_2.txt").read().splitlines()


result = lambda ch: sum(int(move[-1]) for move in moves if move[0] == ch)
print(result("f") * (result("d") - result("u")))



# horizontal = 0
# depth = 0
# for move in moves:
#     if move.startswith("up"):
#         depth -= int(move[-1])
#     elif move.startswith("down"):
#         depth += int(move[-1])
#     else:# move.startswith("forward")
#         horizontal += int(move[-1])

# print(horizontal * depth)


# aim = 0
# horizontal = 0
# depth = 0
# for move in moves:
    # if move[0] == "d":
    #     aim += int(move[-1])
    # elif move[0] == "u":
    #     aim -= int(move[-1])
    # else:# move.startswith("forward")
    #     horizontal += int(move[-1])
    #     depth += aim * int(move[-1])
# print(horizontal * depth)



aim = horizontal = depth =0
for move in moves:
    aim += int(move[-1]) * {'u':-1, 'f':0, 'd': 1}[move[0]]
    if move[0] == "f":
        horizontal += int(move[-1])
        depth += aim * int(move[-1])

print(horizontal * depth)


