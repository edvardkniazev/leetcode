"""
69. Sqrt(x)
Easy


Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer
part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as
pow(x, 0.5) or x ** 0.5.
 

Example 1:

Input: x = 4
Output: 2


Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


Constraints:

0 <= x <= 2**31 - 1
"""


def solution1(x):
    x_max = 2147483647
    candidate = 0
    for i in range(1, x_max, 2):
        candidate += i
        if candidate > x:
            break
    return int((i - 1) / 2)


def solution2(x):
    candidate_1 = 6 * 10**((len(str(x)) - 1) // 2)
    candidate_2 = x / candidate_1
    
    while int(candidate_1) != int(candidate_2):
        candidate_1 = (candidate_1 + candidate_2) / 2
        candidate_2 = x / candidate_1
    return int(candidate_1)


x = 134217727
print(solution2(x))
