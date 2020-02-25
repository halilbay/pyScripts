# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 2020

@author: halil
"""

romanNumbers = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 
                50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def converter(number):
    romanValue = ''
    if(number > 3999):
        '''
        The largest number you can write in Roman numerals is 3,999 which is MMMCMXCIX. 
        You can represent numbers larger than 3,999 in Roman numerals using an overline. 
        An overline on a Roman numeral means you are multiplying that Roman numeral by 1,000. 
        For the number 50,000 in Roman numerals you would use the Roman numeral L (50) 
        with an overline to make it 50,000.
        For example, L means 50 × 1,000 = 50,000. To enter 50,000 into 
        this calculator as a Roman numeral enter _L.
        '''
        for dec, value in romanNumbers.items():
            while(number >= (dec * 1000)):
                number -= (dec * 1000)
                romanValue += "_{}".format(value)
    for dec, value in romanNumbers.items():
        while(number >= dec):
            number -= dec
            romanValue += value
    print("romanValue is: {}".format(romanValue))
    return romanValue

if __name__ == '__main__':
    print(converter(5))
    print(converter(4000))
    print(converter(50))
    print(converter(999))
    print(converter(600))
    print(converter(9900))
    print(converter(100000))
    print(converter(1000000)) 
