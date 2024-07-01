def contains_all_vowels(s):
    vowels = set("aeiou")
    found_vowels = set()

    for char in s.lower():
        if char in vowels:
            found_vowels.add(char)
    
    return vowels == found_vowels

# Example usage
input_string = input("Enter a string: ")
if contains_all_vowels(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
