from flask import Flask, render_template, request, session, redirect, url_for
import os



app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session tracking

import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
conn.close()


@app.route("/")
def welcome():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("home"))
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session["username"] = username
            return redirect(url_for("home"))
        return "Invalid credentials. Please try again."
    return render_template("login.html")



@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("home.html")



# Route: Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("welcome"))




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

questions3 = [
    {
        "question": "What type of elements typically form ionic bonds?",
        "options": ["Two metals", "A metal and a non-metal", "Two non-metals", "Metals only"],
        "answer": "A metal and a non-metal"
    },
    {
        "question": "What charge does a sodium ion (Na⁺) have?",
        "options": ["Positive", "Negative", "Neutral", "Variable"],
        "answer": "Positive"
    },
    {
        "question": "What charge does a chloride ion (Cl⁻) have?",
        "options": ["Positive", "Negative", "Neutral", "Variable"],
        "answer": "Negative"
    },
    {
        "question": "What holds ions together in an ionic compound?",
        "options": ["Magnetic force", "Covalent bonding", "Electrostatic attraction", "Gravitational force"],
        "answer": "Electrostatic attraction"
    },
    {
        "question": "Which of the following is an example of an ionic compound?",
        "options": ["CO₂", "H₂O", "NaCl", "O₂"],
        "answer": "NaCl"
    },
    {
        "question": "Why do ionic compounds have high melting points?",
        "options": ["They are made of large atoms", "They have strong electrostatic forces", "They contain weak bonds", "They are always in gaseous form"],
        "answer": "They have strong electrostatic forces"
    },
    {
        "question": "What happens to electrons in an ionic bond?",
        "options": ["They are shared equally", "They are transferred from one atom to another", "They remain unchanged", "They form a sea of delocalized electrons"],
        "answer": "They are transferred from one atom to another"
    },
        {
        "question": "What is an ion?",
        "options": ["An atom with extra protons", "An atom that has gained or lost electrons", "A neutral atom", "A molecule"],
        "answer": "An atom that has gained or lost electrons"
    },
    {
        "question": "What is the difference between an atom and an ion?",
        "options": ["Atoms have a charge, ions do not", "Ions have gained or lost electrons, atoms are neutral", "Atoms are only found in metals", "Ions do not exist in nature"],
        "answer": "Ions have gained or lost electrons, atoms are neutral"
    },
    {
        "question": "Why do noble gases not form ionic bonds?",
        "options": ["They already have a full outer shell", "They are too small", "They do not exist in nature", "They are always in liquid form"],
        "answer": "They already have a full outer shell"
    }

]






@app.route("/quiz1", methods=["GET", "POST"])
def quiz1():
    if "score1" not in session:
        session["score1"] = 0
        session["question_index1"] = 0

    question_index = session["question_index1"]

    if question_index >= len(questions):
        return render_template("quiz1.html", question=None, score=session["score1"], total=len(questions), quiz_title="Group 1 Alkali Metals Quiz")

    question = questions[question_index]
    feedback = None  # Initialize feedback to prevent reference errors

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer:
            feedback = "Incorrect!"
            if selected_answer == question["answer"]:
                session["score1"] += 1
                feedback = "Correct!"
            
            session["question_index1"] += 1
            session["feedback1"] = feedback
            session.modified = True
            return redirect(url_for("quiz1"))

    return render_template("quiz1.html", question=question, score=session["score1"], total=len(questions), feedback=session.get("feedback1"))






@app.route("/quiz2", methods=["GET", "POST"])
def quiz2():
    if "score2" not in session:
        session["score2"] = 0
        session["question_index2"] = 0

    question_index = session["question_index2"]

    if question_index >= len(questions2):
        return render_template("quiz2.html", question=None, score=session["score2"], total=len(questions2), quiz_title="Group 7 The Halogens")

    question = questions2[question_index]

    @app.route("/quiz2", methods=["GET", "POST"])
    def quiz2():
        if "score2" not in session:
            session["score2"] = 0
        session["question_index2"] = 0

    question_index = session["question_index2"]

    if question_index >= len(questions2):
        return render_template("quiz2.html", question=None, score=session["score2"], total=len(questions2), quiz_title="Group 7 The Halogens")

    question = questions2[question_index]
    feedback = None

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer:
            feedback = "Incorrect!"
            if selected_answer == question["answer"]:
                session["score2"] += 1
                feedback = "Correct!"
            
            session["question_index2"] += 1
            session["feedback2"] = feedback
            session.modified = True
            return redirect(url_for("quiz2"))

    return render_template("quiz2.html", question=question, score=session["score2"], total=len(questions2), feedback=session.get("feedback2"))


    return render_template("quiz2.html", question=question, score=session["score2"], total=len(questions2))


@app.route("/quiz3", methods=["GET", "POST"])
def quiz3():
    if "score3" not in session:
        session["score3"] = 0
        session["question_index3"] = 0

    question_index = session["question_index3"]

    if question_index >= len(questions3):
        return render_template("quiz3.html", question=None, score=session["score3"], total=len(questions3), quiz_title="Ionic Bonding Quiz")

    question = questions3[question_index]
    feedback = None  # Initialize feedback to avoid reference errors

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer:  # Ensure a selection is made
            feedback = "Incorrect!"
            if selected_answer == question["answer"]:
                session["score3"] += 1
                feedback = "Correct!"
            
            session["question_index3"] += 1
            session["feedback3"] = feedback  # Store feedback in session
            session.modified = True
            return redirect(url_for("quiz3"))

    return render_template("quiz3.html", question=question, score=session["score3"], total=len(questions3), feedback=session.get("feedback3"))



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
    elif quiz == "quiz3":
        session.pop("score3", None)
        session.pop("question_index3", None)
        return redirect(url_for("quiz3"))
    return redirect(url_for("welcome"))

if __name__ == "__main__":
    app.run(debug=True)
