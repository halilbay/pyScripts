__author__ = 'halilbay'

'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

# source => https://gist.github.com/endolith/114336


def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)


def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

print lcm(*range(1, 21))

# 2. source => http://www.enrico-franchi.org/2010/09/nice-functional-lcm-in-python.html


def lcm2(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x, y), numbers, 1)

print lcm2(range(1, 21))