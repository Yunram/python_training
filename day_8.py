# import math
#
# def paint_calc(height, width, cover):
#     num_of_can = math.ceil(height * width / cover)
#     print(f"You'll need {num_of_can} cans of paint.")
#
# height = int(input("Type height of your wall: "))
# width = int(input("Type width of your wall: "))
# cover = 5
#
# paint_calc(height, width, cover)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

num = int(input("Please type number to check prime or not: "))
prime_checker(num)