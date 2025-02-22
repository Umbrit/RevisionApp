from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session tracking

# Sample chemistry questions
questions = [
    {
        "question": "What is the chemical symbol for Sodium?",
        "options": ["Na", "S", "N", "So"],
        "answer": "Na"
    },
    {
        "question": "Which gas do plants use for photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is the pH of pure water?",
        "options": ["7", "1", "10", "14"],
        "answer": "7"
    },
    {
        "question": "Which element is a noble gas?",
        "options": ["Oxygen", "Nitrogen", "Neon", "Hydrogen"],
        "answer": "Neon"
    },
    {
        "question": "What is the chemical formula for water?",
        "options": ["H2O", "O2", "CO2", "H2O2"],
        "answer": "H2O"
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["Iron", "Mercury", "Lead", "Gold"],
        "answer": "Mercury"
    },
    {
        "question": "What is the charge of an electron?",
        "options": ["Positive", "Negative", "Neutral", "Variable"],
        "answer": "Negative"
    },
    {
        "question": "What gas do humans exhale?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Which of these is an alkali metal?",
        "options": ["Calcium", "Potassium", "Aluminium", "Silver"],
        "answer": "Potassium"
    },
    {
        "question": "What is the most abundant gas in Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"],
        "answer": "Nitrogen"
    }
]


@app.route("/", methods=["GET", "POST"])
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
