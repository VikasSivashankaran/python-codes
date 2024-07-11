'''Method overriding is an ability of any 
object-oriented programming language that 
allows a subclass or child class to provide 
a specific implementation of a method that 
is already provided by one of its 
super-classes or parent classes. '''

class Parent():
    def __init__(self):
        self.value = "Inside the parent"
    def show(self):
        print(self.value)

class Child():
    def __init__(self) :
        self.value = "Inside the Child"
    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
