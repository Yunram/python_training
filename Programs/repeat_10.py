# Calculator

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = float(input("Type first number: "))

    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        chosen_operation = input("Pick an operation: ")
        next_num = float(input("Type next number: "))

        calculation_function = operations[chosen_operation]
        answer = calculation_function(num1, next_num)

        print(f"{num1} {chosen_operation} {next_num} = {answer}")

        if input(f"Do you want to continue calculation with {answer}? 'y' or 'n': ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

