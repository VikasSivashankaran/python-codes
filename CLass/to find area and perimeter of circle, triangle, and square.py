class shape():
    
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class circle(shape):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.142857142857143 * self.radius**2
    
    def perimeter(self):
        return super().perimeter()

a = float(input("enter the radius for circle"))
Circle=circle(a)   

print("Area of Circle: ",Circle.area())

print