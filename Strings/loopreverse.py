#a. Using loop
ins=input("enter the string:")
os=""
for i in range(len(ins)-1,-1,-1):
    os+=ins[i]
print("reverse string",os)


