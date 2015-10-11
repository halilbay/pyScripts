__author__ = 'halilbay'

"""
Covariance is always measured between 2-dimensions. If you calculate the covariance between one dimension and itself
you get the variance.
Variance is the product of standard deviation value with own value. Covariance is the product of 2-dimensions.
"""


def get_average(numbers):
    count = len(numbers)
    total = 0
    for number in numbers:
        total += number
    return float(format(float(total) / count, '.2f'))


def covariance(numbers1, numbers2):
    if not isinstance(numbers1, list):
        numbers1 = [numbers1]

    if not isinstance(numbers2, list):
        numbers2 = [numbers2]

    avg_1 = get_average(numbers1)
    avg_2 = get_average(numbers2)

    s_d = 0
    count = len(numbers1)

    for idx in range(0, count):
        s_d += (numbers1[idx] - avg_1) * (numbers2[idx] - avg_2)

    return s_d / (count - 1)


"""
num1 = [9, 15, 25, 14, 10, 18, 0, 16, 5, 19, 16, 20]
num2 = [39, 56, 93, 61, 50, 75, 32, 85, 42, 70, 66, 80]

print covariance(num1, num2)

If you have 3-dimensions data set (x, y, z), then you could measure the covariance between x and y, x and z and finally
y and z
x = []
y = []
z = []
cov1 = covariance(x, y)
cov2 = covariance(x, z)
cov3 = covariance(y, z)
"""
