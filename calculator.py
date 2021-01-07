# assignment: programming assignment 3
# author: Reed Warren
# date: 11/16/2020
# file: calculator.py is a program that calculates anything you throw at it!
# input: numbers
# output: numbers
def isfloat(token):
    dot = False
    minus = False
    for char in token:
        if char.isdigit():  # allow many digits in a string
            continue
        elif char == ".":  # allow only one dot in a string
            if not dot:
                dot = True
            else:
                return False
        elif char == "-" and token[0] == "-":  # allow one minus in front
            if not minus:
                minus = True
            else:
                return False
        else:  # do not allow any other characters in a string
            return False
    return True


def format(num, precision=2):
    num = str(round(num, precision))
    while (num[-1] == "0" or num[-1] == ".") and not (num == '-0') and not num.isdigit():
        num = num[0:len(num) - 1]
    if num == "-0":
        num = "0"
    return num


def add(a, b):
    c = a + b
    return f"{format(a)} + {format(b)} = {format(c)}"


def subtract(a, b):
    c = a - b
    return f"{format(a)} - {format(b)} = {format(c)}"


def multiply(a, b):
    c = a * b
    return f"{format(a)} x {format(b)} = {format(c)}"


def divide(a, b):
    c = a / b
    return f"{format(a)} / {format(b)} = {format(c)}"


done = False
print("Welcome to Calculator Program!")
while not done:
    operation = str(input(
        "Please choose one of the following operations:" + "\nAddition - A " + "\nSubtraction - S" +
        "\nMultiplication - M" + "\nDivision - D" + "\n>\n"))
    if operation == "A" or operation == "a":
        print("You chose addition.")
    elif operation == "S" or operation == "s":
        print("You chose subtraction.")
    elif operation == "M" or operation == "m":
        print("You chose multiplication.")
    else:
        print("You chose division.")

    num1 = input("Please enter the first number:\n")
    while not isfloat(num1):
        print("You did not choose a number.\n")
        num1 = input("Please enter the first number:\n")
    print(f"The first number is {format(float(num1))}.")
    num2 = input("Please enter the second number:\n")
    while not isfloat(num2):
        print("You did not choose a number.\n")
        num2 = input("Please enter the second number:\n")
    print(f"The second number is {format(float(num2))}.\n")

    if operation == "A" or operation == "a":
        print(add(float(num1), float(num2)))
    elif operation == "S" or operation == "s":
        print(subtract(float(num1), float(num2)))
    elif operation == "M" or operation == "m":
        print(multiply(float(num1), float(num2)))
    else:
        if num2 == "0":
            print("The division by zero is prohibited!\n")
        else:
            print(divide(float(num1), float(num2)))
    again = input("Do you want to continue? [Y/N]:\n")
    if again == "N" or again == "n":
        done = True
print("Goodbye!")
