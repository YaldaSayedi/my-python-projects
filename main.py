
print("Welcome to the rollercoaster! ")
height= int(input("What is your height?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age= int(input("What is your age? ?"))
    if age >= 18:
        print("You should pay 10$")
    else:
        print("You should pay 5$")

else:
    print("I am sorry but you can not ride the rollercoaster!")