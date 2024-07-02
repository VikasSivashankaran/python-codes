dict1={1: 10, 2: 20, 3: 30}
sum_List=[]
for i in dict1:
    sum_List.append(i + dict1[i])
print(*sum_List)