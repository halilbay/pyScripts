# coding=utf-8
__author__ = 'halilbay'

'''Hence the difference between the sum of the squares of the first ten natural numbers
 and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.'''


def all_number_sq(numbers):
    last_number = numbers[-1]
    total_numbers = last_number * (last_number + 1) / 2
    total_numbers_sq = total_numbers ** 2

    def number_sq_total():
            number_sq_all = last_number * (last_number + 1) * (2 * last_number + 1) / 6
            return number_sq_all

    return total_numbers_sq - number_sq_total()

print all_number_sq(range(1, 101))

