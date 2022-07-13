#!/usr/bin/env python3

x = 0
sign = 1 if x > 0 else -1
x = abs(x)
y = '0'

while x:
    y += str(x % 10)
    x //= 10

x = sign * int(y)

if x < 2147483647 and x > -2147483648:
    print(x)
else:
    print(0)
