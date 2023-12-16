file_input = tuple(tuple(string) for string in open("2023/input/day_14.txt").read().split('\n'))

from functools import cache

@cache
def proces(board):
    board = [list(row) for row in board]
    moved = True
    while(moved):
        moved = False
        for row in range(1, len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'O' and board[row-1][col] == '.':
                    board[row][col] = '.'
                    board[row-1][col] = 'O'
                    moved = True
    return tuple(tuple(row) for row in board)

@cache
def rotat(board):
    return tuple((row[::-1]) for row in zip(*board))

part_one = proces(file_input)
print(sum(row.count("O") * i for i, row in enumerate(reversed(part_one), start=1)))


#       N
#   W       E
#       S

@cache
def cycle10k(board):
    for _ in range(4*10000):
        board = proces(board)   
        board = rotat(board)
    return board

for _ in range(100000):
    file_input = cycle10k(file_input)

print(sum(row.count("O") * i for i, row in enumerate(reversed(file_input), start=1)))

