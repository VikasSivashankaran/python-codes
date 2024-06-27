#Reverse a number 123456789
n=123456789
s=0
while n>0:
    a=n%10
    s=s*10+a
    print(s)
    n=n//10
    print(n)
print(s)