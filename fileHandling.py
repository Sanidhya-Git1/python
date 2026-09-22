# different modes to open a file in python:
# r - open a file for reading (default mode)
# w - open a file for writing. Creates a new file if it does not exist or truncates if it exists.ZeroDivisionError
# x - open a file for exclusive creation. If the file already exists, the operation fails. 
# a - open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist. 

# file = open("test1.txt", 'r')
# type(file)

# content = file.read()
# print(type(content))
# print(content)
# file.close()



# open and close in one shot (to avoid resource leak)
# with open("test1.txt", "r") as file: 
#     content = file.read()
#     print(content)



#readLine()
# with open("test1.txt", "r") as file: 
#     cur_line = file.readline()
#     print(cur_line)

#     cur_line = file.readline()
#     print(cur_line)


# with open("test1.txt", "r") as file:
#     while True: 
#         cur_line = file.readline()
#         if cur_line:
#             # some operations here
#             print(cur_line)
#         else:
#             break



# #readlines()
# with open("test1.txt", "r") as file: 
#     lines = file.readlines()
#     print(lines)


# Navigate through file
# with open("test1.txt", "r") as file: 
#     #move to 11 character
#     #file.seek(11)
#     file.readline()

#     #find the position of the current character
#     position = file.tell()

#     print(file.read())
#     print(position)



# file6 =  open("test2.txt", "w")
# file6.write("Hello there!\n How are you ")
# file6.close()


# # Creates a new file OR erase and overwrite
# with open("test2.txt", "w") as file:
#     file.write("Programming is Fun.")
#     file.write("Python for beginners")


# with open("test3.txt", "w") as file:
#     L = ["This is Lagos\n", "This is Python\n", "This is Fcc\n"]
#     file.write("Hello there!")
#     file.writelines(L)


with open("myfile.txt",'r') as file:
    lines = file.readlines
idx = []
for line in lines:
    find_idx = line.index("Python")
    idx.append(find_idx)
print(idx)