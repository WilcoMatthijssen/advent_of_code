import hashlib
file = open("2015/input/day_4.txt").read()
l = len(file)

for i in range(10000000):
   if hashlib.md5(f"{file}{i}".encode()).hexdigest().startswith("00000"):
        print(i)
        break


for i in range(10000000):
    if hashlib.md5(f"{file}{i}".encode()).hexdigest().startswith("000000"):
        print(i)
        break
