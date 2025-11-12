# sets
"""
another form of data collection of items
the mathematics definition of a set can be applied also in python.

Set is a unique collection of unordered and un-indexed distinct elements

in python, set is used to store unique items, and it is possible to find the:
union
intersection,
difference
symmetric difference,
subset,
super set,
disjoint set among sets
"""
# creating a set -- empty

st = set() # syntax

# creating a set with initial items
st = {'item1','item2','item3','item4'}

example = {'US','Canada','Mexico','Guatemala','Peru'}
# getting length of a set --- using len()
print("the length of example set is: ", len(example))

# to access items we need a repetition structure

# moving on, lets learn how to check the existence of an item in the set
print("Does Chicago exist in example? ", 'Chicago' in example)
print("Does Mexico exist in example? ", 'Mexico' in example)

#adding items in a set

# once a set is created we cannot change any items and, we can also add additional items
print(example)
# to add an item, use add()
example.add('Chicago')
print(example)
# to add multiple items--- we can use update() in a set

example.update(["Ecuador","Colombia","Brazil"])
print("updating....",example)

actors = {"jongsuk","park-hyungsik","changwook","Hyoseop","jaehyun"}
print(actors)
debut_actors ={"Seo InGuk","Kang Joon","HaeJin","Gong yoo","Joon gi","bogum","dongwook"}
actors.update(debut_actors)

print(actors)

# we can remove an item from the set using remove()
# cautious: items might not be in set --- please check first using membership operators
# however, we can use discard---no errors will occur
actors.remove("bogum")
print(actors)

nums = {1992,1993,1994,1995,1997,1995}
print(nums) # will not print duplicates


# pop() --- will randomly remove any items inside set
save = nums.pop()  # -- u can pop an item and save it/store it
print(nums)
print(save)

# clearing items in a set

example.clear()
print(example) # output: set()

# deleting a set
del example
#print(example) # error

# converting list into set

list = [1,2,3,3,3,4,5,6]
print(list)
st = set(list)
print(st) # order must be random ---


"""JOINING SET
 we can join set using the union() or update() method
"""

st1 = {2,4,6,8}
st2 = {1,3,5,7}
st3 = st1.union(st2)
print(st1)
print(st2)
print(st3)

# finding intersections
# intersection return a set of items which are in both the sets

# syntax
st1 = {'item1','item2','item3'}
st2 = {'item3','item4','item5'}
print(st1.intersection(st2)) # {"items3'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

#checking subset and superset
# a set can be a subset or superset of others
# subset - issubset()
# superset - issuperset()


print(whole_numbers.issuperset(even_numbers))
print(even_numbers.issubset(whole_numbers))

# checking the difference between two subsets

vmin = {'jimin',"v"}
vminkook ={"v","jungkook","jimin"}

print("what is the difference between vmin and vminkook? ",vmin.difference(vminkook))
print("what is the difference between vminkook and vmin? ",vminkook.difference(vmin))

# finding symmetric difference between two sets

st1 = {'item1','item2','item3','item4'}
st2 = {'item2','item3'}
# it means A\B U B\A
print(st2.symmetric_difference(st1))

# joining sets
# if two sets do not have a common item or items we call them disjoint set

# we can check if two sets are joint or disjoint using disjoint() methods
bts = {"namjoon","jin","yoongi","hoseok","jimin","tae","jungkook"}
wooga = {"tae","woosik","seojoon","hyungsik","peakboy"}
ninety_seven = {"jungkook","yugyeom","bambam","mingyu","dk","eunwoo","jaehyun","bangchan"}
print(ninety_seven)
print(wooga)
print(ninety_seven.isdisjoint(wooga))
print(bts)
print(bts.isdisjoint(wooga))

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(it_companies)
print("the length of it_companies is: ", len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Instagram","Duckietown","Meta","DeepAi"])
print(it_companies)

it_companies.remove("Facebook")
print(it_companies)

# difference between remove and discard---remove will send error if element does not exist in set
# discard() will try to delete element even if it's not in the set

print(A)
print(B)
print("union: ",A.union(B))
print("intersection: ",A.intersection(B))
print("is A a subset of B: ",A.issubset(B))
print("are A and B disjoint sets? ", A.isdisjoint(B))

A.update(B)
B.update(A)

print(A)
print(B)

print("Symmetric difference between A and B: ", A.difference(B))

del A
del B

set_ages = set(age)
print("list size: ",len(age))
print("set size: ",len(set_ages))
print(len(set_ages)==set(age))

str = "I am a teacher and I love to inspire and teach people"
cha = str.split()
set_cha = set(cha)
print(cha)
print(set_cha)