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

    return render_template("index.html", question=question, score=session["score"], total=len(questions))

# New route to restart the quiz
@app.route("/restart")
def restart():
    session.pop("score", None)
    session.pop("question_index", None)
    return redirect(url_for("quiz"))

if __name__ == "__main__":
    app.run(debug=True)
