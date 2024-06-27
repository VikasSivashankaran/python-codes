'''write a python program to add two numbers given below a=55 and b=22
    store the answer in a new variable
    multiply the answer with a 
    store the multiplied answer in new variable 
    compare the multiplied answer with value a 
    if the answer is greater then multiply the answer with (pi)value
    increment the answer by 34
    and decrement the answer by 20 
    then compare the value of all the present solution
'''
import math
a=55
b=22
c=a+b
print(c)
d=c*a
print(d)
if d>a:
    ma=d*math.pi
    print(ma)
    ma+=34
    print(ma)
    ma-=20
    print(ma)
    
