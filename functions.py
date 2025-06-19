def greeting(name):
    print("Hello World")
    print (f"My name is {name}")

def upper_name(name):
    return name.upper()

def lower_name(name):
    return name.lower()

def length_of_name(name):
    return len(name)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

def power(x, y):
    return x ** y

def celsius_to_fahrenheit(c):
    return c * (9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

answer = celsius_to_fahrenheit(100)
print(answer)

result = fahrenheit_to_celsius(100)
print(result)

# user_name = input("Enter your name: ")
# uppercased_name = upper_name(user_name)
# greeting(uppercased_name)

# print(add(100, 54))