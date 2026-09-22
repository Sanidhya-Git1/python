# How to create a class
class Student :
    #define a method
    def walk(self):
        print("Hey, I am walking")

# Creating an object
student = Student()

#calling a method using object
student.walk()

student2 = Student()
student2.walk()

#Adding attribute to a class 
student.name = "Matt"
student.age = 25

print(student.name, student.age)

student2.name = "Bob"
student2.age = 30

print(student2.name, student2.age)

 