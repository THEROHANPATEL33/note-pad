from flask import Flask, render_template, request

app = Flask(__name__)
notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("note")
        if content:
            notes.append(content)
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
