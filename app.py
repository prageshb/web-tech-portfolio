from flask import Flask, render_template
import sqlite3

app = Flask(__name__)




@app.route("/")
def home ():
    return render_template('index.html')


@app.route("/resume")
def resume ():
    return render_template('resume.html')

@app.route("/about")
def about ():
    return render_template("about.html")

@app.route("/dashboard")
def contact ():
    return render_template('dashboard.html')

if __name__ == "__main__" :
    app.run(debug= True)


