#!/usr/bin/env python3
# q5.py
# Count number of digits in a number

n = int(input('Enter a number: '))
c = 0
while n != 0:
    c += 1
    n //= 10

print('Number of digits:', c)
