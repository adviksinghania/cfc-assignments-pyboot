#!/usr/bin/env python3
# q2.py

n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
ch = int(input('Enter an operator: '))
if ch == '+':
    print('Sum:', n1 + n2)
elif ch == '-':
    print('Difference:', n1 - n2)
elif ch == '*':
    print('Product:', n1 * n2)
elif ch == '/':
    print('Quotient:', n1 // n2)
elif ch == '%':
    print('Remainder:', n1 % n2)
