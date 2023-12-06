input_file = open("2022/input/day_6.txt").read()

# for i in range(len(input_file)):
#     if len(set(input_file[i-4:i])) == 4:
#         print(i)
#         break

# for i in range(len(input_file)):
#     if len(set(input_file[i-14:i])) == 14:
#         print(i)
#         break

print(next(i for i in range(len(input_file)) if len(set(input_file[i-4:i] )) == 4 ))
print(next(i for i in range(len(input_file)) if len(set(input_file[i-14:i])) == 14))
