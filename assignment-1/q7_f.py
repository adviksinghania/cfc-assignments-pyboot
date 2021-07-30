#!/usr/bin/env python3
# q7_f.py
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

n = int(input('Enter a number: '))
for i in range(1, n + 1):
    print('  ' * (n - i), end='')
    print('* ' * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print('  ' * (n - i), end='')
    print('* ' * (2 * i - 1))
