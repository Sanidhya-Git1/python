greetings = "Hello, World!"

greetings_message = 'Hello, World! How are you?'

multiline_string = """
This is a multiline string.
It spans multiple lines.
You can use triple quotes to create it.
"""


str = " hello sanidhya "
print(str) # Output:  hello sanidhya
print(str.strip()) # Output: hello sanidhya
print(str.lstrip()) # Output: hello sanidhya
print(str.rstrip()) # Output: hello sanidhya
print(str.upper()) # Output:  HELLO SANIDHYA
print(str.lower()) # Output:  hello sanidhya
print(str.capitalize()) # Output:  Hello sanidhya
print(str.title()) # Output:  Hello Sanidhya

#string formating
name = "Alice"
age = 30
# Using f-string (Python 3.6+)
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

#using str.format() method
formatted_string_2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string_2)  # Output: My name is Alice and I am 30 years old.

#practice
attendee = "John"
event = "python workshop"

# formating using f-string
new_formatted_strng = f"Attendee name is '{attendee}' for the event '{event}'"  
print  (new_formatted_strng)  # Output: Attendee name is 'John' for the event 'python workshop'

new_string = "Attendee name is '{}' for the event '{}'".format(attendee, event)
print(new_string)  # Output: Attendee name is 'John' for the event '

words = new_string.split();
print(words)  # Output: ["Attendee", "name", "is", "'John'", "for", "the", "event", "'python", "workshop'"]