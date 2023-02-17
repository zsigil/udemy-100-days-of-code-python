logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("What type of operation would you like to do? Choose from above: ")

    num2 = float(input("What is the second number? "))

    function = operations[operation_symbol]
    answer = function(num1, num2)
    print(f"{str(num1)} {operation_symbol} {str(num2)} = {answer}")

    should_continue = True

    while should_continue:
        num3 = float(input("What is the next number? "))
        operation_symbol = input("What type of operation would you like to do? Choose from above: ")
        function = operations[operation_symbol]
        oldanswer = answer
        answer = function(answer, num3)
        print(f"{str(oldanswer)} {operation_symbol} {str(num3)} = {answer}")

        check_continue = input("Do you want to continue? press 'y' for yes, press 'n' to start new calculation, any other to quit ")
        if check_continue == 'n':
            should_continue = False
            calculator()
        elif check_continue != 'y':
            should_continue = False

calculator()