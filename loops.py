# Loops
# For loop : iterate over a sequence (ex. list, tuple, string)
# While loop : execute code block while a condition is true

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 1
while count <=3:
    print(count)
    count += 1

# loop control statements
# break : Exit the loop immediately
# continue : skip the rest of the loop body and start the next iteration

# nested loops
items = ['a','b','c','d']
pairs = []
for i in items:
    for j in items:
       pairs.append((i,j))

print(pairs) # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c'), ('d', 'd')]