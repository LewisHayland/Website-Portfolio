from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def aboutme():
    return render_template("About Me.html")

@app.route("/")
def contact():
    return render_template("Contact.html")

if __name__ == "__main__":
    app.run(debug=True)