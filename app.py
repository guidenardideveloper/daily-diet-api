from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
