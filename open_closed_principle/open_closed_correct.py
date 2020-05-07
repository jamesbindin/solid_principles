# Now each shape class has their own implementation for calculating area. the shape object is passed to the
# AreaCalculator constructor. this makes the program open to extension because it it easy to add another shape.
# The program is closed to modification because the current program logic does not need to be changed to be extended.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print("Area of Rectangle:", self.height * self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print("Area of Circle:", self.radius * self.radius *3.14)

class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def calculate(self):
        self.shape.calculate_area()


a = AreaCalculator(Circle(3))
a.calculate()
