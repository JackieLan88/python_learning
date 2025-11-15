"""A dictionary is a collection of unordered, modifiable paired datatype
and it stores data with a (key:value)"""

# to create a dictionary we use curly brackets or the dict() built-in functon

# syntax
empty_dict = {}

# dictionary with data values
dct = {"key1": "value1","key2":"value2","key3":"value3","key4":"value4"}

# example -- any value could be any type: string, boolean, list, tuple, set or even dictionaries
person = {'first_name':'Yoongi','last_name':'Min','age':'32','country':'south korea','is_married':False,"skills":['singer','rapper','songwriting','musical production','music video director'], "address":{"community":'daegu',"zipcode":"54032"}}


# to check length of a dictionary we can use:
print(len(dct)) # 4 ---- this checks the number os 'key':'value' pairs in the dictionary

print(len(person))


# accessing dictionary items -- we can access dictionary items by referring to its key name!

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct['key1'])
print(dct['key3'])

# going back to our example:

print("first name: ",person['first_name'])
print("last name: ", person['last_name'])
print("country: ", person['country'])
print("skils: ",person['skills'])
print("skill: ", person['skills'][0])
print('address: ', person['address']['community'])
#print(person['city']) # error if key doesn't exist

# to avoid any errors in case the key doesn't exist, we have to check(we can use the get method)

# the get method returns None whcich is a nonetype object data type of the key doesn't exist

person = {'first_name':'Yoongi',
          'last_name':'Min',
          'age':'32',
          'country':'south korea',
          'is_married':False,
          "skills":['singing','rap','songwriting','musical production','music video director'],
          "address":{"community":'daegu',"zipcode":"54032"}
          }

print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))   # None -- avoids keyerror

# adding items to a dictionary  -- we can add new key and value paris to a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'  #added

person['job_title'] = 'Singer'
person["skills"].append('HTML')  # skills is a list
print(person)
person['skills'][-1] = "dance"
print(person)

# modifying items in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'valueone'


person["first_name"] = "namjoon"
person["age"] = 30

print(person)


#checking key in a dictionary --- using the in operator to check if a key exist in a dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print("is key 2 in the dictionary",'key2' in dct)
print("is key 23 in the dictionary",'key23' in dct)

# removing key and value pairs from a dictionary
"""pop(key): remove the item with the specified key name
    popitem: remove the last items
    del: removes an item with specified key name
    """

dct.pop("key1")
print(dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()
print(dct)
del dct['key2']
print(dct)


# changing dictionary to a list of items
# the items() method changed dictionary to a list of tuples

dc = {"album": "Dark_and_wild",
      "songs": 8,
      "release_year": 2014,
      "main_track": "danger",
      "album_sold":"4.2 million"}

print(dc.items())
# dict_items([('album', 'Dark_and_wild'), ('songs', 8), ('release_year', 2014), ('main_track', 'danger'), ('album_sold', '4.2 million')])

# clearing a dictionary -- if we don't want items in a dictionary
# we can clear them using clear() method

# syntax
jin = {"name": "jin","year":1992,"album":"echo"}
print(jin)
print(jin.clear()) # None

# deleting a dictionary
# if we do not use the dictionary we can delete it completely
#syntax

fruit = {"name":"apple","color":"red","seeds?":"yes","shape":"round"}
print(fruit)
del fruit
# print(fruit) not defined

# copy a dictionary -- using the copy() method  --- using copy we can
# avoid mutation of the original dictionary

fruit = {"name":"apple","color":"red","seeds?":"yes","shape":"round"}
fruit_copy = fruit.copy()
print(fruit_copy)


# getting dictionary keys as a list!

# the keys() method gives us all keys of a dictionary as a list

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

keys = dct.keys()
print(keys)
print(person.keys())

# getting dictionary values as a list -- the values() method
# gives us all the values of a dictionary as a list

values = person.values()
print(values)
person["first_name"] = "Yoongi"
print(person)


# exercises day 8

dog = {}
dog["name"] = "Murphy"
dog["color"] = "brown"
dog["breed"] = "pomerania"
dog["age"] = 5

print(dog)

student = {"first_name":"chris","last_name":"martin","gender":"male","marital status":"single","skills":["organization","time-management","microsoft suite 360"],"country":"United States","city":"Oak Park","address":"4532 N Leavington Ave"}

print(student.keys())
print("what is the length of student:",len(student))


print("type of students ",type(student["skills"]))
student["skills"].append("communication")
student["skills"].append("teamwork")

print(student["skills"])
print(student.values())

# changing a dictionary to a list of tuples using items() method

print(student.items())
lst = student.items()
print(lst)

del student["last_name"]
print(student)

del student
# print(student)