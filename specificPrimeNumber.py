__author__ = 'halilbay'

'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

from primeFactors import is_prime


def getPrimeNumber(nth_prime):
    n = 2
    number = 3
    flag = True
    while n <= nth_prime:
        if is_prime(number):
            if n == nth_prime:
                flag = False
            n += 1

        if flag:
            number += 2

    return number


print getPrimeNumber(10001)