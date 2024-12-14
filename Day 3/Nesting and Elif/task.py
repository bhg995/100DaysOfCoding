print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Children ticket, $5 please")
    elif age >= 12 and age < 18:
        print("Teenager ticket, $7 please")
    else:
        print("Adult ticket, $12 please")
else:
    print("Sorry you have to grow taller before you can ride.")