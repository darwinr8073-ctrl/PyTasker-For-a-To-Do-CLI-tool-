
import datetime
import os
import platform
import random
import time


def welcome():
    print("=" * 50)
    print("       PYTHON SYSTEM MANAGEMENT PROJECT")
    print("=" * 50)
    print("Date:", datetime.datetime.now())
    print("Operating System:", platform.system())
    print("Python Version:", platform.python_version())
    print("=" * 50)


def system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print("System:", platform.system())
    print("Machine:", platform.machine())
    print("Hostname:", platform.node())
    print("Processor:", platform.processor())
    print("Current Directory:", os.getcwd())


def calculator():
    print("\n--- CALCULATOR ---")

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", a + b)
        elif operator == "-":
            print("Result:", a - b)
        elif operator == "*":
            print("Result:", a * b)
        elif operator == "/":
            print("Result:", a / b if b != 0 else "Cannot divide by zero")
        else:
            print("Invalid operator!")

    except ValueError:
        print("Please enter valid numbers.")


def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                print("Correct! Congratulations!")
                print("Attempts:", attempts)
                break

        except ValueError:
            print("Enter a valid number.")


def create_file():
    print("\n--- FILE CREATION ---")
    filename = input("Enter filename: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    content = input("Enter file content: ")

    try:
        with open(filename, "w") as file:
            file.write(content)

        print("File created successfully!")
        print("File location:", os.path.abspath(filename))

    except OSError as error:
        print("Error:", error)


def list_files():
    print("\n--- FILES AND DIRECTORIES ---")
    print("Current location:", os.getcwd())

    for item in os.listdir():
        print(item)


def countdown():
    print("\n--- COUNTDOWN TIMER ---")

    try:
        seconds = int(input("Enter countdown seconds: "))

        for remaining in range(seconds, 0, -1):
            print(remaining)
            time.sleep(1)

        print("Countdown completed!")

    except ValueError:
        print("Enter a valid number.")


def main():
    welcome()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. System Information")
        print("2. Calculator")
        print("3. Number Guessing Game")
        print("4. Create Text File")
        print("5. List Files")
        print("6. Countdown Timer")
        print("7. Exit")
        print("===============================")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            system_info()
        elif choice == "2":
            calculator()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            create_file()
        elif choice == "5":
            list_files()
        elif choice == "6":
            countdown()
        elif choice == "7":
            print("Thank you! Project closed.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
