class Employee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
        self.empCount = 0

    def displayEmployee(self):
        print("Name : "+self.name + " , Salary : "+self.salary)

    def __repr__(self):
        return "{ " + self.name + " , "+self.salary


employee1 = Employee("Matt", 2000)
employee2 = Employee("Raju", 5000)

employee1.displayEmployee()
print(employee2)


# Attribute methods
print(hasattr(employee1, 'salary')) # returns true if 'salary' attribute exists
print(getattr(employee1, 'salary')) # returns value of 'salary' attribute exists
print(setattr(employee1, 'salary'),7000) # set attribute 'salary' = 7000
print(delattr(employee1, 'salary')) # delete  'salary' attribute exists
