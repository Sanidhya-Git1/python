# common exceptions : 
# Syntax Error
# Type Error
# Value Error
# FileNotFoundError

# How to handle : 
#     try : 
#         # code that may cause exception
#     except : 
#         # code to run when exception occurs 

# try : 
#     # some code which may cause exception
# except: 
#     #optional block
#     #Handling of exception if required
# else:
#     #execute if no exception
# finally: 
#     # some code which always executes no matter if exception is there or not

a = 5 
b = 0

# try : 
#     print (a / b)
# except: 
#     print("cannot divide by zero")
# print("Hello")


# try: 
#     x = x + "abc"
# except Exception as e:
#     print("Error : something went wrong")
#     print(e)



# # using raise
# def divide(a, b): 
#     if b ==0: 
#         raise ValueError("cannot divide by zero")
#     return a / b

# try : 
#     result = divide(10, 0)
# except ValueError as e:
#     print(e)


# # catching specific exception in python
# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5]) # Index out of bounds 
#     x = 5 / 0  # Divide by zero 
#     print (x)
# except ZeroDivisionError: 
#     print("Denominator cannot be zero")
# except IndexError:
#     print("Index out of bound")



# # use else after except
# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 ==0
# except: 
#     print("Not an even number")
# else:
#     reciprocal = 1 / num
#     print(reciprocal)




#try .. finally
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except:
    print("Error : Denominator cannot be 0")
finally:
    print("This is finally block")