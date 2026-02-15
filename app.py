from flask import Flask, render_template, request
from detector import analyze_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        email_text = request.form["email"]
        score, level, bar, reasons = analyze_email(email_text)
        result = {
            "score": score,
            "level": level,
            "bar": bar,
            "reasons": reasons
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
