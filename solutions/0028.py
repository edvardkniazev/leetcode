"""
28. Implement strStr()
Easy

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask
during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is
consistent to C's strstr() and Java's indexOf().
 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2


Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 10**4
haystack and needle consist of only lowercase English characters.
"""


def solution1(haystack, needle):
    idx = 0
    idx_h = 0
    idxn = 0
    len_h = len(haystack)
    lenn = len(needle)
    while idx_h < len_h:
        while idxn < lenn and idx_h < len_h and haystack[idx_h] == needle[idxn]:
            idx_h += 1
            idxn += 1
        if idxn == lenn:
            return idx
        idx += 1
        idx_h = idx
        idxn = 0
    return -1


haystack = "aaaaa"
needle = "bba"
haystack = "hello"
needle = "ll"

print(solution1(haystack, needle))
