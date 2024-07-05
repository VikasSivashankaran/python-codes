class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area_circle(self):
        return 3.142857142857143 * self.radius * self.radius
    
    def calculate_perimeter_circle(self):
        return 2 * 3.142857142857143 * self.radius
    
radius = float(input("Enter the Radius of Circle:"))

Circle = Circle(radius)

area = Circle.calculate_area_circle()

perimeter = Circle.calculate_perimeter_circle()
print("Area of Circle is: ",area)

print("Perimeter of Circle:",perimeter)