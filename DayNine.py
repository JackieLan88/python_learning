# conditional statments in python

# by default  -- statements in python scripts are executed sequentially from top to bottom
# if the processing logic requiro se, the sequential flow of execution can be
# altered in two ways:

# conditional execution: a block of one or more statments will be executed if
# a certain expression is true
# repetitive executionL a block of one or more statements will be repetitively executed
# as long as a certain expression is true


# if --- else ---- elif
"""
if condition:
    this part of code runs for truthy conditions
"""

# example 1

a = 3
if a > 0:
    print("A is a positive number")
else:
    print("a is a negative number")

# In our daily life, we make decisions on daily basis

# We make decisions not by checking one or two conditions but multiple conditions
# even simultaneously!
#As similar to life, programming is also full of conditions.
#We use elif when we have multiple conditions!

a = 0

if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

# similar to the ternary operator in Java
a = 34
print("A is greater than 30") if a > 30 else print("A is less than 30")


# nested conditional statements
b = 0

if b >0:
    if b % 2 == 0:
        print("B is a positive and even number")
    else:
        print("B is a positive and odd number")
elif b == 0:
    print("B is zero")
else:
    print("B is a negative number")

# we can avoid writing nested condition by using logical operator and

# if condition and logical operators

c = 43
if c > 0 and c % 2 == 0:
    print("C is a positive and even number")
elif c > 0 and c % 2 != 0:
    print("C is a positive number")
elif c == 0:
    print("C is zero")
else:
    print("C is a negative number")


# if and or logical operator

user = "jackie"
access_level = 3

if user == "jackie" or access_level >=4:
    print("access granted!")
else:
    print("Access denied!")



# exercise level 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    print("Output:\nYou need "+str(18-age)+" more years to learn to drive")

my_age = 21
your_age = int(input("Enter your age: "))

if your_age > my_age:
    if your_age - my_age > 1:
        print("You are "+str(your_age-my_age)+" years older than me")
    else:
        print("You are 1 year older than me.")
elif my_age > your_age:
    if my_age - your_age > 1:
        print("I am " + str(my_age - your_age) + " years older than you")
    else:
        print("I am one year older than you.")
else:
    print("We are the same age!")

# get two number from the user input prompt
# if a is greater than b return a is greater than b
# is a is less than b return a is smaller than b
# else a is equal to b



a = int(input("\n\nEnter your first number: "))
b = int(input("\nEnter your second number: "))

if a > b:
    print(a, "is greater than ",b)
elif b > a:
    print(a, "is smaller than ",b)
else:
    print(a, "is equal to",b)

# exercise 2

score = int(input("\n\nEnter your score: "))
if score >= 90 and score <= 100:
    print("your score is an A.")
elif score>= 70 and score<=89:
    print("Your score is a B")
elif score>= 60 and score<= 69:
    print("your score is a C")
elif score>= 50 and score<= 59:
    print("your score es a D")
else:
    print("your score is an F")


season = input("Enter a month of the year: ")

if season.lower() == 'january' or season.lower() == 'february' or  season.lower() == 'december':
    print("its winter brrr...")
elif season.lower() == 'march' or season.lower() == 'april' or season.lower() == 'may':
    print("its spring!")
elif season.lower() == 'june' or season.lower() == 'august' or  season.lower() == 'july':
    print("its summer!!")
elif season.lower() == 'september' or season.lower() == 'october' or  season.lower() == 'november':
    print("its fall brrr...")
else:
    print("not an existing month...")

fruits = ['bananas','apples','mangos','oranges','lemon']
selec = input("\n\nHello! Welcome to our fruitmarket!\nWhat kind of fruit are you looking for today?: ")
if selec in fruits:
    print("we do have "+selec+"!\nThat fruit already exist in the list")
else:
    print("we don't have "+ selec+", however we will add it to our inventory checklist!")
    fruits.append(selec)
    print("Added:",fruits)

person={
    'first_name': 'Hobi',
    'last_name': 'Jung',
    'age': 31,
    'country': 'S.K',
    'is_married': False,
    'skills': ['rap', 'dance', 'listening', 'music theory', 'rhythm'],
    'address': {
        'street': 'hope street',
        'zipcode': '06013'
    }
    }

#if len(person['skills']) == 0:

if 'skills' in person.keys():
    print("skill: ",person['skills'][int(len(person['skills'])/2)])
    if 'singing' in person.values():
        print(person.values)
    else:
        print("skill not found")



person['skills'] = ['Javascript','React','Python','Node','MongoDB',]
print(person)

 # If a person skills has only JavaScript and React,
# #print('He is a front end developer'),
# #if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!

if 'Javascript' in person['skills'] and 'React' in person['skills']:
    print('He is a front-end developer')
    if 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
        print("He is a back-end developer")
        print('He is a full-stack developer')
else:
    print("unknown title.")



if not person['is_married'] and person['country'] == "S.K":
    print(person["first_name"]+" isn't married and lives in "+person['country'])

