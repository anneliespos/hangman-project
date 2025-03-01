import random
from art import stages, logo
from wordlist import word_list

print(logo)

random_word=random.choice(word_list)
blanks = "_" * len(random_word)
print(blanks)

game_over = False
correct_guesses = []
wrong_guesses = []
lives_left = 6          #you can make 6 wrong guesses before you hang

while not game_over:
    print(f"You have {lives_left}/6 lives left")
    user_input = input("Guess a letter: ").lower()
    if len(user_input) != 1:
        print("Guess a single letter please.")

    #Ensure the used input is a single letter
    if user_input in correct_guesses or wrong_guesses:
        print("You already guessed this letter, try another one!")

    display = ""

    for letter in random_word:
        if letter == user_input:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    if user_input not in random_word:
        wrong_guesses.append(user_input)
        print(f"Your guess {user_input} is not in the word, you lose a live...")
        lives_left-=1
        if lives_left <= 0:
            game_over = True
            print(f"You lose... The correct word was: {random_word}")

    print(display)
    print(stages[lives_left])

    if "_" not in display:
        game_over=True
        print("You win!")






