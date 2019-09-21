# simple class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# create object of the class
myobjectx = MyClass()

# accessing the object variable
myobjectx.variable


# multi object in the same class
myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)


# acessing object function
myobjectx.function()




























'''
EXERCISE
We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
'''

# define the Vehicle class
# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str
# # your code goes here

# # test code
# print(car1.description())
# print(car2.description())