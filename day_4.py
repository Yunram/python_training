import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n")
print("YOUR CHOSE:")

if your_choice == "0":
    print(rock)
elif your_choice == "1":
    print(paper)
elif your_choice == "2":
    print(scissors)
else:
    print("Carefully read instruction above")

list_ch = [rock, paper, scissors]
computer_choice = random.choice(list_ch)
print("COMPUTER CHOSE:")
print(computer_choice)

if your_choice == "0" and computer_choice == rock:
    print("DRAW")
elif your_choice == "0" and computer_choice == paper:
    print("YOU LOSE")
elif your_choice == "0" and computer_choice == scissors:
    print("YOU WON")
elif your_choice == "1" and computer_choice == rock:
    print("YOU WON")
elif your_choice == "1" and computer_choice == paper:
    print("DRAW")
elif your_choice == "1" and computer_choice == scissors:
    print("YOU LOSE")
elif your_choice == "2" and computer_choice == rock:
    print("YOU LOSE")
elif your_choice == "2" and computer_choice == paper:
    print("YOU WON")
elif your_choice == "2" and computer_choice == scissors:
    print("DRAW")
else:
    print("Something gone wrong")
