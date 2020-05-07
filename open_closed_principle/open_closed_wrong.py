# open-closed principle:
#    software entities classes, functions etc should be open for extension and closed for modification.

# The example below violates this principle. if you wanted to extend the behaviour of the programme by adding
# another shape, you would need to modify the AreaCalculator class.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def calculate(self):
        if isinstance(self.shape, Rectangle):
            print(self.shape.height * self.shape.width)
        elif isinstance(self.shape, Circle):
            print(self.shape.radius * self.shape.radius * 3.14)

a = AreaCalculator(Circle(3))
a.calculate()