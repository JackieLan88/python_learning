 # Lists!
 # there are four collection data types in python
'''List: A collection which is ordered and changeable (modifiable).
     - Allows duplicate members.
 Tuple: A collection which is ordered and unchangeable or unmodifiable (immutable).
     - Allows duplicate members.
 Set: A collection which is unordered, unindexed, and unmodifiable, but we can add new items to the set.
     - Duplicate members are not allowed.
 Dictionary: A collection which is unordered, changeable (modifiable), and indexed.
     - No duplicate members.
 List: A collection of different data types which is ordered and modifiable (mutable).
     - A list can be empty or it may have different data type items.'''

 # how to create a list

 # syntax using built-in function
lst = list()
empty_list = list()        # this is an empty list, no item in the list
print("Length of a list with parenthesis: ",len(empty_list))  # 0

 #syntax using square brackets, []

lst = []
empty_list = []    # this is an empty list, no item in the list
print("Length of a list with square brackets: ",len(empty_list)) # 0

# list with initial values. we use len() to find the length of a list

fruits = ['banana','orange','mango','lemon']
vegetables = ['Tomato','Potato','Cabbage','Onion','Carrot']
animal_products = ['milk','meat','butter','yoghurt']
web_tech = ['HTML','CSS','JS','React','Redux','Node','MongDB']
countries= ['Finland','Estonia','Denmark','Sweden','Norway']

# print the list and its length

print('Fruits:', fruits)
print("Number of fruits: ", len(fruits))
print('Vegetables:', vegetables)
print("Number of vegetables: ", len(vegetables))
print("Animal products:", animal_products)
print("Number of animal products:", len(animal_products))
print("Web technologies:", web_tech)
print("Number of web technologies:", len(web_tech))
print('Countries:',countries)
print("Number of countries:",len(countries))

list_data_types = ['Jackie',21,True,{'Country':'United States','city':'Chicago'}]
bangtan = ['Namjoon','jin','Suga','Jhope','Jimin','Tae','Jungkook']
first_member = bangtan[0]
print(first_member)
sec_member = bangtan[1]
print(sec_member)
third_mem = bangtan[2]
print(third_mem)

last_mem = len(bangtan)-1
last_bts = bangtan[last_mem]
print(last_bts)
print(bangtan[len(bangtan)-1])


# accessing list items using negative indexing
fruits = ['banana','orange','mango','lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last)


#unpackimg list items
lst = ['item1','item2','item3','item4','item5']
first_item,second_item,third_item, *rest =lst

print(first_item)
print(second_item)
print(third_item)
print(rest)

leader, hyung, rapper, *rest, goldenMaknae = ['namjoon','jin','suga','jhope','jimin','V','Jungkook']
print(leader)
print(hyung)
print(goldenMaknae)
print(rest)
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#slicing items from a list -- this is possible by speciying a range between start and end of the list
# there is also another way of slicing list using step, which will slice the list in a certain gap
drama = ['true beauty','my demon','my holo love', 'doom at your service']
all_dramas = drama[0:4]
print(all_dramas," this list has been indexed with 2 arguments")
all_dramas = drama[0:]
print(all_dramas," this list has been indexed with 1 arguments")
romance_dramas = drama[::2] # using the 3rd slot, as step.
print(romance_dramas)
last_drama = drama[2:4] # last two drama in the list
print(last_drama, " are the last two dramas i have seen, using 2 argument to retrieve from list")
last_drama = drama[2:]
print(last_drama) # same purpose without using an end index
