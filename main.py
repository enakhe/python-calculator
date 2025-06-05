user_name = input("Enter your name: ")
message = f"\nWelcome {user_name}, to our calculator app\n"
print(message)

num_one = input("Enter first number to add: ")
num_two = input("Enter second number to add: ")

result = int(num_one) + int(num_two)

answer = f"\nThe addition of {num_one} and {num_two} is {result}\n"
print(answer)