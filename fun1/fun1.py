from flask import Flask

app = Flask(__name__)

# Function Declaration
def greet_user(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Route Declaration
@app.route('/greet/<name>')
def greet(name):
    """Greet the user with their name."""
    return greet_user(name)

# Main Block to Run the Application
if __name__ == "__main__":
    app.run(debug=True)