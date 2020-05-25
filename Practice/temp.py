import numpy as np
import sys

nums = [1,5,2,4,3]
print(sum(nums))  # 15

courses = ['history','maths','physics','chemistry']

for item in sorted(courses):
    print(item)

for index,item in enumerate(sorted(courses),start=1):
    print(index,item)

course_string = '-'.join(courses)

print(course_string)  # history-maths-physics-chemistry

new_courses = course_string.split('-')
print('new_courses -- ',new_courses)


# mutable example "List"
courses = ['history','maths','physics','chemistry']
new_courses = courses

courses[0] = 'Arts'

print(courses)  #     ['Arts', 'maths', 'physics', 'chemistry']
print(new_courses)  # ['Arts', 'maths', 'physics', 'chemistry']


# immutable example "Tuple"
tuple_1 = ('history','maths','physics','chemistry')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Arts' -- TypeError: 'tuple' object does not support item assignment

# sets
set_1 = {'history','maths','physics','chemistry','chemistry'}
set_2 = {'history','maths','AI','ALGO'}

print(set_1)  # {'maths', 'physics', 'chemistry', 'history'} un-ordered and remove duplicates
print(set_1.intersection(set_2))  # {'maths', 'history'}
print(set_1.difference(set_2))  # {'physics', 'chemistry'}

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # NO this will create empty Dictionary
empty_set = set()  # YES correct way to create empty_set

# Dictionary

student = {'name':'Devdutt' , 'age': 27, 'courses': ['AI','ALGO']}
print(student['courses'])  # ['AI', 'ALGO']
# print(student['phone'])  # KeyError: 'phone'
print(student.get('phone'))  # None

student['phone'] = '555-555555'
print(student.get('phone'))  # 555-555555

age = student.pop('age')  # {'name': 'Devdutt', 'courses': ['AI', 'ALGO'], 'phone': '555-555555'}
print(student)
print(age)

print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key,value)

# name = input("What is you name -- ")  # waits for input from user
# print('Hello',name)

for i in range(10):
    print(i)

corpus = np.array([[
    'cheap meds for sale',
    'click here for the best meds',
    'book your trip',
    'cheap book sale , not meds',
    'here is the book for you'
    ],['1','2','3','4','5']])

print(corpus)
print(corpus.ndim)
print(corpus.shape)
print(corpus.size)

print(sys.path)
# ['C:\\DEVDUTT JADEJA\\Python\\AI_LabExercise\\Practice', 'C:\\DEVDUTT JADEJA\\Python\\AI_LabExercise', 'C:\\Users\\Devdutt\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\Devdutt\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\Devdutt\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\Devdutt\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\DEVDUTT JADEJA\\Python\\AI_LabExercise\\venv', 'C:\\DEVDUTT JADEJA\\Python\\AI_LabExercise\\venv\\lib\\site-packages', 'C:\\DEVDUTT JADEJA\\Python\\AI_LabExercise\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.8.egg', 'C:\\DEVDUTT JADEJA\\Python\\AI_LabExercise\\venv\\lib\\site-packages\\pip-19.0.3-py3.8.egg']

import random
import datetime
import calendar
import os

randomvalue = random.choice(courses)
print(randomvalue)
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd()) # C:\DEVDUTT JADEJA\Python\AI_LabExercise\Practice
print(os) # <module 'os' from 'C:\\Users\\Devdutt\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\os.py'>


def sum_of_squares(*listOfNumber):
    """computes the sum of squares"""
    s = 0

    for num in listOfNumber:
        s = s + num**2

    return s


print(sum_of_squares((2)))
print(sum_of_squares(2,4,5))



lst = [1,5,8]
print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# print(sum_of_squares(lst))
# Does not work correctly
# s = s + num**2
# TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'


def length(*t, degree=2):
    """Computes the length of the vector given as parameter. By default, it computes
    the Euclidean distance (degree==2)"""
    s=0
    for x in t:
        s += abs(x)**degree
    return s**(1/degree)


print(length(-4,3))
print(length(-4,3, degree=3))
