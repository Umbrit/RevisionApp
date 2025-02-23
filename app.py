from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session tracking

# Sample chemistry questions
questions = [
    {
        "question": "Which element is the first in Group 1 of the periodic table?",
        "options": ["Lithium", "Sodium", "Potassium", "Rubidium"],
        "answer": "Lithium"
    },
    {
        "question": "What is a common property of all Group 1 alkali metals?",
        "options": ["They are gases", "They are highly reactive", "They are non-metals", "They have low density"],
        "answer": "They are highly reactive"
    },
    {
        "question": "Which alkali metal is found in table salt?",
        "options": ["Lithium", "Sodium", "Potassium", "Cesium"],
        "answer": "Sodium"
    },
    {
        "question": "What happens when alkali metals react with water?",
        "options": ["They dissolve silently", "They explode", "They form an acidic solution", "They produce hydrogen gas and an alkaline solution"],
        "answer": "They produce hydrogen gas and an alkaline solution"
    },
    {
        "question": "Which alkali metal is used in rechargeable batteries?",
        "options": ["Sodium", "Lithium", "Potassium", "Rubidium"],
        "answer": "Lithium"
    },
    {
        "question": "What color flame does potassium produce in a flame test?",
        "options": ["Red", "Yellow", "Lilac", "Green"],
        "answer": "Lilac"
    },
    {
        "question": "Why are alkali metals stored in oil?",
        "options": ["To keep them shiny", "To prevent them from reacting with air and water", "To make them easier to handle", "To increase their reactivity"],
        "answer": "To prevent them from reacting with air and water"
    },
    {
        "question": "Which alkali metal is the least reactive?",
        "options": ["Sodium", "Potassium", "Lithium", "Francium"],
        "answer": "Lithium"
    },
    {
        "question": "What is the trend in reactivity as you go down Group 1?",
        "options": ["It decreases", "It increases", "It stays the same", "It fluctuates"],
        "answer": "It increases"
    },
    {
        "question": "What is produced when sodium reacts with water?",
        "options": ["Oxygen and salt", "Hydrogen gas and sodium hydroxide", "Carbon dioxide and acid", "Chlorine gas"],
        "answer": "Hydrogen gas and sodium hydroxide"
    }
]



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if "score" not in session:
        session["score"] = 0
        session["question_index"] = 0

    question_index = session["question_index"]

    if question_index >= len(questions):  
        return render_template("index.html", question=None, score=session["score"], total=len(questions))

    question = questions[question_index]

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer == question["answer"]:
            session["score"] += 1
        session["question_index"] += 1
        session.modified = True  
        return redirect(url_for("quiz"))  # Redirect to refresh session data

    return render_template("index.html", question=question, score=session["score"], total=len(questions))

@app.route("/restart")
def restart():
    session.clear()  # Fully reset quiz progress
    return redirect(url_for("quiz"))


if __name__ == "__main__":
    app.run(debug=True)
