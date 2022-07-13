#!/usr/bin/env python3

nums = [3, 1, 2, 10, 1]
nums = [1, 1, 1, 1, 1]

runningSum = []

for i, n in enumerate(nums):
    if i:
        runningSum.append(runningSum[i - 1] + n)
    else:
        runningSum.append(n)
print(runningSum)



