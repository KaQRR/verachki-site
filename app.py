from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Добро пожаловать в культ Верочки!</h1><p>Она следит за тобой.</p>"

if __name__ == "__main__":
    app.run(debug=True)
