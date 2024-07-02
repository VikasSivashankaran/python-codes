lists=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List",lists)
dict=list(filter(lambda x: x % 2 ==0,lists))
print("Even numbers from list:",dict)