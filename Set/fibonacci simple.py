n=10
n1=0
n2=1
next=n2
count=0

while count<=n:
    print(next,end='')
    count+=1
    n1,n2=n2,next
    next=n1+n2
    print()