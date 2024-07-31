def shout(text):
    return text.upper()
print(shout("hello"))

yell = shout

print(yell("hello"))

def whisper(text):
    return text.lower()
print(whisper("helloo"))

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("""function created as argument""")
    print(greeting)
greet(shout)
greet(whisper)

def create_adder(x):
    return create_adder

add_15 = create_adder(15)

print(add_15(10))
