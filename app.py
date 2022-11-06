from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def welcome():

    # the user has not filled out the quiz yet
    if request.method == "GET":
        return render_template("index-quiz.html")

    # the user has filled out the quiz
    if request.method == "POST":
        # the user has filled out the quiz and we want to display proper pathway resources
        # return render_template("propertemplate.html")
        first_answer = request.form.get("q1")
        second_answer = request.form.get("q2")
        third_answer = request.form.get("q3")
        schools = pd.read_csv("T3Data.csv")
        schools = schools[schools["Grade"] == first_answer]
        schools = schools[schools["Time_Available"] == second_answer]
        schools = schools[schools["Finances"] == third_answer]
        schools["Cost of program"] = schools["Cost of program"].apply(
            lambda x: "$" + str(x) + ".00")
        schools["Average Salary Outcome"] = schools["Average Salary Outcome"].apply(
            lambda x: "$" + str(x) + "0")
        schools.rename(columns={"Cost(3 diff ranges, annual)": "Cost",
                       "Opportunity_Type": "Opportunity"}, inplace=True)

        if second_answer == "0-1 Year":
            return render_template("result_one_year.html", schools=schools)
        else:
            return render_template("result.html", schools=schools)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/news")
def news():
    return render_template("newsletter.html")


@app.route("/news/news2")
def news2():
    return render_template("newsletter.html")


@app.route("/espanol")
def espanol():
    return render_template("espanol.html")


@app.route("/resultados")
def resultados():
    return render_template("resultados.html")


@app.route("/index_quiz_spanish")
def index_quiz_spanish():
    return render_template("index_quiz_spanish.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
