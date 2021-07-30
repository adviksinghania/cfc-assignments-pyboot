#!/usr/bin/env python3
# q1.py
# Pseudocode:
# Take credits of leader as input
# if credits are greater than or equal to 7500
#     print Tera Leader
# else if the credits are less than 7500 but greater than or equal to 6000
#     print Gega Leader
# else if the credits are less than 6000 but greater than or equal to 4500
#     print Mega Leader
# else if the credits are less than 4500 but positive
#     print Rising Star
# else
#     print Invalid input

credit = int(input('Enter credits: '))

if credit >= 7500:
    print('Tera Leader')
elif 6000 <= credit < 7500:
    print('Gega Leader')
elif 4500 <= credit < 6000:
    print('Mega Leader')
elif 0 < credit < 4500:
    print('Rising Star')
else:
    print('Invalid input')
