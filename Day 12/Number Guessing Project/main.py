from random import randint
import art

EASY_LEVEL = 15
HARD_LEVEL = 7


def check_answer(user_guess, actual, times):
    """Checks answer against guess, Returns the number of turns remaining."""
    if user_guess < actual:
        print("Too low. ")
        return times - 1
    elif user_guess > actual:
        print("Too high. ")
        return times - 1
    else:
        print(f"You got it! The answer was {actual}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    else:
        set_difficulty()


def game():
    print(art.logo)
    answer = randint(1, 100)

    print("Guessing Game")
    print("number between 1-100")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


game()