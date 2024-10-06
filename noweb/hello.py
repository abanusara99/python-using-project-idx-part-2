from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_abanu_sara():
    return 'Hello, ABAnuSara!'

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)