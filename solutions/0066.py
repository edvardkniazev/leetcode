"""
66. Plus One
Easy

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].


Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


def solution1(digits):
    delta = 1
    lenght = len(digits) - 1
    for i in range(lenght, -1, -1):
        d = digits[i] + delta
        digits[i] = d % 10
        #delta = d // 10
        delta = 1 if d > 9 else 0
    if delta:
        digits.insert(0, 1)
    return digits


def solution2(digits):
    delta = 1
    for i in range(len(digits) - 1, -1, -1):
        d = digits[i] + delta
        if d == 10:
            digits[i] = 0
            delta = 1
        else:
            digits[i] = d
            delta = 0
            break
    if delta:
        digits.insert(0, 1)
    return digits


def solution3(digits):
    delta = 1
    digits.reverse()
    for i, d in enumerate(digits):
        d += delta
        if d == 10:
            digits[i] = 0
        else:
            digits[i] = d
            delta = 0
            break
    if delta:
        digits.append(1)
    digits.reverse()
    return digits


digits = [4,3,2,1]
digits = [1,2,3]
digits = [9]
print(solution3(digits))
