# numbers = "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"
file_input = tuple(open("2021/input/day_3.txt"))
from collections import Counter


# gamma = "".join("1" if "".join(num[i] for num in numbers).count("1") > (len(numbers) // 2) else "0" for i in range(len(numbers[0])))

# gamma = "".join(str(int(sum(int(num[i]) for num in numbers) > (len(numbers) // 2))) for i in range(len(numbers[0])))

# gamma = "".join(Counter(num[i] for num in file_input).most_common(1)[0][0] for i in range(len(file_input[0])))


gamma = "".join(Counter(col).most_common(1)[0][0] for col in zip(*file_input))
print(int(gamma,2)* int("".join("1" if bit == "0" else "0" for bit in gamma),2))


# def common(diag, i):
#     return int(sum(n >> i & 1 for n in diag) / len(diag) + .5)

# def gamma(diag, width):
#     return sum(common(diag, i) << i for i in range(width))

# def epsilon(diag, width):
#     return sum((1 - common(diag, i)) << i for i in range(width))

# def rating(diag, width, most_common):
#     i = width - 1
#     while len(diag) > 1:
#         bit = common(diag, i) ^ most_common
#         diag = [n for n in diag if n >> i & 1 == bit]
#         i -= 1
#     return diag[0]


# diag = [int(line, 2) for line in open("2021/day_3/day_3_input.txt")]

# width = max(n.bit_length() for n in diag)
# print(gamma(diag, width) * epsilon(diag, width))
# print(rating(diag, width, True) * rating(diag, width, False))


# print( list(zip(*file_input))[0])


def part2(data, p):
    for n in range(12):
        counts = Counter(list(zip(*data))[n]).most_common()
        c = str(1 + p) if (len(counts) == 2 and counts[0][1] == counts[1][1]) else counts[p][0]
        data = list(filter(lambda x: x[n]==c, data))
    return int(''.join(data[0]), 2)


print('part2:', part2(file_input, 0) * part2(file_input, -1))
