from functools import reduce

#lambda function 
# syntax : 
# lambda argument(s) : expression
# arguments are the values passed to the function and expression is the operation performed on those arguments. 
# expression is executed and the result is returned when the lambda function is called.

greet = lambda : print("Hello, World!")
greet()  # Output: Hello, World!

 # map(function, iterable, ...) applies the given function to each item of the iterable (like a list) and returns a map object (which is an iterator). You can convert it to a list or other collection type if needed.
 # filter(function, iterable,..) constructs an iterator from those elements of the iterable for which the function returns true.   
 # reduce(function, iterable, initializer) applies the function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value. The initializer is optional and can be used to provide an initial value for the reduction.

def add (a, b):
    return a + b

add_2 = lambda a, b : a + b
added_val2 = add_2(5, 10)
print(added_val2)  # Output: 15

def greet1() :
    print("Hello, World!")

greet2 = lambda : print("Hello, World!")

greet3 = lambda name : print(f"Hello, {name}!")

greet1(); 
greet2();
greet3("Alice")  # Output: Hello, Alice!

# map()
numbers = [2,4,6,8,10]

def square(number):
    return number ** 2

numbers_square_list = list(map(square, numbers))
print(numbers_square_list)  # Output: [4, 16, 36, 64, 100]


squared_numbers = list(map(lambda number: number**2, numbers))
print(squared_numbers)  # Output: [4, 16, 36, 64, 100]


# filter()
scores = [66,90,68,59,76,60,88,74,81,65]
def isAStudent(score):
    return score > 75

filtered_scores = filter(isAStudent, scores)
over_75 = list(filtered_scores)
print(over_75)  

# using lambda
over75 = list(filter(lambda score : score > 75, scores))
print(over75)


# reduce()
myIter = [1,2,3,4]
result = reduce(lambda x, y : x + y, myIter) # initially result = 0 , add all numbers in result
print(result) #10

result = reduce(lambda x, y : x + y, myIter, 5)# initially result = 5 , add all numbers in result
print(result) #15

# practice questions
func = lambda a, b : b - a if a <= b else a * b
print(func(10,2), func(2,10))

# write a code to keep negative numbers 
numbers = [1,0,-3,6,5,-9,24]
less_than_zero = list(filter(lambda x : x<0 , numbers))
print(less_than_zero)

# write a code to find length of each string
strings = ["apple", "fig", "orange"]
lengths_list = list(map(len, strings ))
print(lengths_list)

#write a code to keep even numbers 
numbers = [1,2,3,4,5,6,7,8]
even_numbers_list = list(filter(lambda num : num%2 == 0, numbers))
print(even_numbers_list)

# write a code to find the maximum number
numbers = [3,7,2,9,5]
result = reduce(lambda a, b : a if a > b else b, numbers)
print(result)



