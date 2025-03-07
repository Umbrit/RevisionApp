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




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/password-protected", methods=["GET", "POST"])
def password_page():
    correct_password = "admin123"  # Change this to your preferred password

    if request.method == "POST":
        entered_password = request.form.get("password")
        if entered_password == correct_password:
            session["is_admin"] = True  # Store session state for admin access
            return redirect(url_for("admin_page"))  # Redirect to Admin Page
        else:
            return render_template("password.html", error="Incorrect password, try again.")

    return render_template("password.html")  # Render password input page

import random

import random
import time  # Import time to track resets

import random
import time

import random
import time

@app.route("/admin", methods=["GET", "POST"])
def admin_page():
    if not session.get("is_admin"):
        return redirect(url_for("password_page"))  # Redirect if not logged in as admin

    # Check if the balance needs to reset every hour
    if "money" not in session or "last_reset" not in session:
        session["money"] = 100
        session["last_reset"] = time.time()
    else:
        elapsed_time = time.time() - session["last_reset"]
        if elapsed_time > 3600:  # 1 hour
            session["money"] = 100
            session["last_reset"] = time.time()
            session.modified = True  # Save session changes

    result = None
    win_message = None
    bet_amount = 0
    redeem_message = None  # Message for redeeming code

    # Slot Machine Logic
    symbols = ["🍒", "🍋", "🍉", "⭐", "💎"]
    payouts = {
        "🍒🍒🍒": 5,
        "🍋🍋🍋": 10,
        "🍉🍉🍉": 20,
        "⭐⭐⭐": 50,
        "💎💎💎": 100
    }

    if request.method == "POST":
        if "redeem" in request.form:  # Check if they entered a redeem code
            redeem_code = request.form.get("redeem_code")
            if session["money"] == 0 and redeem_code == "GET100":  # Only works if money is 0
                session["money"] = 100
                redeem_message = "✅ You received 100 coins!"
                session.modified = True
            else:
                redeem_message = "❌ Invalid code or you still have coins."

        else:  # Otherwise, process the slot machine bet
            bet_amount = int(request.form.get("bet"))

            if bet_amount > session["money"] or bet_amount <= 0:
                win_message = "Invalid bet! Check your balance."
            else:
                session["money"] -= bet_amount  # Deduct bet
                spin = random.choices(symbols, k=3)  # Random symbols
                spin_result = "".join(spin)

                if spin_result in payouts:
                    winnings = bet_amount * payouts[spin_result]  # Calculate winnings
                    session["money"] += winnings
                    win_message = f"🎉 You won {winnings} coins!"
                else:
                    session["money"] += bet_amount // 2  # Give back half bet if they lose
                    win_message = f"❌ No match! You lost {bet_amount // 2} coins."

                session.modified = True  # Update session

        result = locals().get("spin_result", None)  # Fix to prevent UnboundLocalError

    return render_template("admin.html", money=session["money"], result=result, win_message=win_message, redeem_message=redeem_message)

@app.route("/logout-admin")
def logout_admin():
    session.pop("is_admin", None)  # Remove admin session
    return redirect(url_for("home"))  # Redirect back to home page



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


@app.route("/quiz3", methods=["GET", "POST"])
def quiz3():
    if "score3" not in session:
        session["score3"] = 0
        session["question_index3"] = 0

    question_index = session["question_index3"]

    if question_index >= len(questions3):  
        return render_template("index.html", question=None, score=session["score3"], total=len(questions3), quiz_title="Ionic Bonding Quiz")

    question = questions3[question_index]

    if request.method == "POST":
        selected_answer = request.form.get("answer")
        if selected_answer == question["answer"]:
            session["score3"] += 1
        session["question_index3"] += 1
        session.modified = True  
        return redirect(url_for("quiz3"))

    return render_template("index.html", question=question, score=session["score3"], total=len(questions3), progress=session["question_index3"], quiz_title="Ionic Bonding Quiz")


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
    return redirect(url_for("home"))  # Redirect to home if no quiz is specified




if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
