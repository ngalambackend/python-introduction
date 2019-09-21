# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

'''
To use two or more argument specifiers, use a tuple (parentheses):
'''
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

'''
Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string
'''
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)


'''
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''




























'''
You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
'''
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string % data)






















'''
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
'''