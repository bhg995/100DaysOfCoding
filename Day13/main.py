'''
Debugging and stuff
'''

# To fix
#def my_function():
#    for i in range(1, 20):
#        if i == 20:
#            print("You got it")
#my_function()

# Fixes
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

def my_function1():
    for i in range(1, 20):
        i+=1
        if i == 20:
            print("You got it")
my_function1()

# Reproducing bug
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # Range too high and starts from "❷", never shows "❶" # . randint(0,5)
print(dice_images[dice_num])

# Millennial or not?
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

# To fix
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)

# Fix
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"The book would have total words of {total_words}")

# To fix
import random
import maths
#def mutate(a_list):
#    b_list = []
#    new_item = 0
#    for item in a_list:
#        new_item = item * 2
#        new_item += random.randint(1, 3)
#        new_item = maths.add(new_item, item)
#    b_list.append(new_item)
#    print(b_list)
#mutate([1, 2, 3, 5, 8, 13])

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)                 # indentation
    print(b_list)
mutate([1, 2, 3, 5, 8, 13])
