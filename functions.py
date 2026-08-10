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

# 2. **kwargs -- Allows a function to accept any number of keyword arguments. It collects all keyword arguments into a dictionaly.
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="Alice", age=30, city='New York')

