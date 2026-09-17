fruits = ("apple", "banana", "cherry") 
print("Fruits Tuple:", fruits); #Fruits Tuple: ('apple', 'banana', 'cherry')   

first_fruit = fruits[0]; #Accessing an element in a tuple
print("First Fruit:", first_fruit); #First Fruit: apple

# Tuple is immutable - cannot add, remove or change elements in a tuple
#fruits.append("orange"); # AttributeError: 'tuple' object has no attribute 'append'
#fruits.remove("banana"); # AttributeError: 'tuple' object has no attribute 'remove'
#fruits[1] = "kiwi"; # TypeError: 'tuple' object does not support item assignment    

mixed_tuple = ("apple", 42,3.14,(1,2,3))
print("Mixed Tuple:", mixed_tuple); # Mixed Tuple: ('apple', 42, 3.14, (1, 2, 3))


tuple_1 = ("Max", 28, "New York")
print("Tuple 1:", tuple_1)
print(type(tuple_1)) # <class 'tuple'>

# parentheses are optional when creating a tuple with multiple elements
tuple_2 = "Max", 28, "New York"
print("Tuple 2:", tuple_2)
print(type(tuple_2)) # <class 'tuple'>


# tupes are immutable
#tuple_1[2] = "Boston"

# Tuples are iterable, so you can loop through the elements in a tuple using a for loop
new_tuple = (
            ["Alice", 25, "New York"],
            ["Bob", 30, "Los Angeles"]
        )

names = []
for cur_list in new_tuple:
    names.append(cur_list[0])
print("Names:", names) # Names: ['Alice', 'Bob']

# Use list comprehensions to split and bundle corresponding elements from a list of lists into a tuple of tuples
names = [x[0] for x in new_tuple]
ages = [x[1] for x in new_tuple]
cities = [x[-1] for x in new_tuple]

print(names) # ['Alice', 'Bob']
print(ages) # [25, 30]
print(cities) # ['New York', 'Los Angeles']

names, ages, cities = ( [x[i] for x in new_tuple] for i in range(3) )

print(names) # ['Alice', 'Bob']
print(ages) # [25, 30]
print(cities) # ['New York', 'Los Angeles']

# Tuples are immutable, but you can create a new tuple by concatenating existing tuples
myTuple = (1,2)

# Tuple with only one element requires a trailing comma to differentiate it from a regular parenthesis
#single_element_tuple = (1,)

myTuple = myTuple + (3,)
newTuple = myTuple + (3,)

print(myTuple) # (1, 2, 3)
print(newTuple) # (1, 2, 3, 3)

# Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement
person = ("Alice", 25, "New York")

name, age, city = person

print(name) # Alice
print(age) # 25  
print(city) # New York

# one element tuple definition
obj_1 = (5) # Not a tuple, just an integer
print(type(obj_1)) # <class 'int'>

obj_2 = (5,) # This is a tuple with one element
print(type(obj_2)) # <class 'tuple'>

new_obj = ("a",)
print(type(new_obj)) # <class 'tuple'>

#iteration through a tuple using a for loop
tuple_1 = ("Max", 28, "Alberta")
for item in tuple_1:
    print(item, end = " ") # Max 28 Alberta

# iterate by index using range() and len()
n = len(tuple_1)
for i in range(n):
    print(i, tuple_1[i], end = " ") # 0 Max 1 28 2 Alberta

#search a tuple
tuple_1 = ("Max", 28, "Alberta")
result1 = "Alberta" in tuple_1
print(result1) # True
result2 = "Toronto" in tuple_1
print(result2) # False      
result3 = "Boston" not in tuple_1   
print(result3) # True

# convert list to tuple
myList = [1, 2, 3, 4]
myTuple = tuple(myList)
print(myTuple) # (1, 2, 3, 4)

# convert tuple to list
myTuple = (1, 2, 3, 4)
myList = list(myTuple)
print(myList) # [1, 2, 3, 4]    

#convert string to tuple
myString = "Hello"
str_to_tuple = tuple(myString)
print(str_to_tuple) # ('H', 'e', 'l', 'l', 'o')

#convert tuple to string
myTuple = ('H', 'e', 'l', 'l', 'o') 
tuple_to_str = str(myTuple) # or ''.join(myTuple) to get 'Hello' without parentheses and commas 
print(tuple_to_str) # ('H', 'e', 'l', 'l', 'o') 
print(type(tuple_to_str)) # <class 'str'>

# Tuple to string using join() method
tuple_to_str = ''.join(myTuple)
print(tuple_to_str) # Hello 
print(type(tuple_to_str)) # <class 'str'>

#Using a tuple to return multiple values from a function
def divide(a, b) : 
    quotient = a // b
    remainder = a % b
    return (quotient, remainder) # Or return quotient, remainder

result = divide(10, 3)
print(result) # (3, 1)  
print(result[0], result[1]) # 3 1

quotient, remainder = divide(10, 3)
print(quotient) # 3
print(remainder) # 1

