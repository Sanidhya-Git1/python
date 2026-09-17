def myFunction() : 
    x = 5 # local-variable
    print (x);

x = 4 #global variable
print(x)
myFunction();
print(x)

def myFunction1() : 
    z = 5 #local variable
    print (z + y)

y = 4 #global variable
myFunction1()
print(y)
#print(z) # NameError: name 'z' is not defined

# modify global variable
def f() : 
    global s
    print(s)
    s = "CD" # global variable
    print(s)

s = "AB"
print(s)
f()
print(s)


# local variable
def func1():
    local_var = 5
    print(local_var)

func1()
#print(local_var) #NameError: name 'local_var' is not defined

# non local variable
def outerFunction():
    nonlocal_var = 10
    def innerFunction():
        nonlocal nonlocal_var
        nonlocal_var +=5
    innerFunction()
    print(nonlocal_var)


outerFunction()


