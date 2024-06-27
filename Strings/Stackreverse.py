ins=input("enter string to reverse:")
stack=[]

for i in ins:
    stack.append(i)
rs=""
while stack:
    rs+=stack.pop()
print(rs)