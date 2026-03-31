
print("Welcome to the rollercoaster! ")
height= int(input("What is your height?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age= int(input("What is your age?"))
    if age < 12:
        bill= 5
        print("Your ticket cost it 5$")
    elif age <= 18:
        bill= 10
        print("Your ticket cost is 10$")
    else:
        bill= 12
        print("Your ticket cost is 12$")
    wants_photo= input("Do you want a photo taken? Y or N?")
    if wants_photo.upper() == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("I am sorry but you can not ride the rollercoaster!")