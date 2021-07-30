#!/usr/bin/env python3
# q7_c.py
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

n = int(input('Enter a number: '))
for i in range(1, n + 1):
    print('  ' * (n - i), end='')
    for j in range(1, i + 1):
        print(j, end=' ')

    for m in range(i - 1, 0, -1):
        print(m, end=' ')

    print()
