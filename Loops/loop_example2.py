'''
Get a number input and print all 
the values from 1 to the number 
but skip values that are divisible 
by 10 - using continue
'''



n=int(input("enter the number:"))
for i in range(1,n+1):
    if i%10==0:
        continue
    print(i)
    