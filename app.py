from flask import Flask, render_template, request
from hashbreaker import crack
import os

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
    # Use Render's assigned port or default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
