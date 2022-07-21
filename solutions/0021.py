#!/usr/bin/env python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode
l2 = ListNode

l1 = [1, 2, 3]
l2 = [1, 3, 4]

result = ListNode
result = []
print(l1, l2)
print(result)

while l1 and l2:
    if l1[0] < l2[0]:
        result.append(l1.pop(0))
    else:
        result.append(l2.pop(0))

if l1:
    result.extend(l1)
else:
    result.extend(l2)

print(result)
