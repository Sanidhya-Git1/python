# Data Structures
# Python List
# What is List :  Ordered, mutable collection of items. Can contain elements of different types. Created using [] and allows duplicate data
# Usage : create variable-length and mutable sequences of objects. Store objects of any type, store multiple types of objects together.

fruits = ["Apple","Banana","Cherry",[1,2,3],10,10.3]
first_item = fruits[1]
print(first_item) #Banana
first_item = fruits[-1]
print(first_item) #10.3
first_item = fruits[-2]
print(first_item) #10

# List is mutable i.e. in the list, elements are changeable. It means we can modify the items stored within the list.
#Adding an item
fruits.append("date");
print(fruits) #['Apple', 'Banana', 'Cherry', [1, 2, 3], 10, 10.3, 'date']

# Removing an item
fruits.remove("Banana")
print(fruits)  # ['Apple', 'Cherry', [1, 2, 3], 10, 10.3, 'date']
#fruits.remove("banana")  #ValueError: list.remove(x): x not in list
#print(fruits)

# changing an item
fruits[1] = "Blueberry"
print(fruits) #['Apple', 'Blueberry', [1, 2, 3], 10, 10.3, 'date']

# ----------------------- SLICING IN PYTHON --------------------------
# used to extract a subset of elements from a sequence (list, tuple or string)
# sequence(start : stop : step_size)
# start index : inclusive , stop index : exclusive  , step_size : the interval between indices (default to 1 )

numbers = [0,1,2,3,4,5,6,7,8,9]
#slicing from index 2 to 5
subset = numbers[2:6]
print(subset) #[2, 3, 4, 5]

#slicing from 1 to 7 with step size of 2
subset = numbers[1:8:2]
print(subset) # [1,3,5,7]

text = "Hello, World!"
# Slicing from index 7 to the end
substring = text[7]
print(substring) # W
substring = text[7:]
print(substring) # World!

#slicing from the beginning to index 5
substring = text[:5]
print(substring) #Hello

# Slicing - negative indexing - can be used for slicing to refer to elements from the end of the sequence
numbers = [1,2,3,4,5,6,7,8,9,10]
# slice the list from the second-to-last element to the fifth-to-last element (exclusive)
slice_negative = numbers[-5:-2]
print(slice_negative) # [6, 7, 8]
numbers = [0,1,2,3,4,5,6,7,8,9]
slice_negative = numbers[-5:-2]
print(slice_negative) # [5, 6, 7]


# --------------------------------- TUPLES ---------------------------------------------
# Ordered collection
# Accessing items using their index (zero based, negative)
# Immutable collection : cannot add, remove or change an item in the tuple
# Different datatypes
fruits = ("apple", "banana", "cherry")
first_item = fruits[0]
print(first_item) # apple
mixed_tuple = ("apple",42,3.14,(1,2,3))
print(mixed_tuple) # ('apple', 42, 3.14, (1, 2, 3))
last_item = mixed_tuple[3]
print(last_item)  # (1, 2, 3)
last_item_second_element = mixed_tuple[3][1]
print(last_item_second_element)  # 2

# ----------------------------- SET -------------------------
# Unordered collection
# Unique items
# Mutable collection
fruits_1  = {"apple", "banana", "cherry"}
fruits_2  = {"apple", "cherry", "banana"}
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits) # {'apple', 'cherry', 'banana'} --> duplicates are removed from a set
# Add an item
fruits.add("date")
print(fruits) # {'banana', 'apple', 'date', 'cherry'}
# removing an item
fruits.remove(("banana"))
print(fruits) # {'date', 'apple', 'cherry'}
# Set can contain different data types but can NOT contain mutable elements like lists or dictionaries
mixed_set= {"apple",42,3.14,(1,2,3)}
print(mixed_set)  # {42, 3.14, 'apple', (1, 2, 3)}

# ----------------------------- DICTIONARY -------------------------
#key-value pairs
# unique element : if dictionary contains duplicate keys, the last key-value pair will be used
# Commonly used to store configuration settings for applications
student_ages = {
    "Alice" : 25,
    "Bob" : 22,
    "Charlie" : 23,
    "Alice" : 26
}
print(student_ages) #{'Alice': 26, 'Bob': 22, 'Charlie': 23}
age_of_alice = student_ages["Alice"]
print(age_of_alice) # 26

# Adding a new key-value pair
student_ages["David"] = 24
print(student_ages) # {'Alice': 26, 'Bob': 22, 'Charlie': 23, 'David': 24}

# different data types
# keys must be immutable i.e. Strings or tuples
# Values can be of any data type
mixed_dict = {
    "name" : "Alice",
    "age" : 25,
    "is_student" : True,
    "grades" : [85,90,92]
}
print(mixed_dict)  # {'name': 'Alice', 'age': 25, 'is_student': True, 'grades': [85, 90, 92]}

user = {
    'name' : 'John Doe',
    'age ' : 30,
    'email' : 'john@example.com',
    'city' : 'New York'
}
email = user['email']
print(email)  # john@example.com

students = {
    1001 : {'name' : 'Alice', 'age' : 20},
    1002 : {'name' : 'Bob', 'age' : 22 }
    # more students
}

