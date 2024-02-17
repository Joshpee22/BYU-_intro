import random

def initialize_game():
    words = ["mosiah", "nephi", "helaman", "alma", "ether"]
    secret_word = random.choice(words)
    return secret_word.lower()

def generate_initial_hint(word):
    return "_" * len(word)

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
    attempts = 0
    hint = generate_initial_hint(secret_word)

    print("Welcome to the Word Guessing Game!")

    while True:
        guess = input(f"\nGuess the word: {hint}\nYour guess: ").lower()

        if len(guess) != len(secret_word):
            print("Your guess must have the same number of letters as the secret word.")
            continue

        attempts += 1

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {attempts} {'attempt' if attempts == 1 else 'attempts'}.")
            break

        hint = provide_hint(secret_word, guess)
        print(f"Hint: {hint}")

if __name__ == "__main__":
    play_game()

