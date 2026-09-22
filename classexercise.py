class Student: 
    #constructor
    def __init__(self, age, name, gpa):
        print("Creating a new Student Object.\n")
        self.age = age
        self.name = name
        self.gpa = gpa

    # Modify the representation with providing the name 
    def __repr__(self):
        return "Student = "+self.name


class Course : 
    # constructor
    def __init__(self,courseName):
        print("Creating a new course Object.\n")
        self.name = courseName
        self.list_of_learners = []

    #method to enroll student
    def add_a_student(self, student_obj):
        self.list_of_learners.append(student_obj)

    # write a method to find the time student (from their gpa) --> return top_student
    def find_top(self):
        max_gpa = 0
        top_student = None
        for student in self.list_of_learners:
            if student.gpa > max_gpa:
                max_gpa = student.gpa
                top_student = student
        return top_student 

# Creating Student class objects    
student_A = Student(25,"Mary", 4)
student_B = Student(28, "Sarah", 3)
student_C = Student(27, "Jill", 2.5)

# Creating Math course
math_course = Course("Math")

math_course.add_a_student(student_A)
math_course.add_a_student(student_B)
math_course.add_a_student(student_C)

print(math_course.list_of_learners)
print()

top_student = math_course.find_top()
print(top_student.age)
print(top_student.name)
print(top_student.gpa)


