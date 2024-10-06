# Function for Addition
def add(a, b):
    """Return the sum of a and b."""
    return a + b

# Function for Subtraction
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

# Function for Multiplication
def multiply(a, b):
    """Return the product of a and b."""
    return a * b

# Function for Division
def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b

# Function for Modulus
def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        return "Cannot perform modulus by zero."
    return a % b

# Main Block to Execute the Script
if __name__ == "__main__":
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform calculations and print results
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    
    # Division and Modulus without exception handling
    division_result = divide(num1, num2)
    print(f"Division: {num1} / {num2} = {division_result}")

    modulus_result = modulus(num1, num2)
    print(f"Modulus: {num1} % {num2} = {modulus_result}")
