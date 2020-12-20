import random

def generate_number():
    return random.randint(1, 101)

def user_number():
    return int(input("Make a guess: "))

def compare(random_number, user_guess):
    if random_number == user_guess:
        return "Wow, you win."
    elif random_number > user_guess:
        return f"{user_guess} is Too Low"
    elif random_number < user_guess:
        return f"{user_guess} is Too High"

def play_game():
    is_game_over = False
    random_number = generate_number()
    print("Welcome to the NUMBER GUESSING GAME")
    print("I am thinking of a number between 1 and 100")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty_level == "easy":
        print(f"You have 10 attempts remaining to guess the number")
        lives = 10
    elif difficulty_level == "hard":
        print(f"You have 5 attempts remaining to guess the number")
        lives = 5

    while not is_game_over:
        user_guess = user_number()
        print(compare(random_number, user_guess))
        if user_guess != random_number:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
            if lives == 0:
                print("You lose")
                is_game_over = True
        if random_number == user_guess:
            is_game_over = True

play_game()


