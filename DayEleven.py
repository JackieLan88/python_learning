# functions

"""custom-functions-- reusable block of code or programming statements
designed  to perform a certain task, to define or declare a function,
python provides:
def ---- keyword"""

# declaring and calling a function

def generate_full_name():
    first_name = "Kelly"
    last_name = "Min"
    space =' '
    full_name = first_name+space+last_name
    print(full_name)
generate_full_name() # invoking function

def adding():
    num1 = 2
    num2 = 53
    total = num1 + num2
    print(total)
adding() # calling function


# functions can return values --- even if they don't have a return statement (in that case the return value is None)
def generate_full_name():
    first_name = "Kelly"
    last_name = "Min"
    space =' '
    full_name = first_name+space+last_name
    return full_name

print("return value: ",generate_full_name())

def adding():
    num1 = 2
    num2 = 53
    total = num1 + num2
    return total

print("return value: ",adding())


# function with parameters:
"""in a function we can pass different data types as arguments(numbers, strings
booleans, lists, tuples, dictionaries,sets"""


# single parameter
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings("Jackie"))


def add_ten(num):
    ten = 10
    return num+ten
print(add_ten(90))

def square_number(a):
    return a * a
print(square_number(2))

def area_circle(r):
    PI = 3.1416
    area = PI * r **2
    return area

print(area_circle(4))

def sum_of_num(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)

print(sum_of_num(4)) # this should print out none since there is no return st in the function
print(sum_of_num(100))

# two parameters
def calc_age(current_year,birth_year):
    return current_year - birth_year
print("Age: ", calc_age(2025,2004))

def weight_of_objects(mass,gravity):
    weight = str(mass *gravity)+' N'
    return weight
print("Weight of an object in Newtons: ", weight_of_objects(100,9.81))


"""When calling a function where you will pass arguments, you can reference their
parameters and assign a value when invoking the method signature"""
def adding(num1,num2):
    return num1+num2

print("adding 2 + 5 = ", adding(num2 = 2,num1=5)) # when specifying the parameter and assigning it a value, that order of the parameters/args don't matter

# returning a list

def find_even(n):
    even = []
    for i in range(n+1):
        if i % 2 == 0:
            even.append(i)
    return even
print(find_even(10))

# functions with default parameters

def greetings(name = 'Jackie'):
    message = name + ", welcome to python for everyone!"
    return message
print(greetings('Conan'))
print(greetings())

# arbitrary number of args
"""when we do not know the number of arguments we pass to our function,
we can create a function which can take arbitrary number of args by adding *
before the parameter name"""

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total+=num
    return total
print(sum_all_nums(2,3,5,))

# function as a parameter of another function
def sn(n):
    return n * n
def do_something(f,x):
    return f(x)
print("calling function do_something and passing function sn and value 3: ", do_something(sn,3))


