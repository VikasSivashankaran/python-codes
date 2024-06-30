'''Update each element in tuple list
The original list :[(1, 3, 4), (2, 4, 6), (3, 8, 1)]
Expected output - [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
'''

ele = 4
list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
res = [tuple(map(lambda x: x + ele, sub))for sub in list]
print("list after update", str(res))

