import random

def choose_random_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"]
    return random.choice(word_list)

def play_hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1

        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
    
    if "_" in display_word:
        print(f"Out of attempts! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
