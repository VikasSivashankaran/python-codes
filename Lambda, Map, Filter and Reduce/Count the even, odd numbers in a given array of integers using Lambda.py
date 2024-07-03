arraynum1=[1, 2, 3, 5, 7, 8, 9, 10]

print("Original array",arraynum1)
odd_result=(list(filter(lambda x:(x%2!=0),arraynum1)))
print("odd list elements are :",odd_result,"\n And its length is :",len(odd_result))

even_result=(list(filter(lambda x:(x%2==0),arraynum1)))
print("even list elements are :",even_result,"\n And its length is :",len(even_result))
