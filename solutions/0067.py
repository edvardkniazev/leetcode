"""
67. Add Binary
Easy


Given two binary strings a and b, return their sum as a binary string.

 
Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10**4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


def solution1(a, b):
    max_len = max(len(a), len(b))
    a = a.rjust(max_len, '0')
    b = b.rjust(max_len, '0')

    a = [int(x) for x in a[::-1]]
    b = [int(y) for y in b[::-1]]
    s = []

    d = 0
    for x, y in zip(a, b):
        d = x + y + d
        s.append(d % 2)
        d //= 2
    if d:
        s.append(d)

    s.reverse()
    return ''.join(str(x) for x in s)


a = '11'
b = '1'
a = "1010"
b = "1011"

print(solution1(a, b))
