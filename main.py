from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def landingpage():
    return render_template("index.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/blog/1")
def blog1():
    return render_template("blog-single.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/faq/")
def faq():
    return render_template("faq.html")

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
