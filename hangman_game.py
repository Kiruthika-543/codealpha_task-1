import random

# Step 1: Predefined list of 5 words
words = ["apple", "banana", "grape", "cherry", "orange"]
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Step 2: Game loop
print("Welcome to Hangman!")
print("_ " * len(word_to_guess))

while incorrect_guesses < max_guesses:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} tries left.")

    # Display the current guessed word
    current_state = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            current_state += letter + " "
        else:
            current_state += "_ "
    print(current_state.strip())

    # Check for win
    if all(letter in guessed_letters for letter in word_to_guess):
        print("Congratulations! You guessed the word correctly.")
        break
else:
    print(f"Game Over! The word was '{word_to_guess}'. Better luck next time.")
