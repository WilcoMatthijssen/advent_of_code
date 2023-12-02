import pathlib
import os

file = pathlib.Path("2021/input/day_4.txt").read_text();
linesep = '\n'
bingo_moves = eval(f"[{file.split(linesep)[0]}]")

# print(file.split(linesep)[1:])

boards = file[file.find('\n\n')+1:]

boards = boards.replace(' ', ',')
boards = boards.replace(',,', ',')

boards = boards.replace('\n', '],[')

print(boards)
