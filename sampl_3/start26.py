# Function Declaration / Define
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

# Main Block to Execute the Script
if __name__ == "__main__":
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Call the function and store the result
    result = add_numbers(num1, num2)
    
    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")