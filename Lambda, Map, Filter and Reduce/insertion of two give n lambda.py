arraynum1=[1, 2, 3, 5, 7, 8, 9, 10]
arraynum2=[1, 2, 4, 8, 9]

print("original array:")
print(arraynum1)
print(arraynum2)

result=list(filter(lambda x:x in arraynum1,arraynum2))

print("after insertion",result)