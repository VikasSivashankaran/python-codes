while True:
    n=input("enter 'exit' to come out of loop:").strip()#strip is used to prompts the user to enter a string and removes any leading or trailing whitespace from the input.
    if n.lower()=='exit':
        break
    else:
        print(n)
print("teminate")