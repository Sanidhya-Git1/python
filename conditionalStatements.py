# there is no {} in python
# indentation helps to determine block of code

# if elif else
x = 10
if x > 5:
    print("x is greater than 5")
    print("adding another line to see if it prints or not")

x = 20
if(x > 25): # () is optional
    print("x is greater than 25")
elif x>5:
    print("x is greater than 15 but less than or equal to 15")

x = 3
if x > 5 :
    print("x is greater than 5")
elif x > 2 :
    print("x is greater than 2 but less than or equal to 5")
else:
    print("x is 2 or less")

age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

number = 20
if number>=10 and number <=25:
    print("Condition is true")
else :
    print("Condition is false")