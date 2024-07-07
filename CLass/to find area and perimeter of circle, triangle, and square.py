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
        return 2 * 3.142857142857143 * self.radius

print("\n")
a = float(input("enter the radius for circle: "))
Circle=circle(a)   

print("Area of Circle: ",Circle.area())
 
print("Perimeter of Circle: ",Circle.perimeter())

class triangle(shape):

    def __init__(self, a, b, c, h):
        self.a = a     #side 1 
        self.b = b     #side 2 or base
        self.c = c     #side 3
        self.h = h     #height
    
    def area(self):
        return 0.5 * self.b * self.h
    
    def perimeter(self):
        return self.a + self.b + self.c
    
print("\n")

a = float(input("enter the a for Triangle: "))
b = float(input("enter the b or base for Triangle: "))
c = float(input("enter the c for Triangle: "))
h = float(input("enter the height for Triangle: "))


Triangle = triangle(a,b,c,h)

print("Area of Triangle: ",Triangle.area())
 
print("Perimeter of Triangle: ",Triangle.perimeter())

class square(shape):

    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4 * self.side

print("\n")
a = float(input("enter the side for square: "))
Square=square(a)   

print("Area of Square: ",Square.area())
 
print("Perimeter of Square: ",Square.perimeter())