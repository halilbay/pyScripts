__author__ = 'halilbay'


def is_prime(number):
    flag = True
    for i in range(2, number):
        if i != number and number % i == 0:
            flag = False

    return flag


def prime_factor(number):
    arr = []
    for i in range(2, number):
        if number % i == 0 and is_prime(i):

            arr.append(i)
    return arr
