# Functions with outputs and calculator program

# Add
def add(n1, n2):
    return n1 + n2
# Subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What is your first number: "))
for operator in operators:
    print(operator)

should_continue = True
while should_continue:
    select_operator = input("Pick an operation: ")
    num2 = int(input("What is your next number: "))
    calculation_function = operators[select_operator]
    answer = calculation_function(num1, num2)

    print(f"{num1} {select_operator} {num2} = {answer}")


    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
        num1 = answer
    else:
        should_continue = False













