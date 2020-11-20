# Azaan Dawson amdg 11/11/20
numbers = (input('Enter a list on numbers (no spaces) '))
commas = int(numbers.count(','))
number = list(numbers)
numbers_2 = number.copy()
numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
if ',' in numbers_2 :
  numbers_2.remove(',')
number.sort()
del number[0:commas]
print(number)
print(numbers_2)
if list(numbers_2) == number :
  print('The list was sorted')
else :
  print('The list was not sorted')
