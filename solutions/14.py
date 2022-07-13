#!/usr/bin/env python3

strs = ["flower", "flow", "flight"]
strs = ["flower", "flower", "flower"]

def longestCommonPrefix(strs):
    prefix = ''
    for c in zip(*strs):
        prefix += c[0]
        for x, y in zip(c[:-1], c[1:]):
            if x != y:
                return prefix[:-1]
    return prefix

print(longestCommonPrefix(strs))
