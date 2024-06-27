list = [1, 2, 3]
#Output: [(1, 1), (2, 8), (3, 27)]

r=[(val,val**3)for val in list]
print(r)