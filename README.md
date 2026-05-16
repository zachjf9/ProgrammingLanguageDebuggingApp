# ProgrammingLanguageDebuggingApp
Code is becoming more AI generated, this way programmers will understand how their code works and how they can fix it themselves if they encounter a problem

## Python Debugging App

A Flask app for learning Python syntax by debugging small, premade broken programs. Each challenge gives the learner bugged code, a place to submit a fix, and a three-step hint path:

1. Narrow the line range.
2. Name the bug type.
3. Show the exact fix direction.

After a correct answer, the app unlocks an explanation of why the bug breaks the code.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```

Then open `http://127.0.0.1:5000`.
