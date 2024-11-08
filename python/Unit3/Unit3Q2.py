#Inheritance and Method Overriding
#Implement an inheritance example with a base class Shape and a derived class Rectangle that overrides the area method. 

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):  
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

r = Rectangle(10, 5)
print("Area of Rectangle:",r.area())