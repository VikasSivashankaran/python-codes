'''Count frequency of List Items using Dictionary
List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
'''
List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
dic={}
for i in List1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
