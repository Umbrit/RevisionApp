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

questions2 = [
    {
        "question": "What is the pH of a neutral solution?",
        "options": ["0", "7", "14", "1"],
        "answer": "7"
    },
    {
        "question": "Which ion is responsible for acidity in solutions?",
        "options": ["OH⁻", "Na⁺", "H⁺", "Cl⁻"],
        "answer": "H⁺"
    },
    {
        "question": "What is the name of the substance that neutralizes an acid?",
        "options": ["Salt", "Base", "Water", "Metal"],
        "answer": "Base"
    },
    {
        "question": "What products are formed when an acid reacts with a metal carbonate?",
        "options": ["Salt and water", "Salt and carbon dioxide", "Salt, water, and carbon dioxide", "Salt and hydrogen"],
        "answer": "Salt, water, and carbon dioxide"
    },
    {
        "question": "What is the general word equation for a reaction between an acid and an alkali?",
        "options": ["Acid + Metal → Salt + Hydrogen", "Acid + Alkali → Salt + Water", "Acid + Carbonate → Salt + Water + Carbon Dioxide", "Acid + Oxygen → Water"],
        "answer": "Acid + Alkali → Salt + Water"
    },
    {
        "question": "What color does universal indicator turn in a strong acid?",
        "options": ["Blue", "Green", "Red", "Purple"],
        "answer": "Red"
    },
    {
        "question": "Which of these substances is an alkali?",
        "options": ["Hydrochloric acid", "Sulfuric acid", "Sodium hydroxide", "Carbon dioxide"],
        "answer": "Sodium hydroxide"
    },
    {
        "question": "What type of reaction occurs when an acid and a base react together?",
        "options": ["Oxidation", "Neutralization", "Combustion", "Precipitation"],
        "answer": "Neutralization"
    },
    {
        "question": "What is the name of the salt formed when hydrochloric acid reacts with sodium hydroxide?",
        "options": ["Sodium sulfate", "Sodium nitrate", "Sodium chloride", "Sodium carbonate"],
        "answer": "Sodium chloride"
    },
    {
        "question": "Which gas is produced when a metal reacts with an acid?",
        "options": ["Oxygen", "Carbon dioxide", "Hydrogen", "Chlorine"],
        "answer": "Hydrogen"
    }
]




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz1", methods=["GET", "POST"])
def quiz1():
    if "score1" not in session:
        session["score1"] = 0
        session["question_index1"] = 0

    question_index = session["question_index1"]

    if question_index >= len(questions):  
        return render_template("index.html", question=None, score=session["score1"], total=len(questions), quiz_title="Group 1 Alkali Metals Quiz")

    question = questions[question_index]

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer == question["answer"]:
            session["score1"] += 1
        session["question_index1"] += 1
        session.modified = True  
        return redirect(url_for("quiz1"))

    return render_template("index.html", question=question, score=session["score1"], total=len(questions), quiz_title="Group 1 Alkali Metals Quiz")



@app.route("/quiz2", methods=["GET", "POST"])
def quiz2():
    if "score2" not in session:
        session["score2"] = 0
        session["question_index2"] = 0

    question_index = session["question_index2"]

    if question_index >= len(questions2):  
        return render_template("index.html", question=None, score=session["score2"], total=len(questions2), quiz_title="Group 7 The Halogens")

    question = questions2[question_index]

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer == question["answer"]:
            session["score2"] += 1
        session["question_index2"] += 1
        session.modified = True  
        return redirect(url_for("quiz2"))

    return render_template("index.html", question=question, score=session["score2"], total=len(questions2), quiz_title="Group 7 The Halogens")



@app.route("/restart/<quiz>")
def restart(quiz):
    if quiz == "quiz1":
        session.pop("score1", None)
        session.pop("question_index1", None)
        return redirect(url_for("quiz1"))
    elif quiz == "quiz2":
        session.pop("score2", None)
        session.pop("question_index2", None)
        return redirect(url_for("quiz2"))
    return redirect(url_for("home"))  # Redirect to home if no quiz is specified



if __name__ == "__main__":
    app.run(debug=True)
