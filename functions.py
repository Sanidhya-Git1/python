# syntax
# def function_name (parameters):
    # function body
    # return (optional)

def subtract(a,b):
    return a-b
result = subtract(10,5)
print(result)

def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")
greet(name="Sanidhya", message="Hi")
greet(message="Good Morning", name="Ekta")
#greet("Adhrit") #TypeError: greet() missing 1 required positional argument: 'message'

# ---- Function parameter and Argument

# variable length argument
# 1. *args -- allows a function to accept any number of positional arguments and it collects all positional arguments into a tuple
def multiply(*args):
    res = 1
    for num in args:
        res *= num
    return res

print(multiply(1,2,3,4))

# 2. **kwargs -- Allows a function to accept any number of keyword arguments. It collects all keyword arguments into a dictionayy.
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="Alice", age=30, city='New York')


# Type Hinting 
# It is not forced in Python but it is a good practice to use type hints to indicate the expected types of function parameters and return values. It helps with code readability and can assist with static type checking.
def greet_someone(name: str) -> None :   
    print(f"Hello, {name}!")

greet_someone("Alice")  # Output: Hello, Alice!
greet_someone(name = "Bob")    # Output: Hello, Bob!

def add_numbers(a : int, b : int) -> int : 
    return a + 2 * b;

result = add_numbers(3, 4)  # Output: 11
print(result)

result = add_numbers(a=5, b=6)  # Output: 17
print(result)
