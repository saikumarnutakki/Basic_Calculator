def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def process_choice(choice):
    if choice in ['1', '2', '3', '4']:
        num1 = get_float("Enter the first number: ")
        num2 = get_float("Enter the second number: ")

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice. Please select a valid operation.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        process_choice(choice)

if __name__ == "__main__":
    main()
