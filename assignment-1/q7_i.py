#!/usr/bin/env python3
# q7_i.py
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5

n = int(input('Enter a number: '))
for i in range(n, 0, -1):
    for k in range(n, i, -1):
        print(k, end=' ')

    for j in range(1, i + 1):
        print(i, end=' ')

    for m in range(i, 1, -1):
        print(i, end=' ')

    for p in range(i + 1, n + 1):
        print(p, end=' ')

    print()

for i in range(2, n + 1):
    for k in range(n, i, -1):
        print(k, end=' ')

    for j in range(1, i + 1):
        print(i, end=' ')

    for m in range(i, 1, -1):
        print(i, end=' ')

    for p in range(i + 1, n + 1):
        print(p, end=' ')

    print()
