from abc import abstractmethod

class Polygon():

    @abstractmethod
    def no_of_sides(self):
        pass
class Triangle(Polygon):

    def no_of_sides(self):
        print("I have 3 slides")


class Hexagon(Polygon):
    def no_of_sides(self):
        print("I have 6 sides")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("I have 5 sides")



T=Triangle()
T.no_of_sides()

H=Hexagon()
H.no_of_sides()

P=Pentagon()
P.no_of_sides()