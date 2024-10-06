class BankAccount:
    """A class to represent a bank account."""

    def __init__(self, account_holder, initial_balance=0):
        """Initialize the account with the holder's name and an initial balance."""
        self.account_holder = account_holder  # Instance attribute for account holder's name
        self.balance = initial_balance          # Instance attribute for the balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Current balance: ${self.balance:.2f}")

# Main Block to Execute the Script
if __name__ == "__main__":
    # Create a new bank account for John Doe with an initial balance of $1000
    account = BankAccount("John Doe", 1000)

    # Check the initial balance
    account.check_balance()

    # Deposit money
    account.deposit(500)

    # Withdraw money
    account.withdraw(200)

    # Attempt to withdraw more than the current balance
    account.withdraw(1500)

    # Check the final balance
    account.check_balance()
