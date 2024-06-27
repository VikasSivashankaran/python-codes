
def swapPositions(lis, pos1, pos2):
	temp=lis[pos1]
	lis[pos1]=lis[pos2]
	lis[pos2]=temp
	return lis
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))
#code 2
def swap(liss,poss1,poss2):
	tempp=liss[poss1]
	liss[poss1]=liss[poss2]
	liss[poss2]=tempp
	return liss
lisst=[1,2,3,4]
poss1,poss2=1,3
print(swap(lisst,poss1-1,poss2-1))