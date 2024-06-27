def divisible(a):
    if a % 2 == 0 and a%3==0 and a%4==0:
        print("num is divisible by 2,3 and 4")
    elif a%2==0 and a%3==0:
        print("divisible of 2 and 3")
    elif a%3==0 and a%4==0:
        print("divisible of 3 and 4")
    elif a%2==0 and a%4==0:
        print("divisible of 2 and 4")
    elif a%2==0:
        print("divisible of 2")
    
    elif a%3==0:
        print("divisible of 3")
    elif a%4==0:
        print("divisible of 4")
    else:
        print("can't divisible")
num=int(input())
divisible(num)