import random
import hangman_art
import hangman_words

print(hangman_art.logo)
live= 6
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder= ""
for position in chosen_word:
    placeholder = "_ "
    print(placeholder, end= "")
game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{live}/6 LIVES LEFT****************************")
    guess = input("\nEnter your guess: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display= ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in  correct_letters:
             display += letter
        else:
            display += "_ "
    print("word to guess:", display)
    if guess not in correct_letters:
        live -= 1
        print(f"You guessed {guess}, that's not in the word :(")
        if live == 0:
            game_over = True
            print(f"*********************** It Was {chosen_word} YOU LOSE!**********************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(hangman_art.stages[live])

