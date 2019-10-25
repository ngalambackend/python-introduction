# simple function
def my_function():
    print("Hello From My Function!")

# my_function()

# function with argument
def my_function_with_args(username, greeting="Halo"):
    print("Hello, %s , From My Function!, I wish you %s" % (
        username, greeting)
    )

# my_function_with_args("Mahrus", "JADI BARU")


# function with return value
def sum_two_numbers(a, b):
    return a + b


# function with *args
def sum_numbers(*args):
    print("args value: {}".format(args))
    print("Type %s: " % (type(args)))

    sum = 0
    for i in args:
        sum += i if type(i) is not str else 0

    return sum

sum = sum_numbers(1,2,3,4)
# # sum = sum_numbers([1,2,3,4], (4,5), 3423)
# print(sum)

# function with *kwargs
def example_kwargs(**kwargs):
    print("kwargs value: {}".format(kwargs))
    print("Type: %s" % (type(kwargs)))

    for key, item in kwargs.items():
        print("Key: %s, Item: %s" % (key, item))

# example_kwargs(
#     one="Satu",
#     two="Dua",
#     three="Tiga",
#     four="Empat",
#     five="Lima"
# )

def contoh(bahasa, *args, **kwargs):
    print(bahasa)
    print(args)
    print(kwargs)

# contoh("Indonesia",4,5, nama="Mahrus", asal="Malang")























'''
EXERCISE

In this exercise you'll use an existing function,
and while adding your own to create a fully functional program.

Add a function named list_benefits()
that returns the following list of strings:
    "More organized code",
    "More readable code",
    "Easier code reuse",
    "Allowing programmers to share and connect code together"

Add a function named build_sentence(info)
which receives a single argument containing a string
and returns a sentence starting with the given string
and ending with the string " is a benefit of functions!"

Run and see all the functions work together!
'''



#     # Modify this function to return a list of strings as defined above
def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"
    ]

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    # is a benefit of functions
    return benefit + "is a benefit of functions"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

# name_the_benefits_of_functions()


datas = [
    {'name': 'Mahrus', 'learn': 'python'},
    {'name': 'Hadi', 'learn': 'php'},
    {'name': 'Dani', 'learn': 'python'},
    {'name': 'Ika', 'learn': 'java'},
    {'name': 'Deni', 'learn': 'java'},
    {'name': 'Dewi', 'learn': 'python'},
    {'name': 'Rina', 'learn': 'php'},
    {'name': 'Rina', 'learn': 'android'},
]

def grouping(datas):
    new_data = {}
    for data in datas:
        if data['learn'] in new_data:
            new_data[data['learn']].append(data)
        else:
            new_data[data['learn']] = [data]
    print(new_data)

def searching(param, datas):
    # new_data = []
    # for data in datas:
    #     if data['learn'] == param:
    #         new_data.append(data)

    new_data = [data for data in datas if data['learn'] == param]

    return new_data

a = searching('python', datas)
print(a)

# grouping(datas)


# data2 = {
#     'python': [
#         {'name': 'Mahrus', 'learn': 'python'},
#         {'name': 'Dani', 'learn': 'python'}
#     ],
#     'php': [],
#     'java': []
# }
