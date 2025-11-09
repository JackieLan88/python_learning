#Arthmetic Operators in Python

#Boolean data types

print(True)         #these values for boolean data types should be capitalized
print(False)

#integers operations

print('Addition: ', 1+2)
print('Subtraction: ', 2-1)
print('Multiplication', 2*3)
print('Division:', 4/2)
print('Division: ',7/2) #decimal
print('Division without the remainder: ', 7//2)
print('Division without the remainder', 7//3)
print('Modulus', 3%2)
print('Exponentiation: ', 2**3)

#floats in python

print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# complex numbers in python and multiplying them
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: (1+1j) * (1-1j) =  ',(1+1j) * (1-1j))


a = 7
b = 2013

total = a + b
diff = a - b
product = a * b
division = a * b
remainder = a % b
floor_division = a // b
exponential = a ** b

# why didn't we use sum for adding a and b?
# sum is a built-in function in python

print("a+b= ",total)
print("a-b= ", diff)
print("a*b= ", product)
print("a/b= ", division)
print("a%b= ", remainder)
print("a//b= ", floor_division)
print("a**b= ", exponential)

print('==Addition, Subtraction, Multiplication, Division, Modulus ==')

num_one = 3
num_two = 4

#Arithmetic operations

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

print("")
#calculating area of a circle
radius = 10
area_of_a_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_a_circle)

# calcuting the area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("The area of a rectangle: ", area_of_rectangle)


# calculating the weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print("The weight is",weight,'N')

# calculate the density of a liquid

mass = 75  # in kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 kg/m^3

print("density: ", density)

# comparison operators
print("greater than 3>2",3>2)
print("Greater than or equal to 3>=2", 3>=2)
print("Less than 3<2",3<2)
print("Less than 2<3",2<3)
print("Less or equal to 2<=3",2<=3)
print("Equal 3 == 2",3 == 2)
print("Not equal 3!=2",3!=2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False



# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print("b" in "bangtan")
print("7 is 5", 7 is 5)
print("2 is not 3", 2 is not 3)
print("bangtan" in "bangtan sonyeondan")
print('4 is 2 ** 2', 4 is 2 ** 2)

#logical operators   (and, or, not)
print(3 > 2 and 4 > 3)
print(3>2 and 4<3)
print(3 > 2 and 4 > 3)
print('True and True', True and True)
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


# Exercises for Python
age = 21        # Declare your age as integer variable
height = 157.0  # Declare your height as a float variable
cnum = 1 + 1j    #Declare a variable that store a complex number

b = float(input("Enter base: "))#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
h = float(input("Enter height: "))
area = (0.5 * b) * h
print("the area of the triangle is ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c

print("The perimeter of the triangle is ", perimeter)

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the length of the width: "))

ar = length * width
pe = (length * 2) + (width * 2)
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))'
print("The area of the rectangle is", ar," and the perimeter is ", pe)


radius = float(input("Enter the radius of a circle: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius

print("the area of this circle with a radious of ", radius," is ", area, " and the cicumferences is ", circumference)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = int(input("Enter a value for x:"))
y = x**2 + (6 * x) + 9


print(len('python') > len('dragon'))
print(('on' in "python") and ("on" in "dragon"))
print("jargon" in "I hope this course is not full of jargon.")

print("the length of python is " + str(float(len("python"))))
print(45 % 2 == 0, " this number is not even if the result is 1")

print("Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.")
print(7//3)
print(7//3 == int(2.7))
print(int(9.8) == 10)

hours = float(input("Enter hours "))
rate = float(input("Enter rate per hour: "))
earn = hours * rate
print("Your weekly earning is $", earn)

years = int(input("how many years have you lived? "))

seconds = years * 365 * 24 * 60 * 60

print("You have lived for", seconds, " seconds" )

# Display the table 
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
