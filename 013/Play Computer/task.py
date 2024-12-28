year = int(input("What's your year of birth?"))

#if year > 1980 and year < 1994: # less than 1994, not 1994
#    print("You are a millennial.")
#elif year > 1994:               # more than 1994, not 1994
#    print("You are a Gen Z.")

# Fix
if year > 1980 and year <= 1994: # here <= 1994
    print("You are a millennial.")
elif year > 1994:                # OR here >= 1994
    print("You are a Gen Z.")
