def pangram(s):
    alphabet=set("abcdefghijklmnopqrstuvwxyz")
    letters=set()
    for i in s.lower():
        if i in alphabet:
            letters.add(i)
    return alphabet==letters
    
input_string=input("enter the string:")
if pangram(input_string):
        print("the string is panagram")

else:
        print("the string is not panagram")