nums = open("2015/input/day_1.txt").read()

 
print(nums.count('(') - nums.count(')'))

x = 0
for i, n in enumerate(nums, start=1):
    x += 1 if n == '(' else -1
    if x == -1:  
        print(i) 
        break
        
