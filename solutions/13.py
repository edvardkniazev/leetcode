#!/usr/bin/env python3
s = 'MCCCXLVIII'

case_i = False
case_x = False
case_c = False
result = 0

for symbol in s:
    if symbol == 'I':
        result += 1
        case_i = True

    elif symbol == 'V':
        result += 5
        if case_i:
            result -= 2
            case_i = False

    elif symbol == 'X':
        result += 10
        case_x = True
        if case_i:
            result -= 2
            case_i = False

    elif symbol == 'L':
        result += 50
        if case_x:
            result -= 20
            case_x = False

    elif symbol == 'C':
        result += 100
        case_c = True
        if case_x:
            result -= 20
            case_x = False

    elif symbol == 'D':
        result += 500
        if case_c:
            result -= 200
            case_c = False

    elif symbol == 'M':
        result += 1000
        if case_c:
            result -= 200
            case_c = False

print(result)
