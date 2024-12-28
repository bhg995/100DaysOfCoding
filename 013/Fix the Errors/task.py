# To fix
#age = int(input("How old are you?"))
#if age > 18:
#print("You can drive at age {age}.")

# Fixes & small upgrades
legal_age = 18
age = int(input("How old are you? "))
if age >= 18:
    print("You can drive")
    print(f"You can drive legally at age {legal_age} in most countries.")
elif 16 <= age < 18:
    print("Hang in there")
elif 14 <= age < 16:
    print("You can try scooters for now")
else:
    print(f"Stick with bicycles young person at the age of {age}")