#!/usr/bin/env python3
# q10.py
# Count primes in an array

def issorted(arr):
    if len(arr) in {0, 1}:
        return True

    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False

    return True


arr = tuple(map(int, input('Enter an array of integers: ').split()))
if issorted(arr):
    print('Array is sorted.')
else:
    print('Array is unsorted.')
