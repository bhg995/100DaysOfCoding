import random
from art import logo


def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    draw = random.choice(cards)
    return draw


def calculate(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(uzer, cpu):
    """Compares the user score u_score against the computer score c_score."""
    if uzer == cpu:
        return "Draw 🙃"
    elif cpu == 0:
        return "Lose, opponent has Blackjack 😱"
    elif uzer == 0:
        return "Win with a Blackjack 😎"
    elif uzer > 21:
        return "You went over. You lose 😭"
    elif cpu > 21:
        return "Opponent went over. You win 😁"
    elif uzer > cpu:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    finish = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not finish:
        user_score = calculate(user_cards)
        computer_score = calculate(computer_cards)
        print(f"Your cards, {user_cards}, current score: {user_score}")
        print(f"Computers card, {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            finish = True
        else:
            user_should = input("Type y to get another card, or n to pass: ")
            if user_should == "y":
                user_cards.append(deal_card())
            else:
                finish = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate(computer_cards)

    print(user_cards, compare(user_score, computer_score), computer_cards)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
