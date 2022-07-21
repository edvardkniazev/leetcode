#!/usr/bin/env python3

nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3]
val = 3

pointer = 0
index = 0
length = len(nums)

while index < length:
    nums[pointer] = nums[index]

    if val != nums[index]:
        pointer += 1
    index += 1

print(pointer, nums[:pointer])

