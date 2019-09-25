from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

class_roster = [
    ('Sabrina', 'A', 'Junior'),
    ('Dilpreet', 'A', 'Junior'),
    ('Grace', 'A', 'Junior'),
    ('Bob', 'B', 'Senior'),
    ('Drake', 'B+', 'Sophomore'),
    ('George', 'C', 'Freshman'),
    ('Emma', 'C', 'Senior'),
    ('Sarah', 'D', 'Sophomore'),
    ('Thomas', 'D', 'Freshman'),
    ('Jake', 'A', 'Senior'),
    ('Parker', 'B', 'Freshman'),
    ('Jacob', 'C', 'Sophomore')
]
@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", grade_view=grade_view,class_roster=class_roster)

if __name__ == "__main__":
    app.run()
