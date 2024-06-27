s = input("Enter the string: ")
ss = s.split()

for i in ss:
    if len(i) % 2 == 0:
        print(i)
