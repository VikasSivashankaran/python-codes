from functools import reduce

def sum(d):
    return reduce(lambda x,y:x+y,d.values())

mydict={'a':100,'b':200,'c':300}
result= sum(mydict)

print("",result)