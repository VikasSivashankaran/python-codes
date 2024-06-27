ele=[45,'helo',78,74]
print(ele)
if len(ele)>1:
    ele[0],ele[-1]=ele[-1],ele[0]
    print(ele)