#!/usr/bin/env python3

x = 1234567890987654321
y = str(x)

for i in range(len(y) // 2):
    print(y[i], y[-1-i])

    if y[i] != y[-1-i]:
        print(False)

print(True)
