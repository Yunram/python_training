#Creating hangman game
import random
import stages_page

word_list = ["apple", "baboon", "camel", "ramilia", "madagascar", "america", "tanzania"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#TODO-1: - Create an empty List called display.
display = []
for letter in range(word_length):
    display.append("_")
print(f"The word is: {' '.join(display)}\nYou have a 6 lives. Good luck!")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter:\n").lower()
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
    if guess in chosen_word and "_" not in display:
        print(f"Congrats. Your word is {chosen_word}")
    elif guess in chosen_word:
        print(f"You are right. Our word has that letter: {' '.join(display)}")
    else:
        print(f"This letter not in our word. Try ones more. {' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        print(stages_page.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")
    if "_" not in display:
        end_of_game = True
        print("You win")
