nums = open("2021/input/day_1.txt").read().splitlines()


answer = sum(x < y for x, y in zip(nums, nums[1:]))
answer = sum(x < y for x, y in zip(nums, nums[3:]))

print(answer)

