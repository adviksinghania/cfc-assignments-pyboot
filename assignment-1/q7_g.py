#!/usr/bin/env python3
# q7_g.py
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

n = int(input('Enter a number: '))
for i in range(1, n + 1):
    print('* ' * i, end='')
    print('  ' * 2 * (n - i), end='')
    print('* ' * i)

for i in range(n - 1, 0, -1):
    print('* ' * i, end='')
    print('  ' * 2 * (n - i), end='')
    print('* ' * i)
