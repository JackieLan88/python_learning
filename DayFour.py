# strings
# text is a string data type
# and a data type written as text is a string

# these can be wrapped in single, double or triple quote
# there are different string method and built-in functions

# creating a string in python

letter = "p"

print(letter)

print("the length of letter is: ", letter)

greeting = 'Hello, World!'

print(greeting)
print("the length of greeting is ", len(greeting))

sentence = 'I hope you are enjoying 30 days of python challenge'
print(sentence)

multiline_string = '''I am at teacher and enjoy teaching. I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''

print(multiline_string)


first_name = "Jacqueline"
last_name = 'Landi'
space = ' '
full_name = first_name  + space + last_name
print(full_name)

# escape sequences

print("I hope every one enjoying the python challenge.\nDo you? ")  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')

print("this is a back slash symbol(\\)")    # To write a back slash

print('In every programming language it starts with\'Hello, World!\'')

'''String formatting - old style using % operator

% - used to format a set of variable enclosed in a TUPLE 

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

'''
#strings only - one way to format output

first_name = "Jackie"
last_name = 'lan'
language = "python"

formatted_string = 'I am %s %s. I teach %s' %(first_name,last_name,language)
print(formatted_string)

bts = 'Suga'
born = 1993
practiceFormat =  "My name is %s, and I was born in the year %d" %(bts,born)

print(practiceFormat)



# string and numbers being formatted

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f' %(radius,area) # the 2 after the decimal point means the 2 most significant digits after the decimal point
print(formated_string)


python_libraries = ['Djange','Flask','NumPy','MathPlotLib','Pandas'] # this is a list
formated_string = 'The following are python libraries:%s'%(python_libraries)

print(formated_string)

# New Style String Formatting (str.format)
firstN = "Jackie"
lastN = "Lan"
lang = "Java"
formated_string = "I am {} {}. I teach {}".format(firstN,lastN,lang)

print(f"")  # next line
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a,b, a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b)) # format :.2f means the output is limited to two digits after the decimal
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))


# string and numbers again.....
radius = 10
pi = 3.14
area = pi * radius**2
formatted_string = "The area of a circle with a radius {} is {:.2f}".format(radius,area)
print(formatted_string)

# string interpolation
'''Using f-strings (formatted string literals): This is the most modern and recommended method introduced in Python 3.6.'''


bts = "sonyeondan"
song = "Idol"

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a %b}')
print(f'{a} // {b} = {a // b}')
print(f'{a}**{b} = {a**b}')     # single quotes

print(f"{song} by {bts}")   # double quotes


#unpacking character

bangtan = "Bangtan"
ba,ab,c, d,e, f, g= bangtan
print(ba)
print(ab)
print(c)
print(d)
print(e)
print(f)
print(g)

first_letter = bangtan[0]
print(first_letter)
second_letter = bangtan[1]
print(second_letter)
last_index = len(bangtan)-1
last_letter = bangtan[last_index]
print(last_letter)

# another way to index values from the right to the left
language = "Object Oriented Programming"
# negative index
lastletter = language[-1]
print(f"{lastletter} is the last letter of language.")
second_last = language[-2]
print("The second to last letter in the string language: ",second_last)

# slicing python strings into substrings

first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)

last_thre = language[-3:]
print("last three letter of the language string:", last_thre)


another_last_three = language[len(language)-3:]
print(another_last_three)


# reverse strings
greeting = "Hello, Bangtan"

print(greeting[::-1])
print(greeting[0:5])
print(len(greeting))
# string slicing takes   var[start:stop:step]
                #          start includes index
                #           stop doesn't include position
                #           step how many we take/skip
print(greeting[0:14])
print(greeting[0:14:1])
print(greeting[18:6:-1])


bts1 = 'thirty days of python'
print(bts1.capitalize())  # capitalizes ONLY first letter

print(bts1.count('o')) # counts the occurences of letter inside string
print(len(bts1))
print(bts1.count('o',15,20))
print(bts1.count('da'))

print(bts1.endswith('on')) # checks if the string ends with specification
print(bts1.endswith('rt'))   # return true or false -- -boolean values

print(bts1.find('y'))
print(f"{bts1.find('th')} is the index of the first occurence of th in \"{bts1}\"")
print(f"when there is not ocurrences of sd, the find() method will return {bts1.find("sd")}.")


# methods
"""
rfind() ---> : Returns the index of the last occurrence of a substring, if not found returns -1
format(): ---> formats string into a nicer output
index() ---> return the lowest index of a substring giving two arguments
rindex() -- returns the hightest index of a substring with two arguments    first place takes the substring itself, then the position

"""


challenge = 'ThirtyDaysPython'
print(challenge)
print(challenge.isalnum()) # True

challenge = '30DaysPython2'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal() checks if there is numbers only without spaces
hub = 'Cause it\'s easy when i\'m with you, no one sees me the way you do'

print(hub)
print(hub.isdecimal())  # False
hub = '123'
print(hub.isdecimal())  # True
hub = '\u00B2'
print(hub.isdigit())   # False
hub = '12 3'
print(hub.isdecimal())  # False, space not allowed

"""isdigit(): Checks if all characters in a string are numbers 
(0-9 and some other unicode characters for numbers)"""

dontrm = 'Thirty'
print(dontrm.isdigit()) # False
dontrm = '30'
print(dontrm.isdigit())   # True
dontrm = '\u00B2'
print(dontrm.isdigit())   # True
dontrm = "3.42"                             # these are strings!!!
print(dontrm.isdigit()) #/???????

#isnumeric(): Checks if all characters in a string are numbers or 
#number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num)
print(f"{num} is a num: {num.isnumeric()}") # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

"""
isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
islower(): Checks if all alphabet characters in the string are lowercase
isupper(): Checks if all alphabet characters in the string are uppercase
join(): Returns a concatenated string
strip(): Removes all given characters starting from the beginning and end of the string
replace(): Replaces substring with a given string
split(): Splits the string, using given string or space as a separator
title(): Returns a title cased string
swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
startswith(): Checks if String Starts with the Specified String

"""

wording = "Thirty" + " " + "Days"

pal = "Coding for all"

cut_pal = pal[6:len(pal)]
print(cut_pal)


brands = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(brands.split(", "))

print(pal[10])
 