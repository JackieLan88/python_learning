# 30 days of python challenge
# from DayTwo import first_name, last_name

print("Addition ",3+2)
print("Subtraction ",4-1)
print("Multiplication ",65*3)
print("Division ",35/2)
print("Exponential ",54**2)
print("Modulus", 43%10)
print("Floor Division Operator", 37//2)  #rounds down and truncates decimal part

#datatypes

print("What type is 10? ", type(10))
print("What type is 3.14? ", type(3.14))
print("What type is 1+3j? ", type(1+3j))
print("What type is Asabeneh? ", type('Asabeneh'))
print("What type is [1,2,3]? ", type([1,2,3]))
print("What type is {'name':'Asabeneh'}? ", type({'name':'Asabeneh'}))
print("What type is {9.8, 3.14, 2.7}? ", type({9.8, 3.14, 2.7}))
print("What type is (9.8, 3.14, 2.7)? ", type((9.8, 3.14, 2.7)))

print("What type is 3==3? ",type(3 == 3))              # Bool
print("What type is 3>=3",type(3 >= 3))              # Bool


#Write a script that prompts the user to enter number of years.
# #Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years: "))
numDays = years * 365
numHours = numDays * 24
numMin = numHours * 60
numSecs = numMin * 60

print(f"Number of seconds {numSecs}")
'''
print("Length of name: ", len(first_name))
print(first_name > last_name)
num_one = 5
num_two = 4
total = num_one + num_two
'''# help('keywords')