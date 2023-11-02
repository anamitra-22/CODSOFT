# Function to perform arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

# Main program loop
while True:
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {result}")
    else:
        print("Invalid choice. Please try again.")
