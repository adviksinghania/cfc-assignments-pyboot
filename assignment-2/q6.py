#!/usr/bin/env python3
# q6.py
# GCD of 2 numbers

def gcd(x, y):
    while(y):
        x, y = y, x % y

    return x


a, b = map(int, input('Enter 2 numbers: ').split())
print('GCD:', gcd(a, b))
