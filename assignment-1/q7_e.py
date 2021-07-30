#!/usr/bin/env python3
# q7_e.py
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

n = int(input('Enter a number: '))
for i in range(1, n + 1):
    c = 1
    for j in range(1, i + 1):
        print(c, end=' ')
        c = c * (i - j) // j

    print()
