__author__ = 'halilbay'


def calc_sd_and_variance(numbers):
    import math
    # sd => standard deviation.
    # this function calculate standard deviation and variance and returns respectively sd and variance

    # s.d -> find the mean of numbers, add up the difference between each number and mean, then square the result and
    # divide up the count of numbers mines 1 and calculate the root of this value.

    # variance is equal to square of s.d.

    if not isinstance(numbers, list):
        numbers = [numbers]

    total = 0
    count = len(numbers)
    s_d_total = 0
    s_d = 0
    for number in numbers:

        total += number
    avg = float(total) / count

    for number in numbers:
        s_d_total += pow(number - avg, 2)
    try:
        s_d = s_d_total / (count - 1)
    except ZeroDivisionError as e:
        print("You cannot divide a number to zero %s", e)
    return math.sqrt(s_d), s_d


list_numbers = [12, 23, 34, 44, 59, 70, 98]
print calc_sd_and_variance(numbers=list_numbers)