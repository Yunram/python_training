#Creating hangman game
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1: - Create an empty List called display.
display = []
for letter in range(word_length):
    display.append("_")
print(f"The word is: {' '.join(display)}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

while "_" in display:
    guess = input("Guess a letter:\n").lower()
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
    if guess in chosen_word:
        print(f"You are right. Our word has that letter: {' '.join(display)}")
    else:
        print("This letter not in our word")

print("You win")
