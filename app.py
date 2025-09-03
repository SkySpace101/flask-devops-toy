from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    content = "this world is so amazing and it is just is 🌍🌍🌌"
    return f"Hello, DevOps World! and {content} 🚀"

@app.route("/greet/:id")
def hi(id):
    return f"Hello, {id}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 