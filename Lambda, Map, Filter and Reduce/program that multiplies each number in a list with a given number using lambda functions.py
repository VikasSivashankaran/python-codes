list1 = [2, 4, 6, 9, 11]
n = 2
res = list(map(lambda number: number * n, list1))
print(''.join(map(str, res)))
