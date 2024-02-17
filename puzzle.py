import random

def initialize_game():
    words = ["mosiah", "nephi", "helaman", "alma", "ether"]
    secret_word = random.choice(words)
    return secret_word.lower()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter.upper()
        else:
            display += "_"
    return display

def provide_hint(secret_word, guess):
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i]
        else:
            hint += "_"
    return hint

def play_game():
    secret_word = initialize_game()
    guessed_letters = []
    attempts = 0

    print("Welcome to the Word Puzzle Game!")

    while True:
        guess = input(f"\nGuess the word: {display_word(secret_word, guessed_letters)}\nYour guess: ").lower()

        if len(guess) != len(secret_word):
            print("Your guess must have the same number of letters as the secret word.")
            continue

        attempts += 1

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {attempts} attempts.")
            break

        hint = provide_hint(secret_word, guess)
        print(f"Hint: {hint}")

if __name__ == "__main__":
    play_game()

