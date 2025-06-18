user_name = input("Enter your name: ")
message = f"\nWelcome {user_name}, to our calculator application\n"
print(message)

num_one = input("Enter the first number to subtract: ")
num_two = input("Enter the second number to subtract: ")
answer = int(num_one) - int(num_two);

result = f"\nThe subtracton of {num_one} and {num_two} is {answer}\n"

print(result)

