#!/usr/bin/env python3
# q4.py
# 2, 6, 14, 26, ...

n = int(input('Enter a number: '))
print('Output:')
for i in range(1, n + 1):
    print(2 * (i * i - i + 1), end=', ')
