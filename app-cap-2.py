import numpy as np
import math
import random
# import only selected functions
# from math import sqrt, cos, log10

a = np.array([1,2,3,4,5])

print(a[0])

print(math.sqrt(25))
print(type(2))
print(type(2.2))
print(type("2"))

print(isinstance(2.0, int))
print(isinstance(2.0, float))
print(isinstance("Test", bool))

# casting

number = 2
float_number = float(2)

print(float_number)

print(1 > 0 and 0 == 0)
print(0 > 1 and 0 == 0)
print(0 > 1 or 0 == 0)
print(not(0 > 1 or 0 == 0))

if 0 == 0:
    print('0 é igual a 0')
else:
  print('vá aprender matemática')

list1 = [1, 2, 3]
list1_1 = list(['abacate', 'uva'])

print(list1[0])
print(list1_1)

# each with lambada
double_values = list(map(lambda x: x * 2, list1))
print(double_values)

list1.append(list(map(lambda x: x * 2, list1)))
print(list1)
print(len(list1))

list1.remove(2)
print(list1)
print(len(list1))
print(list1.pop(1))
print(len(list1))
print(list1_1.index('abacate'))

print(list1_1[0:1])
print(list1_1[-1])

# tuplas acts likes a imutable list
tuple1 = ()
t1 = (1,2,3)

print(len(tuple1))
print(t1)
print(t1.index(2))

str1 = 'Rafael fique calmo'
print(str1[-5:].upper())
print(str1.split(' '))
print(f'{str1}, por favor')

dict1 = {'name':'Rafael'}
print(dict1)
print(dict1.keys())

set1 = set([1,2,3,4])
set2 = set([1,4,5,6])
print(set1)
print(set1.intersection(set2))

print(1 in set1)
print(10 in set2)

def sum(a,b):
  return a + b

print(sum(10,10))

def name_and_age(name, age):
  return f"{name} has {age} years old."

print(name_and_age('Rafael', 36))

range_list = range(0,10)
# the last param is the increment factor
range_list_increment_arg = range(0, 10, 2)

for n in range_list:
  print(n)
  
print("--------")

for n in range_list_increment_arg:
  print(n)
  
print("---------")
x = random.random()
print(x)

x = []
for i in range(100):
  x.append(random.random())
  
print("---------")

for i in x:
  print(i)
  
names = ['Rafael', 'Gabriel', 'Moema', 'Luisa']

random.shuffle(names)

print(names)

print(random.choice(names))
print(random.sample(names, 2))
print(random.sample(names, 3))

# Random with Numpy
print(np.random.random())