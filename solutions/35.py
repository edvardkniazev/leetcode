#!/usr/bin/env python3

nums = [1,3,5,6,7,8,9]
target = 3

left, right = 0, len(nums)

fraction = (right - left) // 2
index = left + fraction

while fraction:
    fraction //= 2

    if target < nums[index]:
        right = index
        index -= fraction

    elif target > nums[index]:
        left = index
        index += fraction

    else:
        print('found', index)
        exit()

    print(left, index, right, fraction)

if target < nums[0]:
    print('not found', left)

else:
    print('not found', right)
