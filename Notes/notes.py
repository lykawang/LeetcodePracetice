## Generate random number
import random
print(random.randrange(1, 10))



## Casting
# from float to int: remove all decimals



## String
# Remove any whitespace from the beginning or the end
a = '    Hello, World!    '
print(a.strip())  # not change 'a' itself

# replace a string with another string
print(a.replace('H', 'J'))

# splits the string into substrings
print(a.split(','))

# use format() to combine strings and numbers
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder1 = "I want {} pieces of item {} for {} dollars."
print(myorder1.format(quantity, itemno, price))
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity, itemno, price))

# more string methods
# https://www.w3schools.com/python/python_strings_methods.asp



## Boolean
# except
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# all other value bool( ) usually is True

# determine if an object is of a certain data type
x = 200
print(isinstance(x, int))



## Collection Data Types
# List
# ordered, changeable, allows duplicate members
fruits_list = ["apple", "banana", "cherry"]

# Tuple
# ordered, unchangeable, allows duplicate members
fruits_tuple = ("apple", "banana", "cherry")

# Set
# unordered, unchangeable (can remove/add items), unindexed, no duplicate members
fruits_set = {"apple", "banana", "cherry"}

# Dictionary
# ordered, changeable, no duplicate members
info_dic = {"name": "John", "age": 36}



## List
# add item
fruits_list.append("orange")
print(fruits_list)

# add list or other collection
tropical = ("mango", "pineapple", "papaya")
fruits_list.extend(tropical)
print(fruits_list)

# remove specified index
fruits_list.pop(1) # no specify, remove the last one
print(fruits_list)
del fruits_list[0] # alternatively
print(fruits_list)

# sort items LIST
fruits_list.sort()
print(fruits_list)

fruits_list.sort(reverse=True)
print(fruits_list)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)



## Tuples
# To create a tuple with only one item, you have to add a comma after the item
# To change or add or remove a value in tuple, convert it to a list and convert it back

# unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
(green, *yellow) = fruits
print(green)
print(yellow)