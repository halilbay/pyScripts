__author__ = 'halilbay'

number_file = open('files/products_number.txt', 'r').read()

index = 0


def largestProduct(numbers, adjacent):

    arr_list = list(numbers)
    arr = []
    result = []
    for idx, i in enumerate(arr_list):
        arr.append(arr_list[idx:idx+int(adjacent)])

    for i in arr:
        total = 1
        for i2 in i:
            total *= int(i2)
            result.append(total)

    return max(result)

print largestProduct(number_file, 13)