#variables and built-in functions
'''variables store data in a compute memory
    mnemonic variable are recommended to use in many programming languages
    a mnemonic variable  is a var name that can easilty be remembered and associated



'''

first_name = "Jacqueline"
last_name = "Landi"
country = 'United States'
city = "Chicago"
age = 21
is_married = False
skills = ['Java','SQL','JS','Python',] #list

person_info = {'firstname': 'Jacqueline',
               'lastname':'Landi',
               'country':'United States',
               'city':'Helsinki'}   #dictionary

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

print("First name: ",first_name)
print("The length of the first name is", len(first_name))
print("Last name: ",last_name)
print("The length of the last name is: ", len(last_name))
print("Country: ",country)
print("City", city)
print("Age", age)
print("Married", is_married)
print("Skills", skills)
print("Person information", person_info)

#declaring variable and initializing them in the same statement/same line

first_name, last_name, country, age, is_married = 'Jackie','Lan','US','19', True

print(first_name,last_name,country,age,is_married)
# input buily-in function for storing data that has been prompted form the user
first_name = input("What is your name? ")
last_name = input("What is your last name? ")
age = input("How old are you? ")

print("My name is ", first_name,last_name,"and I am", age, "years old.")

#explicit casting

num_int = 7
print('num_int:', num_int)   #7
num_float = float(num_int)      #casting float to an int
print('num_float after casting num_int:', num_float) #7.0


gravity = 9.81
print("Float number: ",gravity)
print("float to int:",int(gravity)) #which is rounding down

#int to string
num_int = 4
print('num_int:', num_int)   #4
num_str = str(num_int)
print("int converted to string", num_str)

# and vice versa

num_str = "43.2"
print(num_str)
num_float = float(num_str)
print("string to floating number", num_float)


#string to list
first_name = 'Jacqueline'
print(first_name)
first_name_to_list = list(first_name)

print(first_name_to_list)

is_true = True
is_light_on = False

bangtan, sonyeondan, kim, jung = 2013, "June", "namjoon", "kook"

#Exercises Level 2

bts = "Bangtan Sonyeondan"

print("The length of the meaning of bts is", len(bts),"which means", bts)
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
divsion = num_one/num_two
remainder = num_one%num_two
exp = num_one ** num_two
floor_div = num_one//num_two

radius_circle = 30
area_circle = 3.14 * (radius_circle**2)
circum_of_circle = 3.14 * (2 * radius_circle)
print("The area is: ",area_circle, "with a radius of 30 meters")

print("The circumference of a circle with 30 meters as radius: ", circum_of_circle)
r = input("what radius does your circle have?")
rad = float(r)
area_circle = 3.14 * (rad**2)
print("The area of your circle is: ", area_circle)

user_first = str(input("Enter your first name:"))
user_last = str(input("Enter your last name:"))
user_country = str(input("Enter the country you are located in:"))
user_age = int(input("How old are you?"))

#Run help('keywords') in Python shell or in your file 
# to check for the Python reserved words or keywords
