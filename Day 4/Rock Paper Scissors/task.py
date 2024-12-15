import random

# My solution
choice = ["rock", "paper", "scissors"]
numb = len(choice)
randomChoice = random.randint(0, numb-1)

play = input("rock, paper or scissors\n")

if choice[randomChoice] == play:
    print("it's a tie")
elif choice[randomChoice] == "rock" and play == "scissors":
    print("computer wins")
elif choice[randomChoice] == "scissors" and play == "paper":
    print("Computer wins")
elif choice[randomChoice] == "paper" and play == "rock":
    print("Computer wins")

elif choice[randomChoice] == "scissors" and play == "rock":
    print("You win")
elif choice[randomChoice] == "paper" and play == "scissors":
    print("You win")
elif choice[randomChoice] == "rock" and play == "paper":
    print("You win")

# Instructor's solution
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# choices= [rock, paper, scissors]
# choice = int(input("Choose 0 for rock, 1 for paper or 2 scissors: "))
# print("you chose: \n" + choices[choice])
# randomChoice = random.randint(0,2)
#
# computerChoice = randomChoice
# print("Computer chose: " + choices[computerChoice])
# print(randomChoice)
#
# if choice > 2 or choice < 0:
#     print("Too high or low")
# elif choice == 0 and computerChoice == 2:
#     print("You win!")
# elif computerChoice == 0 and choice == 2:
#     print("You lose!")
# elif choice > computerChoice:
#     print("You win")
# elif choice < computerChoice:
#     print("You lose")
# elif choice == computerChoice:
#     print("It's a tie")
