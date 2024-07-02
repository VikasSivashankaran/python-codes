
def merge(dict1,dict2):
    res={**dict1,**dict2}
    return res

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = merge(dict1,dict2)
print("after merging :",dict3)



