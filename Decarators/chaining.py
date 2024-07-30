def decarator1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decarator2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decarator1
@decarator2
def num1():
    return 10

@decarator2
@decarator1
def num2():
    return 10


print(num1())
print(num2())