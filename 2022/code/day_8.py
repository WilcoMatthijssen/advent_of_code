file_input =  [list(col) for col in open("2022/input/day_8.txt").read().split("\n")]
from functools import reduce



get_visible_row = lambda i, ranger: [*reduce(lambda old, new: old + ([(i,new)] if file_input[i][old[-1][1]] < file_input[i][new] else []), ranger, [(i,ranger[0])])]
get_joepie = lambda ranger: sum([*map(lambda i: get_visible_row(i, ranger), ranger)], [])


rangeboi = [*range(len(file_input))]
positions = get_joepie(rangeboi)
positions += get_joepie(rangeboi[::-1])

file_input = [*zip(*file_input)]

positions += [(j, i) for i, j in get_joepie(rangeboi)]
positions += [(j, i) for i, j in get_joepie(rangeboi[::-1])]


print(len(set(positions)))










# from collections import namedtuple
# class Tree(namedtuple('Tree', 'x y h')): pass

# forest = open("2022/day_8/day_8_input.txt").read().splitlines()
# forest = {(x,y):Tree(x,y,h) for y,row in enumerate(forest) for x,h in enumerate(row)}
# H,W = max(forest)

# for t in forest.values():
#     t.v = (
#         all(t.h>forest[x,t.y].h for x in range(0,t.x)) or
#         all(t.h>forest[x,t.y].h for x in range(t.x+1,W+1)) or
#         all(t.h>forest[t.x,y].h for y in range(0,t.y)) or
#         all(t.h>forest[t.x,y].h for y in range(t.y+1,H+1)))
#     t.s = (
#         next((l for l,y in enumerate(range(0,t.y)[::-1],1) if t.h<=forest[t.x,y].h),t.y) *
#         next((l for l,y in enumerate(range(t.y+1,H+1),1) if t.h<=forest[t.x,y].h),H-t.y) *
#         next((l for l,x in enumerate(range(0,t.x)[::-1],1) if t.h<=forest[x,t.y].h),t.x) *
#         next((l for l,x in enumerate(range(t.x+1,W+1),1) if t.h<=forest[x,t.y].h),W-t.x))

# print('part1', sum(t.v for t in forest.values()))
# print('part2', max(forest.values(),key=lambda t:t.s).s)


# def loopie(ranger):
#     found_positions = []
#     for i in [*ranger]:
#         lowest = -1
#         for j in [*ranger]:
#             num = int(file_input[i][j])
#             if num > lowest:
#                 found_positions += [(i,j)]
#                 lowest = num
#     return found_positions