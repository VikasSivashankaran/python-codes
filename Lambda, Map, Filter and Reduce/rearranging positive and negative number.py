arraynum1=[1, 2, -3, 5, 7, 8, -9, -10]
print(arraynum1)

result=sorted(arraynum1 ,key=lambda i:0 if i ==0 else -1/i)
print("after  rearranging :",result)