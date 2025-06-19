print(10 > 100)
print(7 < 10)
print(100 == 100)
print("Sam" == "Sam")
print("sam" == "Sam")
print(10 >= 5)
print(11 <= 6)
print(2 != 4)

print(10 > 7 or 10 == 7)
print(2 == 3 and 4 < 6)
print(not(2 == 2))

if (10 < 5):
    print("Yesss!")
elif (10 == 3):
    print("Maybe")
elif (10 == 10):
    print("I don't know")
else: 
    print("Noooo!")


if(3 > 6 or 10 != 10):
    print("Yess!")
else:
    print("Nooo!")


if(not True):
    print("Yesss!")
else:
    print("Nooo")



age = int(input("Enter your age: "))

if (age == 21):
    print("You are at the right age to drink. Don't go wild!")

elif (age > 21):
    print("You are eligible to drink")

else:
    print("You are too young to drink")