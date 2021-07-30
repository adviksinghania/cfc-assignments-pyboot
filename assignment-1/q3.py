#!/usr/bin/env python3
# q3.py
# Pseudocode:
# Input two numbers
# Take minimum of inputs
# Run a variable loop from 1 to minimum value
#     Check if the inputs are divisible by the loop variable
#         Assign that value to the gcd
#
# Print gcd

a, b = map(int, input("Enter two numbers: ").split())
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f'GCD of {a} and {b} is: {gcd}')
