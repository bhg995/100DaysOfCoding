'''
is it < or > ?
'''

from art import logo, vs
from game_data import data
import random

print(logo)
score = 0


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



b = random.choice(data)
continuation = True

while continuation:
    a = b
    b = random.choice(data)
    if a == b:
        b = random.choice(data)
    print(f"Compare A: {format_data(a)}.")
    print(vs)
    print(f"Against B: {format_data(b)}.")

    guess = input("Who has more followers? Type 'a' or 'b': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = a["follower_count"]
    b_follower_count = b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"WRONG!! Congratulations, your score: {score}.")
        continuation = False


