# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main function to demonstrate calculator operations
def main():
    # Sample numbers
    num1 = 10
    num2 = 5

    # Perform operations
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")

# Run the main function
if __name__ == "__main__":
    main()