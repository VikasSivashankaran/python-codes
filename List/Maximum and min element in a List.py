
def getMinMax(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax

arr = [1,85,96,456,78,258,45]
minmax = getMinMax(arr)

print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])