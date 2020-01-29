#!usr/bin/env python
def conversion(num):
    if num < 1 or num > 3999:
        return "Range Fault"

    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''

    for i in range(len(num_list)):
        while num >= num_list[i]:
            result += str_list[i]
            num -= num_list[i]
    return result
