# names = ['Elbek', 'Zakir']
# for name in names:
#     pass

# []-list(изменяемй)
# ()-tuple(не изменяемый)
# name = 'Elbek'
# name = name.upper()
# print('Elbek'.upper())
# print(name)
#  name[0] = 'A'
# del name
# print(name)'123Elbek'
# name = '123Elbek 12 34 12'
# name = name[3].isdigit()
# name = name.islower()
# print(name)

# name = name.lower()
# print(name)

# print(name.index('e'))

# print(name.index('e', 1 , 2))

# print(name.isalpha())
# print(name.count('12'))


# name = 'Elbek      '
# name = name.strip()
# name = name.rstrip()
# name = name.lstrip()
# print(name)

# i = 0
# str = ''
# for letter in 'My name is Elbek. I am 22 years old':
#     if i % 2 == 0: str += letter.upper()
#     else: str += letter
#     i += 1

# print(str)

# i = 0
# str = ''
# for i, letter in  enumerate('My name is Elbek. I am 22 years old', 0):
#     if i % 2 == 0: str += letter.upper()
#     else: str += letter
# print(str)

# i = 0
# str = ''
# for i, letter in  enumerate('My name is Elbek. I am 22 years old', 0):
#     if i % 2 == 0: str += letter.upper()
#     else: str += letter.lower()
# print(str)

# str = 'HELLO'
# str2 = ''
# for ltr in str:
#     str2 = ltr + str2
# print(str2)
# print(str[::-1])

# str = 'Hello'
# str2 = ''
# for i in range(len(str) - 1, -1, -1):
#     str2 += str[i]
# namelist = list('Elbek')
# namelist.reverse()
# str = '__'.join(namelist)
# print(str)

# nums = [1,2,3]
# t = tuple(nums)
# print(t)

# print([elem  for elem in range(10)])



# print([elem  for  elem in range(10) if elem % 2 == 0])

from random import random 
from random import randint

# from datetime import datetime as d
# print(d.now())

# print(int(random() * 256))
# print(randint(0, 255))
# print(int(100 + random() * (200 - 100)))
print(round(100 + random() * (200 - 100)))