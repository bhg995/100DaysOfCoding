print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


if tip == 10:
    newbill = bill * 1.1
elif tip == 12:
    newbill = bill * 1.12
elif tip == 15:
    print("Thanks Yo")
    newbill = bill * 1.15
else:
    print("You don't like the service hunh?")
    newbill = bill * 1.05

totalbill = newbill
totalbill /= people

print("Total bill:","{:.2f}".format(totalbill), "¢$€£")
