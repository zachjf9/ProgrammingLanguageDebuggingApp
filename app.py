import random
import re

from flask import Flask, redirect, render_template, request, session, url_for

from problems import PROBLEMS


app = Flask(__name__)
app.secret_key = "dev-debugging-app-secret"

LANGUAGES = [
    {"name": "Python", "slug": "python", "available": True},
    {"name": "JavaScript", "slug": "javascript", "available": False},
    {"name": "Java", "slug": "java", "available": False},
    {"name": "C++", "slug": "cpp", "available": False},
    {"name": "Ruby", "slug": "ruby", "available": False},
    {"name": "Go", "slug": "go", "available": False},
]


def normalize_code(code):
    trimmed_lines = [line.rstrip() for line in code.strip().splitlines()]
    collapsed_blank_lines = re.sub(r"\n{3,}", "\n\n", "\n".join(trimmed_lines))
    return collapsed_blank_lines.strip()


def problems_for_language(language):
    return [
        problem
        for problem in PROBLEMS
        if problem["language"].lower() == language.lower()
    ]


def current_problem(language):
    problem_id = session.get("problem_id")
    if problem_id is None:
        return None
    return next(
        (
            problem
            for problem in problems_for_language(language)
            if problem["id"] == problem_id
        ),
        None,
    )


def choose_problem(language):
    language_problems = problems_for_language(language)
    if not language_problems:
        return None

    previous_id = session.get("problem_id")
    choices = [
        problem for problem in language_problems if problem["id"] != previous_id
    ]
    problem = random.choice(choices or language_problems)
    session["problem_id"] = problem["id"]
    session["selected_language"] = language
    session["hint_level"] = 0
    session["solved"] = False
    session.pop("last_answer", None)
    session.pop("feedback", None)
    return problem


@app.route("/")
def index():
    return render_template("landing.html", languages=LANGUAGES)


@app.route("/practice/<language>")
def practice(language):
    if not problems_for_language(language):
        return redirect(url_for("index"))

    session["selected_language"] = language
    problem = current_problem(language) or choose_problem(language)
    hint_level = session.get("hint_level", 0)
    hints = [
        problem["line_range"],
        problem["bug_type"],
        problem["fix_hint"],
    ][:hint_level]

    return render_template(
        "practice.html",
        problem=problem,
        hints=hints,
        hint_level=hint_level,
        solved=session.get("solved", False),
        feedback=session.get("feedback"),
        last_answer=session.get("last_answer", problem["bugged_code"]),
        languages=LANGUAGES,
        selected_language=language,
        total_problems=len(problems_for_language(language)),
    )


@app.post("/check")
def check_answer():
    language = session.get("selected_language", "python")
    problem = current_problem(language) or choose_problem(language)
    answer = request.form.get("answer", "")
    session["last_answer"] = answer

    accepted = {normalize_code(problem["fixed_code"])}
    accepted.update(normalize_code(candidate) for candidate in problem["accepted_answers"])

    if normalize_code(answer) in accepted:
        session["solved"] = True
        session["feedback"] = "Correct. Nice debugging."
    else:
        session["feedback"] = "Not quite yet. Run the code in your head and try one smaller change."

    return redirect(url_for("practice", language=language))


@app.post("/hint")
def reveal_hint():
    language = session.get("selected_language", "python")
    session["hint_level"] = min(session.get("hint_level", 0) + 1, 3)
    return redirect(url_for("practice", language=language))


@app.post("/next")
def next_problem():
    language = session.get("selected_language", "python")
    choose_problem(language)
    return redirect(url_for("practice", language=language))


if __name__ == "__main__":
    app.run(debug=True)
