#!/usr/bin/env python3
# q7.py
# LCM of 2 numbers

def lcm(x, y):
    num = max(x, y)
    while(True):
        if((num % x == 0) and (num % y == 0)):
            break

        num += 1

    return num


a, b = map(int, input('Enter 2 numbers: ').split())
print("LCM:", lcm(a, b))
