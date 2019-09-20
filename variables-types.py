'''
NUMBER
=====================
Python supports two types of numbers - integers and floating point numbers.
'''
# integer
# myint = 7
# print(myint)
# print(type(myint)) # check the type of variable myint

# floating point
# myfloat = 8.0
# print(myfloat)
# myfloat = float(7) # cast integer of 7 become floating poin 0f 7
# print(myfloat)
# print(type(myfloat))


'''
STRINGS
====================
Strings are defined either with a single quote or a double quotes.
'''

# mystring = 'Hello'
# print(mystring)
# mystring = "World"
# print(mystring)
# print(type(mystring))

'''
The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
'''
# mystring = "Don't worry about apostrophes"
# print(mystring)


'''
Simple operators can be executed on numbers and strings:
'''
# one = 1
# two = 2
# three = one + two
# print(three)

# hello = "hello"
# world = "world"
# helloworld = hello + " " + world
# print(helloworld)

'''
Assignments can be done on more than one variable "simultaneously" on the same line like this
'''
# a, b = 3, 4
# print(a,b)

'''
Mixing operators between numbers and strings is not supported:
'''
# one = 1
# two = 2
# hello = "hello"

# print(one + two + hello)

















'''
The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
'''
'''

# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
'''