"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
 

Example 1:

    Input: s = "()"
    Output: true


Example 2:

    Input: s = "()[]{}"
    Output: true


Example 3:

    Input: s = "(]"
    Output: false
 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""

def solution1(s):

    last = []

    try:
        for c in s:
            if c == '(':
                last.append(c)
                continue
            elif c == ')' and last.pop() == '(':
                continue
            elif c == '[':
                last.append(c)
                continue
            elif c == ']' and last.pop() == '[':
                continue
            elif c == '{':
                last.append(c)
                continue
            elif c == '}' and last.pop() == '{':
                continue
            else:
                return False

    except IndexError:
        return False

    if len(last) == 0:
        return True
    else:
        return False


print(solution1('[){}'))


