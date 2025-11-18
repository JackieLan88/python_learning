# loops -- repetition structures

# in order to handle repetitive task programming languages use loops
# python programming languages also provide the following type of loops
# while loop and for loop

# we use the reserved word while to make a while loop

# it is executed repeatedly until given condition is satisfied

# remember when the conditions becomes false, the lines of code after the loop will be continued to be executed

count = 0
while count < 5:
    print(count)
    count = count + 1

# prints from 0 to 4 -- the condition becomes false when count is 5---loop stops

"""if we are interested to run block of code once
the condition is no longer true, we can use else"""
print()
count = 0

while count < 5:  # loop will stop when count = 5
    print(count)
    count = count+1
else: # will execute once count is 5
    print(count)

# break and continue part 1
"""we use break when we would like to get out of or stop the loop"""
print("\n\n")
cycles = 0
while cycles < 5:
    print(cycles)
    cycles = cycles + 1
    if cycles == 3:
        break

# continue --- with continue statement we can skip the current
#iteration and continue with the next
print("\n\n")
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue # ignore instructions below, go into next iteration
    print(count)
    count = count+1


# for loop --- it is used for  iterating over a sequence ( that is either a list, tuple,dictionary, a set or a string)
print("\n\n\nFor Loop")
numbers = [4,5,6,1,6,3]
for number in numbers: # number is a temporary name to refer to the list's items; variable reference only exists inside this loop
    print(number) # items will be printed out


print("\n\nIterating over strings")
language = 'python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])


print("\nFor loop with tuple")
numbers = (3,5,5,6,7,8)
for num in numbers:
    print(num) # num is the iterator ---

print("\nwe can also use for loops in dictionaries!")
person = {"first_name":"Jessie", "last_name":"Cane","age":34,"country":"Canada","is_married":False, "skills":['javascript','html',"mongodb","react","node","python"],"address":{"street":"acorn 433 ave","ZIPCODE":43531}}
print("keys:")
for key in person:
    print(key)

for key, value in person.items():
    print(key,value) # this way we get both keys and values printed out


"""
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for i, (name, score) in zip(names, scores):
    print(f"{i}. {name} scored {score}")
"""


# loops in sets
print("\n\nfor loops in sets")
it_companies = {"facebook","google","microsoft","apple","ibm","oracle","amazon"}
for company in it_companies:
    print(company)


#break and continue part 2 ----
print("\n\ncontinue and break part 2")
numbers = (0,1,2,3,4,5)
for num in numbers:
    print(num)
    if num == 3:
        break # loop stops when num == 3
print("\n\n")

for num in numbers:
    print(num)
    if num ==3: # when num == 3, it will skip the rest of the code up to the next iteration
        continue
    print("next number should be ",num+1) if num != 5 else print("loop ends")
print("outside the loop")

# range function
print("\n\nrange function")

lst = list(range(11))
print("list:",lst) # this list will have [0,1,2,3,4,5,6,7,8,9,10]
st = set(range(1,11)) # this function takes 2 arguments, the first one indicates the start and the second argument states the end of the sequence
print("set:",st) # {1,2,3,4,5,6,7,8,9,10}

lst = list(range(0,11,2))
print("list with range 0,11,2",lst)
st = set(range(0,11,2))
print("set with range 0,11,2", st)

# syntax
# for iterator in range(start,end,step)

#examples:
for num in range(11):
    print(num) # prints 0 to 10 - not including 11

print("nested for loop")
# we can write loops inside loops!!
#dictionary
person = {"first_name":"Jessie", "last_name":"Cane","age":34,"country":"Canada","is_married":False, "skills":['javascript','html',"mongodb","react","node","python"],"address":{"street":"acorn 433 ave","ZIPCODE":43531}}

for key in person:
    if key == "skills":
        for skill in person['skills']:
            print(skill)


# for else...
print("\n\nFor Else")
"""if we would like to execute some messages when the loop ends, we use else"""
for num in range(11):
    print(num)
else:
    print("the loops stops at", num)

# pass
print("\n\npass")
# in python when statement is required (after semicolon), but we don't like to execute any code there,
# we can write the word pass to avoid errors
# also we can use it as a placeholder ---  for future statements

# example
for number in range(6):
    pass
else:
    print("happy birthday!")

# exercise 10

print("\n\niterate - 0 to 10 using for loop")
print("for loop")
for n in range(11):
    print(n)

print("while loop:")
n = 0
while n <= 10:
    print(n)
    n+=1

print("\nnow backwards....iterate from 10 to 0")
for no in range(11):
    print(10-no)

print("\nWrite a loop that makes seven calls to print(), so we get on the output the following triangle:")

for i in range(7):
    print("#" * i)
print()
for i in range(8):
    for j in range(8):
        print("#",end=" ")
    print()

print("\nmultiplications: ")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

lst_lib = ["Python","Numpy","Pandas","Django","Flask"]
for i in range(len(lst_lib)):
    print(lst_lib[i])

print("\n\nUse for loop to iterate from 0 to 100 and print only even numbers")

for i in range(101):
    if i % 2 == 0:
        print(i,end= " ")
        if i > 0 and i % 5 == 0:
            print()

print("\n\nUse for loop to iterate from 0 to 100 and print only odd numbers")

for i in range(101):
    if i % 2 == 1:
        print(i,end= " ")
        if i > 5 and i % 5 == 0:
            print()