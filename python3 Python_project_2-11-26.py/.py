
import datetime
import os
import platform
import random
import time

# ==========================================
#        PYTHON SYSTEM INFORMATION APP
# ==========================================

def show_welcome():
    print("=" * 50)
    print("       WELCOME TO PYTHON PROJECT")
    print("=" * 50)
    print("Date:", datetime.datetime.now().strftime("%d-%m-%Y"))
    print("Time:", datetime.datetime.now().strftime("%H:%M:%S"))
    print("Operating System:", platform.system())
    print("Python Version:", platform.python_version())
    print("=" * 50)


def system_information():
    print("\n--- SYSTEM INFORMATION ---")
    print("System:", platform.system())
    print("Computer Name:", platform.node())
    print("Architecture:", platform.machine())
    print("Processor:", platform.processor())
    print("Platform:", platform.platform())


def number_guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number (1-100): "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed it!")
                print("Attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")


def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator!")

    except ValueError:
        print("Please enter valid numbers.")


def create_file():
    print("\n--- CREATE A TEXT FILE ---")

    filename = input("Enter filename: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    content = input("Enter content: ")

    try:
        with open(filename, "w") as file:
            file.write(content)

        print("File created successfully!")
        print("Location:", os.path.abspath(filename))

    except OSError as error:
        print("Error creating file:", error)


def read_file():
    print("\n--- READ A TEXT FILE ---")

    filename = input("Enter filename: ")

    try:
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())

    except FileNotFoundError:
        print("File not found!")
    except OSError as error:
        print("Error:", error)


def show_directory():
    print("\n--- DIRECTORY INFORMATION ---")
    print("Current Directory:", os.getcwd())
    print("\nFiles and Folders:")

    for item in os.listdir():
        print("-", item)


def countdown():
    print("\n--- COUNTDOWN TIMER ---")

    try:
        seconds = int(input("Enter seconds: "))

        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1

        print("Time's up!")

    except ValueError:
        print("Enter a valid number.")


def main():
    show_welcome()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. System Information")
        print("2. Number Guessing Game")
        print("3. Calculator")
        print("4. Create Text File")
        print("5. Read Text File")
        print("6. Show Directory")
        print("7. Countdown Timer")
        print("8. Exit")
        print("=============================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            system_information()

        elif choice == "2":
            number_guessing_game()

        elif choice == "3":
            calculator()

        elif choice == "4":
            create_file()

        elif choice == "5":
            read_file()

        elif choice == "6":
            show_directory()

        elif choice == "7":
            countdown()

        elif choice == "8":
            print("\nThank you for using this Python project!")
            print("Goodbye, DevOps Engineer!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
