from flask import Flask, render_template, request
from hashbreaker import crack

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        hash_input = request.form.get("hash_input")
        result = crack(hash_input)
        if not result:
            result = "Hash not found or unsupported type"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
