#using single quote for a simple string
single_quoted_string = 'Hello, World!'
#using double quote for a simple string
double_quoted_string = "Hello, World!"
#using double quotes to avoid escape character
double_without_escape = "It's a beautiful day"
# using single quote with escape character
single_with_escape = 'It\'s a beautifule day'
#multi line string with a triple quotes
multi_line_string = """
This is a multi-line string. 
It can span multiple times without needing any escape characters. 
"""


#string methods

str = "Hello , world!"
str.lower()  # strings are immutable i.e. you cannot change string
print(str) #Hello , world!
print(str.lower()) #hello , world!
print(str) #Hello , world!  --> strings are immutable
print(str.upper()) #HELLO , WORLD!
print(str.capitalize()) #Hello , world!
print(str.title()) #Hello , World!
print(str) #Hello , world!

#removing space methods
str_new = '    hello   '
print(str_new) #    hello
print(str_new.strip())  #hello  --> removes leading and trailing whitespace
print(str_new.lstrip()) #hello  --> removes only leading whitespace
print(str_new.rstrip()) #    hello  --> removes only trailing whitespace
print(str.split()) # ['Hello', ',', 'world!']
print("".join(["A", "B"])) #AB
print(" ".join(["A", "B"])) #A B
print("!".join(["A", "B"])) #A!B
print("___".join(["A", "B"])) #A___B
print("___".join(["A", "B", "C"])) #A___B___C


#string concatenation
str1 = "Sanidhya"
str2 = "Soni"
concatenated_string = str1 + " " + str2
print(concatenated_string) #Sanidhya Soni
concatenated_string = str1 + "      " + str2
print(concatenated_string) #Sanidhya      Soni

#string formatting
name = "Alice"
age = "30"
formatted_string = f"My name is {name} and age is {age} "
print(formatted_string) # My name is Alice and age is 30
formatted_string_new = "My name is {} and age is {}".format(name, age)
print(formatted_string_new) # My name is Alice and age is 30


# Advanced string operations
text = """
Python is a popular, high-level programming language known for its clear syntax and readability.
 It supports multiple programming styles, including object-oriented, imperative, and functional programming. 
 Its large standard library and active community make it ideal for web development, data analysis, and artificial intelligence. 
 Code written in Python is easy to maintain and runs on all major operating systems. Beginners and experts choose Python to build scalable applications quickly and efficiently.
"""
#Define the prompt for the AI model, asking it to summarise the provided text
prompt = f"""
Summarise the text delimited by triple backticks into a single sentence.
```{text}```
"""

print(prompt)
