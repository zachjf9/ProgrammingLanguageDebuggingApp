PROBLEMS = [
    {
        "id": "python-missing-colon",
        "language": "Python",
        "title": "The quiet loop",
        "prompt": "Fix the syntax error so the loop prints each task.",
        "bugged_code": """tasks = ["read", "trace", "fix"]

for task in tasks
    print(task)""",
        "fixed_code": """tasks = ["read", "trace", "fix"]

for task in tasks:
    print(task)""",
        "bug_line": 3,
        "line_range": "Look closely at lines 3-4.",
        "bug_type": "Missing colon after a Python block header.",
        "fix_hint": "Add a colon at the end of the for statement.",
        "accepted_answers": [
            """tasks = ["read", "trace", "fix"]

for task in tasks:
    print(task)"""
        ],
        "explanation": (
            "Python uses a colon to start the indented body of compound statements "
            "such as for loops, if statements, and function definitions. Without it, "
            "the interpreter cannot tell where the loop header ends and the loop body begins."
        ),
    },
    {
        "id": "python-assignment-condition",
        "language": "Python",
        "title": "The broken comparison",
        "prompt": "Fix the conditional so Python can compare the user's role.",
        "bugged_code": """role = "guest"

if role = "admin":
    print("Welcome, admin")
else:
    print("Welcome, guest")""",
        "fixed_code": """role = "guest"

if role == "admin":
    print("Welcome, admin")
else:
    print("Welcome, guest")""",
        "bug_line": 3,
        "line_range": "The issue is in lines 1-3.",
        "bug_type": "Assignment operator used where equality comparison is needed.",
        "fix_hint": "Use == inside the if condition.",
        "accepted_answers": [
            """role = "guest"

if role == "admin":
    print("Welcome, admin")
else:
    print("Welcome, guest")"""
        ],
        "explanation": (
            "Python uses = for assignment and == for equality comparison. Inside an if "
            "statement, Python expects an expression that can be evaluated as true or false. "
            "An assignment is a statement, so role = \"admin\" is invalid syntax there."
        ),
    },
    {
        "id": "python-list-index",
        "language": "Python",
        "title": "The runaway index",
        "prompt": "Fix the loop so it prints every score without crashing.",
        "bugged_code": """scores = [72, 86, 91]

for index in range(0, len(scores) + 1):
    print(scores[index])""",
        "fixed_code": """scores = [72, 86, 91]

for index in range(0, len(scores)):
    print(scores[index])""",
        "bug_line": 3,
        "line_range": "Focus on line 3.",
        "bug_type": "Off-by-one error in a range boundary.",
        "fix_hint": "Remove the + 1 so the final index is len(scores) - 1.",
        "accepted_answers": [
            """scores = [72, 86, 91]

for index in range(0, len(scores)):
    print(scores[index])""",
            """scores = [72, 86, 91]

for index in range(len(scores)):
    print(scores[index])""",
            """scores = [72, 86, 91]

for score in scores:
    print(score)""",
        ],
        "explanation": (
            "List indexes start at 0, so a three-item list has valid indexes 0, 1, and 2. "
            "range stops before its ending value, but len(scores) + 1 makes the loop try "
            "index 3, which raises an IndexError."
        ),
    },
    {
        "id": "python-missing-parenthesis",
        "language": "Python",
        "title": "The unfinished call",
        "prompt": "Fix the print call so the greeting can be displayed.",
        "bugged_code": """name = "Ada"
greeting = "Hello, " + name

print(greeting""",
        "fixed_code": """name = "Ada"
greeting = "Hello, " + name

print(greeting)""",
        "bug_line": 4,
        "line_range": "Inspect lines 3-4.",
        "bug_type": "Missing closing parenthesis.",
        "fix_hint": "Close the print call with a right parenthesis.",
        "accepted_answers": [
            """name = "Ada"
greeting = "Hello, " + name

print(greeting)"""
        ],
        "explanation": (
            "Function calls in Python must have matching parentheses. When the opening "
            "parenthesis after print is never closed, Python reaches the end of the line "
            "still expecting more call syntax and raises a SyntaxError."
        ),
    },
    {
        "id": "python-string-quote",
        "language": "Python",
        "title": "The split sentence",
        "prompt": "Fix the string so the print call is valid.",
        "bugged_code": """message = "Debugging teaches patience
print(message)""",
        "fixed_code": """message = "Debugging teaches patience"
print(message)""",
        "bug_line": 1,
        "line_range": "The problem is on line 1.",
        "bug_type": "Unterminated string literal.",
        "fix_hint": "Add the missing closing quote at the end of the message.",
        "accepted_answers": [
            """message = "Debugging teaches patience"
print(message)""",
            """message = 'Debugging teaches patience'
print(message)""",
        ],
        "explanation": (
            "A normal quoted string must close on the same line where it starts. Because "
            "the quote is missing, Python keeps scanning for the end of the string and reaches "
            "the next line instead, producing a syntax error before the program can run."
        ),
    },
]
