#!/usr/bin/env python3
# q2.py
# Pseudocode:
# Take principal amount as input
# Take rate of interest as input
# Take time in years as input
# Use formula SI = P * R * T / 100
# Print the SI
# Use formula amount = principal amount + SI
# Print Final Amount

principal = float(input('Enter principal amount: '))
rate = float(input('Enter rate of interest: '))
time = float(input('Enter time (in years): '))
simple_interest = principal * rate * time / 100
print('Simple Interest: Rs.', simple_interest)
amount = principal + simple_interest
print('Final Amount: Rs.', amount)
