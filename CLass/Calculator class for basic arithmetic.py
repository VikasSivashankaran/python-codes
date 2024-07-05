class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
    def multiple(self):
        return self.x * self.y
    
    def division(self):

        if self.y!=0:
            return self.x/self.y
        
        else:
            print("cannot divide")
    
a = int(input("enter first number:"))
b = int(input("enter second number:"))

calculator = Calculator(a, b)

resultadd = calculator.add()
print("Addition:",resultadd)

resultsub = calculator.sub()
print("Subraction:", resultsub)

resultmul = calculator.multiple()
print("Multiplication:", resultmul)

resultdiv = calculator.division()
print("Division:",resultdiv)
