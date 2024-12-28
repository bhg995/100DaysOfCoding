# My solution
print("Welcome to Python Pizza Deliveries!")
print("\nSmall pizza (S): $15 \nMedium pizza (M): $20 \nLarge pizza (L): $25 "
      "\n\nAdd pepperoni for small pizza: +$2 \nAdd pepperoni for medium or large pizza: +$3 "
      "\nAdd extra cheese for any size pizza: +$1")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
    if pepperoni == "Y" and extra_cheese ==  "Y":
        bill += 3
    elif pepperoni == "Y" and extra_cheese == "N":
        bill += 2
    elif pepperoni == "N" and extra_cheese == "Y":
        bill += 1
    else:
        bill = bill
elif size == "M":
    bill = 20
    if pepperoni == "Y" and extra_cheese == "Y":
        bill += 4
    elif pepperoni == "Y" and extra_cheese == "N":
        bill += 3
    elif pepperoni == "N" and extra_cheese == "Y":
        bill += 1
    else:
        bill = bill
elif size == "L":
    bill = 25
    if pepperoni == "Y" and extra_cheese == "Y":
        bill += 4
    elif pepperoni == "Y" and extra_cheese == "N":
        bill += 3
    elif pepperoni == "N" and extra_cheese == "Y":
        bill += 1
    else:
        bill = bill

print(f"Your final bill is: ${bill}")


# Instructors solution
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You have chosen an invalid size.")
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")