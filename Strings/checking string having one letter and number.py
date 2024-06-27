def letter_and_number(s):
    letter=any(c.isalpha() for c in s)
    number=any(c.isnumeric() for c in s)
    return letter and number
s=input("enter the string with letter and number:")
if letter_and_number(s):
    print("input string contains letter and number")
else:
    print("input string does not contains letter and number")