#!/usr/bin/env python3
# q8.py
# Count multiples of 5

arr = set(map(int, input('Enter an array of integers: ').split()))
c = sum(1 for i in arr if i % 5 == 0)
print('Multiples of 5:', c)
