# coding=utf-8
__author__ = 'halilbay'

"""A palindromic number reads the same both ways. The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99"""


def is_palindrome(result):
    str_result = str(result)
    first = str_result[:len(str_result) / 2]
    last = str_result[len(str_result) / 2:]
    if first == last[::-1]:
        return True

a = []
for i in range(999, 100, -1):
    for i2 in range(999, 100, -1):
        res = i * i2
        if is_palindrome(res):
            a.append(res)
a.sort()
print a[-1]

