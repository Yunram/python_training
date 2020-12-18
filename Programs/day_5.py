# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome ti the Password Generator by Ramis")
ch_letter = int(input("Please type how many letters do you like in your password?\n"))
ch_symbols = int(input("Please type how many symbols would you like?\n"))
ch_number = int(input("Please type how many number would you like?\n"))

password_list = []
for i in range(1, ch_letter + 1):
    password_list += random.choice(letters)

for i in range(1, ch_symbols + 1):
    password_list += random.choice(symbols)

for i in range(1, ch_number + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print("Your new password: " + password)


