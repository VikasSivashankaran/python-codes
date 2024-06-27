inputstring=input("Enter the string:")
seen=set()
result=[]
for i in inputstring:
    if i not in seen:
        seen.add(i)
        result.append(i)
        print("".join(result))
