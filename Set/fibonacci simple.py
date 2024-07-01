'''n=10
n1=0
n2=1
next=n2
count=0

while count<=n:
    print(next,end='')
    count+=1
    n1,n2=n2,next
    next=n1+n2
    print()'''

def fibonacci(n):
    if n<0:
        print("invalid")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))
   
     
    
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Example usage
n = 10
fib_series = [fibonacci(i) for i in range(n)]
print("Fibonacci series up to", n, ":", fib_series)
