__author__ = 'halilbay'


def isprime(n):
    """
    https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
    """
    # I dunno this technique as to check a number is prime or not but this function is better than us.
    # It contents more math :)
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def sumOfPrimes(value):
    n = 3
    total = 0
    while n < value:
        if isprime(n):
            print n
            total += n
        n += 2
    return total + 2  # it means total prime numbers which starts 3 and below two million and plus 2 means
    # the first prime number.


print sumOfPrimes(2000000)