from flask import Flask, render_template, request
import pandas as pd
from model import recommend_freelancers

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    error = None

    if request.method == "POST":
        try:
            skills = request.form.get("skills", "")
            budget = float(request.form.get("budget", 0))
            timeline = int(request.form.get("timeline", 0))

            if not skills.strip():
                error = "Please enter required skills."
            elif budget <= 0:
                error = "Please enter a valid budget."
            else:
                recommendations = recommend_freelancers(skills, budget, timeline)

        except ValueError:
            error = "Please enter valid numbers for budget and timeline."
        except Exception as e:
            error = f"An unexpected error occurred: {str(e)}"

    return render_template("index.html", recommendations=recommendations, error=error)

if __name__ == "__main__":
    app.run(debug=True)
