from flask import Flask, render_template, request, session, redirect, url_for
import os



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
        "question": "Which element is at the top of Group 7 in the periodic table?",
        "options": ["Fluorine", "Chlorine", "Bromine", "Iodine"],
        "answer": "Fluorine"
    },
    {
        "question": "What happens to the reactivity of halogens as you go down Group 7?",
        "options": ["It increases", "It decreases", "It stays the same", "It fluctuates"],
        "answer": "It decreases"
    },
    {
        "question": "Which halogen is a liquid at room temperature?",
        "options": ["Fluorine", "Chlorine", "Bromine", "Iodine"],
        "answer": "Bromine"
    },
    {
        "question": "What is the state of iodine at room temperature?",
        "options": ["Gas", "Liquid", "Solid", "Plasma"],
        "answer": "Solid"
    },
    {
        "question": "What color is chlorine gas?",
        "options": ["Red", "Green", "Purple", "Yellow"],
        "answer": "Green"
    },
    {
        "question": "What type of bonding do halogens form in diatomic molecules?",
        "options": ["Ionic", "Metallic", "Covalent", "Hydrogen"],
        "answer": "Covalent"
    },
    {
        "question": "Which halogen is the most reactive?",
        "options": ["Fluorine", "Chlorine", "Bromine", "Iodine"],
        "answer": "Fluorine"
    },
    {
        "question": "What is the general trend in boiling points of halogens down the group?",
        "options": ["They increase", "They decrease", "They stay the same", "They fluctuate randomly"],
        "answer": "They increase"
    },
    {
        "question": "Which halogen is commonly used in disinfectants and bleach?",
        "options": ["Fluorine", "Chlorine", "Bromine", "Iodine"],
        "answer": "Chlorine"
    },
    {
        "question": "What is formed when halogens react with metals?",
        "options": ["Metal oxides", "Metal halides", "Metal carbonates", "Metal nitrates"],
        "answer": "Metal halides"
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

    return render_template("index.html", question=question, score=session["score1"], total=len(questions), progress=session["question_index1"], quiz_title="Group 1 Alkali Metals Quiz")




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

    return render_template("index.html", question=question, score=session["score2"], total=len(questions2), progress=session["question_index2"], quiz_title="Group 7 The Halogens")




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
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
