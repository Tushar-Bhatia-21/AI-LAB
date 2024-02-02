#hangman_game
import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "science", "developer", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Current word: {current_display}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Incorrect! Attempts left: {max_attempts - attempts}")
        
        if set(word_to_guess) == set(guessed_letters):
            print("Congratulations! You guessed the word.")
            break

    if set(word_to_guess) != set(guessed_letters):
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
