nums = open("2021/day_1/day_1_input.txt").read().splitlines()


answer = sum(x < y for x, y in zip(nums, nums[1:]))
answer = sum(x < y for x, y in zip(nums, nums[3:]))

print(answer)

