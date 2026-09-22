class Shape : 
    def area(self): 
        pass

class Circle (Shape):  # Inherits Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self) :  # method implementation or override
        return 3.14159 * self.radius ** 2

class Rectangle (Shape):  # Inherits Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) :    # method implementation or override
        return self.width * self.height

def calculate_area(shape): # common method to calculate area based on a shape. Here is a Polymorphism - same method for different classes
    return shape.area()

# Create instances of Circle and Rectangle
my_circle = Circle(5)
my_rectangle = Rectangle(4,5)


# Calculate and print areas using polymorphism
print(f"Cicle area : {calculate_area(my_circle)}")
print(f"Rectangle area : {calculate_area(my_rectangle)}")