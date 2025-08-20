"""
Calculator Module

A simple calculator module that provides basic arithmetic operations.
This module contains functions for addition, subtraction, multiplication, 
and division operations with proper error handling.

Author: Team Demo
Purpose: Demonstrate basic arithmetic operations for team collaboration
"""


def add(x, y):
    """
    Add two numbers together.
    
    Args:
        x (float): The first number to add
        y (float): The second number to add
        
    Returns:
        float: The sum of x and y
        
    Example:
        >>> add(5, 3)
        8
        >>> add(-2, 7)
        5
    """
    return x + y

def subtract(x, y):
    """
    Subtract the second number from the first number.
    
    Args:
        x (float): The number to subtract from (minuend)
        y (float): The number to subtract (subtrahend)
        
    Returns:
        float: The difference of x and y (x - y)
        
    Example:
        >>> subtract(10, 3)
        7
        >>> subtract(5, 8)
        -3
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers together.
    
    Args:
        x (float): The first number to multiply
        y (float): The second number to multiply
        
    Returns:
        float: The product of x and y
        
    Example:
        >>> multiply(4, 5)
        20
        >>> multiply(-3, 6)
        -18
    """
    return x * y

def divide(x, y):
    """
    Divide the first number by the second number.
    
    Args:
        x (float): The dividend (number to be divided)
        y (float): The divisor (number to divide by)
        
    Returns:
        float or str: The quotient of x and y, or error message if y is zero
        
    Raises:
        Returns error message string instead of raising exception for division by zero
        
    Example:
        >>> divide(15, 3)
        5.0
        >>> divide(10, 0)
        'Error: Division by zero'
    """
    # Handle division by zero
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main function to demonstrate calculator operations
def main():
    """
    Main function to demonstrate the calculator operations.
    
    This function serves as a demonstration of all four arithmetic operations
    using sample numbers. It showcases the functionality of add, subtract,
    multiply, and divide functions.
    
    The function uses predefined sample numbers (10 and 5) and prints the
    results of all operations to the console.
    
    Example output:
        10 + 5 = 15
        10 - 5 = 5
        10 * 5 = 50
        10 / 5 = 2.0
    """
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