# simple dictionaries
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


# another way to create a dictionaries
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)


# iterating over dictionaries
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# removing a value in dictionaries
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)


# another way to removing a value in dictionaries
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)
























'''
EXERCISE
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
'''


# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }

# # write your code here

# # testing code
# if "Jake" in phonebook:
#     print("Jake is listed in the phonebook.")
# if "Jill" not in phonebook:
#     print("Jill is not listed in the phonebook.")