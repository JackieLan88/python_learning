# tuples
# is a collection of different data types
# ordered and unchangeable(immutable)
# written in round brackets
# we cannot use add, insert, remove, methods in a tuple because it is not modifiable
# common methods: tuple(), count(), index()
# tuple() --- create an empty tuple
# count() --- to count the number of a specified item in a tuple
#index()  -- to find the index of a specified item in a tuple
# . operator --- to join two or more tuples and to create a new tuple
from DayFive import animal_products

# creating a tuple

empty_tuple = ()   #empty tuple
empty_tuple = tuple() # creating a tuple using the tuple constructor
type(empty_tuple)
# tuple with initial values
tpl = ('item1','item2','item3')
fruits = ('banana','orange','mango','lemon')
type(fruits)

# tuple len
print(len(tpl))

# Syntax for negative indexing --- similar to LISTS
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

# slicing tuples
# similar to strings....by specifying a range with a starting index to where you would like to end
# we would have in return value the substring

bts = ('namjoon','jin','suga','jhope','jimin','taehyung','jungkook')
all_items = bts[0:7]    # all items --- where 7 is excluded
all_items = bts[0:]     # all items as well

sope = bts[2:4] # does not include 4

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]


all_neg = bts[-7:]
vkook = bts[-2:]
namjin = bts[-7:-5]
print(bts)
print(all_neg)
print(vkook)
print(namjin)



# Changing tuples to list ?? why? tuples are IMMUTABLE! which means you can't modify them
list_bts = list(bts)
list_bts[0] = 'Namjoon'
print(bts)
print(list_bts)

# We can check if an item exists or not in a tuple using in,
# it returns a boolean.


bts = ("joonie",'jinnie','yoongi','hobi,','mochi','taetae','kookie')
print(bts)
print('kookie' in bts)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
#fruits[0] = 'apple' TypeError: 'tuple' object does not support item assignment


vminkook = ('jimin','taehyung', 'jungkook')
namjin = ("namjoon",'jin')
sope = ('suga','jhope')

all_bts = namjin + sope + vminkook
print(all_bts)


del all_bts
del bts
del fruits
#print(bts)
# Exercises: Level 1
family = tuple()
sisters = ('samira','caty')
brothers = ('bangtan',)
siblings = sisters + brothers

print(f"i have {len(siblings)} siblings")

family_members = list(siblings)
family_members.insert(0,"mom")
print(family_members)
family_members.insert(1,"Dad")

print(family_members)

# Exercises: Level 2
fruits = ('apple','strawberry')
vegetables = ('carrots', 'spinach')
animal_products = ('eggs','milk','cheese','meat')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_list = list(food_stuff_tp)
tot = int(len(food_stuff_tp)/2)
chop = food_stuff_tp[0:tot]
print(food_stuff_tp)
print(chop)

first_three = food_stuff_list[0:3]
last_three = food_stuff_list[-3:]

print(first_three)
print(last_three)

del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia in nordic_countries"+ 'Estonia' in nordic_countries) # Check if 'Estonia' is a nordic country
print('Iceland' in nordic_countries) # Check if 'Iceland' is a nordic country


