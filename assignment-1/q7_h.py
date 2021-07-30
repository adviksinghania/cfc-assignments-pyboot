#!/usr/bin/env python3
# q7_h.py
# * * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *

n = int(input('Enter a number: '))
for i in range(n, 0, -1):
    print('* ' * i, end='')
    print('  ' * (2 * (n - i) - 1), end='')
    if i == n:
        print('* ' * (i - 1))
    else:
        print('* ' * i)

for i in range(2, n + 1):
    print('* ' * i, end='')
    print('  ' * (2 * (n - i) - 1), end='')
    if i == n:
        print('* ' * (i - 1))
    else:
        print('* ' * i)
