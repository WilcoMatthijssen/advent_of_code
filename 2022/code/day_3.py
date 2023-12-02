file_input = open("2022/input/day_3.txt").read().splitlines()

value = lambda x: ord(x) -(38  if x.isupper() else 96)

conv1= lambda x: value(*set(x[:len(x)//2]) & ( set(x[len(x)//2:])))
print(sum(map(conv1, file_input)))


conv2 = lambda x: value(*(set(file_input[x]) & set(file_input[x+1]) & set(file_input[x+2])))
print(sum(map(conv2, range(0,  len(file_input), 3))))
