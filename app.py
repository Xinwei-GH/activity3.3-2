from flask import Flask

app = Flask(__Xinwei__)

@app.route("/")
def hello_world():
    return "<p>Hello, Xinwei!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)