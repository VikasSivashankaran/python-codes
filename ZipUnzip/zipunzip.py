# Python3 code to demonstrate
# Unzip a list of tuples
# using list comprehension

# initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]

# Printing original list
print("Original list is : " + str(test_list))

# using list comprehension to
# perform Unzipping
res = [[i for i, j in test_list],
	[j for i, j in test_list]]

# Printing modified list
print("Modified list is : " + str(res))


# Python3 code to demonstrate
# Unzip a list of tuples
# using zip() and * operator

# Initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4), ('Hello')]

# Printing original list
print("Original zip list is : " + str(test_list))

# Performing unzipping
# using zip() and * operator
res = list(zip(*test_list))

# Printing modified list
print("Modified zip list is : " + str(res))

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]

roll_no = [4, 1, 3, 2]

marks = [40, 50, 60, 70]

# using zip() to map values

mapped = zip(name, roll_no, marks)

# converting values to print as set

mapped = set(mapped)

# printing resultant values

print("The zipped result is : ", end="")

print(mapped)

namz, roll_noz, marksz = zip(*mapped)

print("The name list is : ", end="")

print(namz)

print("The roll_no list is : ", end="")

print(roll_noz)

print("The marks list is : ", end="")

print(marksz)