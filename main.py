from art import logo


# Calculator Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2

operators ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "%": modulus,
}

print(logo)

def calculation():
    num1 = float(input("What is your first number?: "))
    for symbol in operators:
        print(symbol)
    should_continue = True
    while should_continue:
        operator_symbols = input("Pick an operator: ")
        num2 = float(input("What is next number?: "))
        calculator_function = operators[operator_symbols]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operator_symbols} {num2} is {answer}")

        if input(f"Type 'y' to calculate with {answer} or Type 'n' to restart calculation \n" ).lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculation()

calculation()