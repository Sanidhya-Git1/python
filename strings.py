greetings = "Hello, World!"

greetings_message = 'Hello, World! How are you?'

multiline_string = """
This is a multiline string.
It spans multiple lines.
You can use triple quotes to create it.
"""


str = " hello "
print(str) # Output:  hello
print(str.strip()) # Output: hello
print(str.lstrip()) # Output: hello
print(str.rstrip()) # Output: hello
print(str.upper()) # Output:  HELLO
print(str.lower()) # Output:  hello
print(str.capitalize()) # Output:  Hello
print(str.title()) # Output:  Hello

#string formating
name = "Alice"
age = 30
# Using f-string (Python 3.6+)
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

#using str.format() method
formatted_string_2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string_2)  # Output: My name is Alice and I am 30 years old.
