"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]


Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]


Constraints:

    2 <= nums.length <= 10**4
    -10**9 <= nums[i] <= 10**9
    -10**9 <= target <= 10**9
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


nums = [2, 7, 11, 15]
target = 9

def solution1():    # time complexity is O(n**2)
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i+1:], start=i+1):
            if n + m == target:
                return i, j


# final solution
def solution2():    # time complexity is O(n)
    d = {}
    for i, n in enumerate(nums):
        d[target - n] = i

    for i, n in enumerate(nums):
        if (n in d) and (i != d[n]):
            return i, d[n]

print(solution2())
