
print("Welcome to Python pizza delivery")
pizza_size = input("What size of pizza do you want? S, M or L")
Pepperoni = input("Do you want pepperoni on your Pizza? Y or N")
Extra_cheese = input("Do you want extra cheese? Y or N")

bill= 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

if Pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3
if Extra_cheese == "Y":
    bill += 1

print("Your final bill is" + str(bill))





