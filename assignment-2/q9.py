#!/usr/bin/env python3
# q9.py
# Count primes in an array

def isprime(n):
    # Checks if a number is prime or not
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


arr = set(map(int, input('Enter an array of integers: ').split()))
c = sum(1 for i in arr if isprime(i))
print('Number of primes:', c)
