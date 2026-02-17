from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/display")
def display():
    tasks = []
    with open("tasks.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return render_template("display.html", tasks=tasks)

@app.route("/input", methods=["GET", "POST"])
def input_task():
    if request.method == "POST":
        # TODO: Read form data from request.form
        # TODO: Add a datetime stamp
        # TODO: Append the new task to tasks.csv using csv.DictWriter
        # TODO: Redirect to the display page
        pass
    return render_template("input.html")

if __name__ == "__main__":
    app.run(debug=True)
