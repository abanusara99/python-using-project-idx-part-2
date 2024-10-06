from flask import Flask, request, render_template_string

# Create an instance of the Flask class
app = Flask(__name__)

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
            return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def check_balance(self):
        """Check the current balance of the account."""
        return f"Current balance: ${self.balance:.2f}"

# Create an instance of BankAccount for demonstration purposes
account = BankAccount("John Doe", 2000)  # Object name is 'account'

@app.route('/')
def index():
    return render_template_string('''
        <h1>Bank Account</h1>
        <form action="/deposit" method="post">
            <input type="number" name="amount" placeholder="Deposit Amount" required>
            <button type="submit">Deposit</button>
        </form>
        <form action="/withdraw" method="post">
            <input type="number" name="amount" placeholder="Withdraw Amount" required>
            <button type="submit">Withdraw</button>
        </form>
        <form action="/balance" method="get">
            <button type="submit">Check Balance</button>
        </form>
    ''')

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.form['amount'])
    message = account.deposit(amount)  # Using the 'account' object to call deposit method
    return render_template_string(f'''
        <h1>Bank Account</h1>
        <p>{message}</p>
        <a href="/">Go Back</a>
    ''')

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = float(request.form['amount'])
    message = account.withdraw(amount)  # Using the 'account' object to call withdraw method
    return render_template_string(f'''
        <h1>Bank Account</h1>
        <p>{message}</p>
        <a href="/">Go Back</a>
    ''')

@app.route('/balance', methods=['GET'])
def balance():
    message = account.check_balance()  # Using the 'account' object to check balance
    return render_template_string(f'''
        <h1>Bank Account</h1>
        <p>{message}</p>
        <a href="/">Go Back</a>
    ''')

# Main Block to Run the Application
if __name__ == "__main__":
    app.run(debug=True)