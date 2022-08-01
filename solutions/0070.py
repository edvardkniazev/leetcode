"""
70. Climbing Stairs
Easy


You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


def solution3(n):

    def f(p, q):
        mx, mn = (p, q) if p > q else (q, p)
        r = 1
        for i in range(mx + 1, p + q + 1):
            r *= i
        for i in range(2, mn + 1):
            r /= i
        return round(r)


    s = 0
    for two in range(0, n // 2 + 1):
        one = n - 2 * two
        s += f(one, two)

    return(s)


print(solution3(6))
