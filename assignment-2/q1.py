#!/usr/bin/env python3
# q1.py
# Decimal to octal

n = int(input('Enter a number: '))
# print('Octal value:', oct(n)[2:])
m = 0
c = 1
while n != 0:
    a = n % 8
    m += c * a
    c *= 10
    n //= 8

print('Octal value:', m)
