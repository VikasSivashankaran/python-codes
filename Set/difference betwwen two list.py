def list_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference = set1 - set2
    return list(difference)

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
difference=list_difference(list1,list2)
print("difference:",difference)