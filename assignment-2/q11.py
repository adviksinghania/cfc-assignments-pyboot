#!/usr/bin/env python3
# q11.py
# Count multiples of 5

arr = tuple(map(int, input('Enter an array of 0s and 1s: ').split()))
zeroes, ones = 0, 0
for i in arr:
    if i == 0:
        zeroes += 1
    if i == 1:
        ones += 1

arr = [0] * zeroes + [1] * ones
print('Sorted array:', arr)
