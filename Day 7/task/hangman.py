import  random, hangman_words

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
word_length = len(chosen_word)
lives = 5
display = []
print(f"Hangman. Try to guess: {chosen_word}."
      f"\nYou'll get {lives} times to try it out")
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input(f"\nWhat's your guess? ")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print("You guessed right")
            print(letter)
            display[position] = letter
    if guess not in chosen_word:
        print("You've guessed wrong")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You've lost")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Won")

