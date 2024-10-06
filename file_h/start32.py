try:
    num = int(input("Enter a number: "))  # May raise ValueError
    result = 10 / num                       # May raise ZeroDivisionError
except ValueError as e:
    print(f"Invalid input: {e}")
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
finally:
    print("Execution completed.")