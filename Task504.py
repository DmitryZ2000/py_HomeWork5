# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from os import system

def code_function(my_str):
    code_str = ''
    zero_item = 0
    for item in range(len(my_str) - 1):
        if my_str[item] != my_str[item+1]:
            code_str += str(item + 1 - zero_item) + my_str[item]
            zero_item = item + 1
        elif item + 2 == len(my_str):
            code_str += str(item + 2 - zero_item) + my_str[item]
    if my_str[-1] != my_str[-2]:
        code_str += '1' + my_str[-1]
    return code_str


def decode_function(my_str):
    decode_str = ''
    number = ''
    for item in range(len(my_str)):
        if my_str[item].isdigit():
            number += my_str[item]
        elif not my_str[item].isdigit():
            mult = int(number)
            decode_str += mult * my_str[item]
            number = ''
    return decode_str

    return decode_str

system('cls')

# str1 = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# str1 = 'wwwAAcccc'
str1 = 'wwwAAccccT'

print('Исходная строка для кодирования для RLE:','\n', str1)
# print(*list(enumerate(str1)))
code_str = code_function(str1)
print('Кодированная строка для кодирования по RLE:','\n', code_str)
dec_str = decode_function(code_str)
print('Декодированная исходная строка','\n',dec_str)
