#!/usr/bin/env python3

nums = []
nums = [2, 1, -1]
nums = [1, 2, 3]
nums = [-1, -1, -1, -1, -1, 0]
nums = [1, 7, 3, 6, 5, 6]

n = len(nums)
if n > 0:
    left = [nums[0]] * n
    right = [nums[n - 1]] * n

for i in range(1, n):
    left[i] = left[i - 1] + nums[i]
    right[i] = right[i - 1] + nums[n - i - 1]

for i in range(n):
    if left[i] == right[n - i - 1]:
        print(i)
        exit()
print(-1)

