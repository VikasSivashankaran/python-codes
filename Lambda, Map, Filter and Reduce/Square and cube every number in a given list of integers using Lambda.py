lists=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List",lists)
dict=list(map(lambda x: x ** 2 ,lists))
print("Square numbers from list:",dict)

dict1=list(map(lambda x: x **3 ,lists))
print("Cube numbers from list :",dict1)