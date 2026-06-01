PYTHON_PROBLEMS = [
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
    {
        "id": "python-indentation-block",
        "language": "Python",
        "title": "The floating print",
        "prompt": "Fix the indentation so the message only prints for passing scores.",
        "bugged_code": """score = 88

if score >= 70:
print("Passing score")""",
        "fixed_code": """score = 88

if score >= 70:
    print("Passing score")""",
        "bug_line": 4,
        "line_range": "Look at lines 3-4.",
        "bug_type": "Missing indentation inside an if block.",
        "fix_hint": "Indent the print call under the if statement.",
        "accepted_answers": [
            """score = 88

if score >= 70:
    print("Passing score")"""
        ],
        "explanation": (
            "After a block header ending in a colon, Python expects an indented body. "
            "The unindented print line makes the if statement empty, so Python raises an "
            "IndentationError before it can run the code."
        ),
    },
    {
        "id": "python-name-error-variable",
        "language": "Python",
        "title": "The renamed total",
        "prompt": "Fix the variable name so the final total prints.",
        "bugged_code": """subtotal = 42
tax = 3
total = subtotal + tax

print(totals)""",
        "fixed_code": """subtotal = 42
tax = 3
total = subtotal + tax

print(total)""",
        "bug_line": 5,
        "line_range": "The mistake is on line 5.",
        "bug_type": "NameError from an undefined variable.",
        "fix_hint": "Use the same variable name that was assigned on line 3.",
        "accepted_answers": [
            """subtotal = 42
tax = 3
total = subtotal + tax

print(total)"""
        ],
        "explanation": (
            "Python variable names must match exactly. total and totals are different names, "
            "and totals was never assigned, so Python cannot find a value to print."
        ),
    },
    {
        "id": "python-string-number-concat",
        "language": "Python",
        "title": "The mixed message",
        "prompt": "Fix the print statement so the age can appear in the message.",
        "bugged_code": """age = 12

print("Age: " + age)""",
        "fixed_code": """age = 12

print("Age: " + str(age))""",
        "bug_line": 3,
        "line_range": "Focus on line 3.",
        "bug_type": "TypeError from adding a string and an integer.",
        "fix_hint": "Convert age to a string before concatenating.",
        "accepted_answers": [
            """age = 12

print("Age: " + str(age))""",
            """age = 12

print(f"Age: {age}")""",
            """age = 12

print("Age:", age)""",
        ],
        "explanation": (
            "The + operator can join two strings, but Python will not guess how to add a "
            "string and an integer. Converting the number or using an f-string makes the "
            "types clear."
        ),
    },
    {
        "id": "python-dict-key-quotes",
        "language": "Python",
        "title": "The unquoted key",
        "prompt": "Fix the dictionary lookup so it prints the user's name.",
        "bugged_code": """user = {"name": "Maya", "level": 2}

print(user[name])""",
        "fixed_code": """user = {"name": "Maya", "level": 2}

print(user["name"])""",
        "bug_line": 3,
        "line_range": "The issue is on line 3.",
        "bug_type": "Dictionary key written as a variable name.",
        "fix_hint": "Put quotes around the string key name.",
        "accepted_answers": [
            """user = {"name": "Maya", "level": 2}

print(user["name"])""",
            """user = {"name": "Maya", "level": 2}

print(user.get("name"))""",
        ],
        "explanation": (
            "Without quotes, name is treated as a variable. Since no variable named name "
            "exists, Python raises a NameError instead of looking up the string key."
        ),
    },
    {
        "id": "python-dict-missing-comma",
        "language": "Python",
        "title": "The crowded dictionary",
        "prompt": "Fix the dictionary syntax so both settings are stored.",
        "bugged_code": """settings = {
    "theme": "dark"
    "font_size": 16
}

print(settings)""",
        "fixed_code": """settings = {
    "theme": "dark",
    "font_size": 16
}

print(settings)""",
        "bug_line": 2,
        "line_range": "Inspect lines 2-3.",
        "bug_type": "Missing comma between dictionary items.",
        "fix_hint": "Add a comma after the first key-value pair.",
        "accepted_answers": [
            """settings = {
    "theme": "dark",
    "font_size": 16
}

print(settings)"""
        ],
        "explanation": (
            "Dictionary entries must be separated with commas. Without the comma, Python "
            "tries to read the next string as part of the same expression and the dictionary "
            "literal becomes invalid."
        ),
    },
    {
        "id": "python-list-method-append",
        "language": "Python",
        "title": "The vanishing list",
        "prompt": "Fix the append usage so the list still contains all tags.",
        "bugged_code": """tags = ["python", "syntax"]
tags = tags.append("debugging")

print(tags)""",
        "fixed_code": """tags = ["python", "syntax"]
tags.append("debugging")

print(tags)""",
        "bug_line": 2,
        "line_range": "The issue is on line 2.",
        "bug_type": "Assigning the result of a mutating list method.",
        "fix_hint": "Call append without assigning its return value.",
        "accepted_answers": [
            """tags = ["python", "syntax"]
tags.append("debugging")

print(tags)""",
            """tags = ["python", "syntax"]
tags = tags + ["debugging"]

print(tags)""",
        ],
        "explanation": (
            "append changes the list in place and returns None. Assigning that return value "
            "back to tags replaces the list with None, so the original list appears to vanish."
        ),
    },
    {
        "id": "python-function-return",
        "language": "Python",
        "title": "The silent helper",
        "prompt": "Fix the function so doubled receives the calculated value.",
        "bugged_code": """def double(number):
    number * 2

doubled = double(5)
print(doubled)""",
        "fixed_code": """def double(number):
    return number * 2

doubled = double(5)
print(doubled)""",
        "bug_line": 2,
        "line_range": "Look inside the function on line 2.",
        "bug_type": "Missing return statement.",
        "fix_hint": "Return the expression from the function.",
        "accepted_answers": [
            """def double(number):
    return number * 2

doubled = double(5)
print(doubled)"""
        ],
        "explanation": (
            "A function that does not return a value returns None automatically. The expression "
            "number * 2 is calculated and discarded unless return sends it back to the caller."
        ),
    },
    {
        "id": "python-function-argument-count",
        "language": "Python",
        "title": "The missing guest",
        "prompt": "Fix the function call so both names are available.",
        "bugged_code": """def introduce(first_name, last_name):
    print(first_name + " " + last_name)

introduce("Grace")""",
        "fixed_code": """def introduce(first_name, last_name):
    print(first_name + " " + last_name)

introduce("Grace", "Hopper")""",
        "bug_line": 4,
        "line_range": "The call on line 4 is missing something.",
        "bug_type": "Wrong number of function arguments.",
        "fix_hint": "Pass a second argument for last_name.",
        "accepted_answers": [
            """def introduce(first_name, last_name):
    print(first_name + " " + last_name)

introduce("Grace", "Hopper")""",
            """def introduce(first_name, last_name="Hopper"):
    print(first_name + " " + last_name)

introduce("Grace")""",
        ],
        "explanation": (
            "The function definition requires two inputs. Calling it with only one leaves "
            "last_name without a value, so Python raises a TypeError."
        ),
    },
    {
        "id": "python-loop-accumulator-reset",
        "language": "Python",
        "title": "The forgetful sum",
        "prompt": "Fix the loop so total keeps the sum of every number.",
        "bugged_code": """numbers = [2, 4, 6]

for number in numbers:
    total = 0
    total += number

print(total)""",
        "fixed_code": """numbers = [2, 4, 6]

total = 0
for number in numbers:
    total += number

print(total)""",
        "bug_line": 4,
        "line_range": "Inspect lines 3-5.",
        "bug_type": "Accumulator reset inside the loop.",
        "fix_hint": "Initialize total before the loop starts.",
        "accepted_answers": [
            """numbers = [2, 4, 6]

total = 0
for number in numbers:
    total += number

print(total)""",
            """numbers = [2, 4, 6]

print(sum(numbers))""",
        ],
        "explanation": (
            "Putting total = 0 inside the loop resets the sum during every iteration. "
            "The accumulator must be created before the loop so it can remember earlier values."
        ),
    },
    {
        "id": "python-while-counter",
        "language": "Python",
        "title": "The stuck countdown",
        "prompt": "Fix the while loop so it eventually stops.",
        "bugged_code": """count = 3

while count > 0:
    print(count)

print("Done")""",
        "fixed_code": """count = 3

while count > 0:
    print(count)
    count -= 1

print("Done")""",
        "bug_line": 4,
        "line_range": "Look inside the loop body, lines 3-4.",
        "bug_type": "Missing loop counter update.",
        "fix_hint": "Decrease count inside the while loop.",
        "accepted_answers": [
            """count = 3

while count > 0:
    print(count)
    count -= 1

print("Done")""",
            """count = 3

while count > 0:
    print(count)
    count = count - 1

print("Done")""",
        ],
        "explanation": (
            "A while loop repeats as long as its condition stays true. Since count never changes, "
            "count > 0 remains true forever and the loop does not reach the final print."
        ),
    },
    {
        "id": "python-boolean-case",
        "language": "Python",
        "title": "The lowercase truth",
        "prompt": "Fix the boolean value so the condition can run.",
        "bugged_code": """is_ready = true

if is_ready:
    print("Launch")""",
        "fixed_code": """is_ready = True

if is_ready:
    print("Launch")""",
        "bug_line": 1,
        "line_range": "The issue is on line 1.",
        "bug_type": "Boolean literal with the wrong capitalization.",
        "fix_hint": "Python booleans are True and False.",
        "accepted_answers": [
            """is_ready = True

if is_ready:
    print("Launch")"""
        ],
        "explanation": (
            "Python's boolean literals are capitalized. true is treated like a variable name, "
            "and because no variable named true exists, Python raises a NameError."
        ),
    },
    {
        "id": "python-none-case",
        "language": "Python",
        "title": "The empty result",
        "prompt": "Fix the empty value so the comparison is valid Python.",
        "bugged_code": """result = none

if result is None:
    print("No result yet")""",
        "fixed_code": """result = None

if result is None:
    print("No result yet")""",
        "bug_line": 1,
        "line_range": "Focus on line 1.",
        "bug_type": "None literal with the wrong capitalization.",
        "fix_hint": "Capitalize None.",
        "accepted_answers": [
            """result = None

if result is None:
    print("No result yet")"""
        ],
        "explanation": (
            "None is a special Python value and must be capitalized. none is just an ordinary "
            "name, so Python looks for a variable by that name and cannot find one."
        ),
    },
    {
        "id": "python-membership-test",
        "language": "Python",
        "title": "The backward membership test",
        "prompt": "Fix the condition so it checks whether the user has the admin role.",
        "bugged_code": """roles = ["editor", "admin", "viewer"]

if roles in "admin":
    print("Allowed")""",
        "fixed_code": """roles = ["editor", "admin", "viewer"]

if "admin" in roles:
    print("Allowed")""",
        "bug_line": 3,
        "line_range": "The condition on line 3 is reversed.",
        "bug_type": "Membership test written in the wrong direction.",
        "fix_hint": "Check whether the item is in the list, not whether the list is in the item.",
        "accepted_answers": [
            """roles = ["editor", "admin", "viewer"]

if "admin" in roles:
    print("Allowed")"""
        ],
        "explanation": (
            "The in operator reads naturally as item in collection. roles is a list, and "
            "\"admin\" is the item you want to find inside that list."
        ),
    },
    {
        "id": "python-slice-boundary",
        "language": "Python",
        "title": "The missing first item",
        "prompt": "Fix the slice so the first three names are selected.",
        "bugged_code": """names = ["Ada", "Grace", "Katherine", "Dorothy"]

first_three = names[1:3]
print(first_three)""",
        "fixed_code": """names = ["Ada", "Grace", "Katherine", "Dorothy"]

first_three = names[0:3]
print(first_three)""",
        "bug_line": 3,
        "line_range": "Focus on the slice on line 3.",
        "bug_type": "Slice starts at the wrong index.",
        "fix_hint": "Start the slice at index 0.",
        "accepted_answers": [
            """names = ["Ada", "Grace", "Katherine", "Dorothy"]

first_three = names[0:3]
print(first_three)""",
            """names = ["Ada", "Grace", "Katherine", "Dorothy"]

first_three = names[:3]
print(first_three)""",
        ],
        "explanation": (
            "List indexes start at 0. A slice of names[1:3] starts with the second item and "
            "stops before index 3, so it returns only Grace and Katherine."
        ),
    },
    {
        "id": "python-import-module",
        "language": "Python",
        "title": "The missing toolbox",
        "prompt": "Fix the code so it can use the math module.",
        "bugged_code": """radius = 4
area = math.pi * radius ** 2

print(area)""",
        "fixed_code": """import math

radius = 4
area = math.pi * radius ** 2

print(area)""",
        "bug_line": 2,
        "line_range": "The missing setup belongs before line 2.",
        "bug_type": "Module used before it is imported.",
        "fix_hint": "Import math before using math.pi.",
        "accepted_answers": [
            """import math

radius = 4
area = math.pi * radius ** 2

print(area)""",
            """from math import pi

radius = 4
area = pi * radius ** 2

print(area)""",
        ],
        "explanation": (
            "Python only knows names that have been defined or imported. math.pi cannot be "
            "resolved until the math module is imported."
        ),
    },
    {
        "id": "python-except-syntax",
        "language": "Python",
        "title": "The risky conversion",
        "prompt": "Fix the exception handler syntax.",
        "bugged_code": """value = "ten"

try:
    number = int(value)
except ValueError
    print("Please enter digits only")""",
        "fixed_code": """value = "ten"

try:
    number = int(value)
except ValueError:
    print("Please enter digits only")""",
        "bug_line": 5,
        "line_range": "Inspect lines 5-6.",
        "bug_type": "Missing colon after an except header.",
        "fix_hint": "Add a colon after ValueError.",
        "accepted_answers": [
            """value = "ten"

try:
    number = int(value)
except ValueError:
    print("Please enter digits only")"""
        ],
        "explanation": (
            "except starts a block just like if, for, and def. The colon tells Python that "
            "the indented handler body is about to begin."
        ),
    },
    {
        "id": "python-range-start",
        "language": "Python",
        "title": "The skipped zero",
        "prompt": "Fix the loop so it prints 0, 1, and 2.",
        "bugged_code": """for number in range(1, 3):
    print(number)""",
        "fixed_code": """for number in range(0, 3):
    print(number)""",
        "bug_line": 1,
        "line_range": "The range arguments are on line 1.",
        "bug_type": "Range starts one step too late.",
        "fix_hint": "Start the range at 0.",
        "accepted_answers": [
            """for number in range(0, 3):
    print(number)""",
            """for number in range(3):
    print(number)""",
        ],
        "explanation": (
            "range(start, stop) includes start but stops before stop. Starting at 1 skips 0, "
            "so range(1, 3) prints only 1 and 2."
        ),
    },
    {
        "id": "python-string-method-call",
        "language": "Python",
        "title": "The uncalled cleanup",
        "prompt": "Fix the string cleanup so the extra spaces are removed.",
        "bugged_code": """raw_name = "  Ada  "
clean_name = raw_name.strip

print(clean_name)""",
        "fixed_code": """raw_name = "  Ada  "
clean_name = raw_name.strip()

print(clean_name)""",
        "bug_line": 2,
        "line_range": "The issue is on line 2.",
        "bug_type": "Method referenced but not called.",
        "fix_hint": "Add parentheses after strip.",
        "accepted_answers": [
            """raw_name = "  Ada  "
clean_name = raw_name.strip()

print(clean_name)"""
        ],
        "explanation": (
            "raw_name.strip without parentheses is the method object itself. Adding () calls "
            "the method and returns the cleaned string."
        ),
    },
    {
        "id": "python-list-comprehension-order",
        "language": "Python",
        "title": "The scrambled comprehension",
        "prompt": "Fix the list comprehension so it squares each number.",
        "bugged_code": """numbers = [1, 2, 3]

squares = [for number in numbers: number * number]
print(squares)""",
        "fixed_code": """numbers = [1, 2, 3]

squares = [number * number for number in numbers]
print(squares)""",
        "bug_line": 3,
        "line_range": "The comprehension on line 3 is out of order.",
        "bug_type": "Invalid list comprehension syntax.",
        "fix_hint": "Put the expression first, then the for clause.",
        "accepted_answers": [
            """numbers = [1, 2, 3]

squares = [number * number for number in numbers]
print(squares)""",
            """numbers = [1, 2, 3]

squares = []
for number in numbers:
    squares.append(number * number)
print(squares)""",
        ],
        "explanation": (
            "A Python list comprehension starts with the value to put in the list, followed "
            "by the for clause. The colon form belongs to a normal for loop, not a comprehension."
        ),
    },
    {
        "id": "python-f-string-prefix",
        "language": "Python",
        "title": "The literal braces",
        "prompt": "Fix the greeting so it includes the value of name.",
        "bugged_code": """name = "Lin"

message = "Hello, {name}"
print(message)""",
        "fixed_code": """name = "Lin"

message = f"Hello, {name}"
print(message)""",
        "bug_line": 3,
        "line_range": "Look at the string on line 3.",
        "bug_type": "Missing f-string prefix.",
        "fix_hint": "Add f before the opening quote.",
        "accepted_answers": [
            """name = "Lin"

message = f"Hello, {name}"
print(message)""",
            """name = "Lin"

message = "Hello, " + name
print(message)""",
        ],
        "explanation": (
            "Braces only interpolate variables inside an f-string. Without the f prefix, "
            "Python treats {name} as ordinary text."
        ),
    },
    {
        "id": "python-class-self",
        "language": "Python",
        "title": "The missing self",
        "prompt": "Fix the method so calling it on an instance works.",
        "bugged_code": """class Badge:
    def label():
        return "Python Debugger"

badge = Badge()
print(badge.label())""",
        "fixed_code": """class Badge:
    def label(self):
        return "Python Debugger"

badge = Badge()
print(badge.label())""",
        "bug_line": 2,
        "line_range": "The method definition on line 2 is missing a parameter.",
        "bug_type": "Instance method missing self.",
        "fix_hint": "Add self as the first method parameter.",
        "accepted_answers": [
            """class Badge:
    def label(self):
        return "Python Debugger"

badge = Badge()
print(badge.label())"""
        ],
        "explanation": (
            "When an instance method is called, Python automatically passes the instance as "
            "the first argument. The method must accept that argument, conventionally named self."
        ),
    },
    {
        "id": "python-mutable-default",
        "language": "Python",
        "title": "The shared backpack",
        "prompt": "Fix the function so each call gets a fresh list.",
        "bugged_code": """def add_item(item, backpack=[]):
    backpack.append(item)
    return backpack

first = add_item("book")
second = add_item("pencil")
print(second)""",
        "fixed_code": """def add_item(item, backpack=None):
    if backpack is None:
        backpack = []
    backpack.append(item)
    return backpack

first = add_item("book")
second = add_item("pencil")
print(second)""",
        "bug_line": 1,
        "line_range": "The risky default value is on line 1.",
        "bug_type": "Mutable default argument.",
        "fix_hint": "Use None as the default and create a new list inside the function.",
        "accepted_answers": [
            """def add_item(item, backpack=None):
    if backpack is None:
        backpack = []
    backpack.append(item)
    return backpack

first = add_item("book")
second = add_item("pencil")
print(second)"""
        ],
        "explanation": (
            "Default argument values are created once when the function is defined. A list "
            "default is shared across calls, so later calls reuse items from earlier calls."
        ),
    },
    {
        "id": "python-file-context-variable",
        "language": "Python",
        "title": "The wrong file handle",
        "prompt": "Fix the variable name used to read the opened file.",
        "bugged_code": """with open("notes.txt") as file:
    contents = f.read()

print(contents)""",
        "fixed_code": """with open("notes.txt") as file:
    contents = file.read()

print(contents)""",
        "bug_line": 2,
        "line_range": "Look at line 2 inside the with block.",
        "bug_type": "Wrong variable name for the file object.",
        "fix_hint": "Use the name after as in the with statement.",
        "accepted_answers": [
            """with open("notes.txt") as file:
    contents = file.read()

print(contents)"""
        ],
        "explanation": (
            "The with statement stores the opened file object in the variable named after as. "
            "Here that variable is file, so f is undefined."
        ),
    },
    {
        "id": "python-operator-precedence",
        "language": "Python",
        "title": "The average trap",
        "prompt": "Fix the calculation so it averages the two scores.",
        "bugged_code": """score_one = 80
score_two = 100

average = score_one + score_two / 2
print(average)""",
        "fixed_code": """score_one = 80
score_two = 100

average = (score_one + score_two) / 2
print(average)""",
        "bug_line": 4,
        "line_range": "The math expression is on line 4.",
        "bug_type": "Operator precedence changes the calculation.",
        "fix_hint": "Use parentheses around the addition.",
        "accepted_answers": [
            """score_one = 80
score_two = 100

average = (score_one + score_two) / 2
print(average)"""
        ],
        "explanation": (
            "Division happens before addition, so score_two / 2 is calculated first. "
            "Parentheses make Python add the two scores before dividing by 2."
        ),
    },
    {
        "id": "python-and-or-condition",
        "language": "Python",
        "title": "The impossible password",
        "prompt": "Fix the condition so either valid password is accepted.",
        "bugged_code": """password = "open"

if password == "open" and password == "sesame":
    print("Access granted")""",
        "fixed_code": """password = "open"

if password == "open" or password == "sesame":
    print("Access granted")""",
        "bug_line": 3,
        "line_range": "The logic bug is in the condition on line 3.",
        "bug_type": "and used where or is needed.",
        "fix_hint": "Use or because one matching password is enough.",
        "accepted_answers": [
            """password = "open"

if password == "open" or password == "sesame":
    print("Access granted")""",
            """password = "open"

if password in ["open", "sesame"]:
    print("Access granted")""",
        ],
        "explanation": (
            "A single string cannot be both \"open\" and \"sesame\" at the same time. "
            "or makes the condition true when either allowed value matches."
        ),
    },
]

JAVASCRIPT_PROBLEMS = [
    {
        "id": "javascript-assignment-condition",
        "language": "JavaScript",
        "title": "The always-open gate",
        "prompt": "Fix the condition so the admin branch only runs for admins.",
        "bugged_code": """const role = "guest";

if (role = "admin") {
  console.log("Welcome, admin");
} else {
  console.log("Welcome, guest");
}""",
        "fixed_code": """const role = "guest";

if (role === "admin") {
  console.log("Welcome, admin");
} else {
  console.log("Welcome, guest");
}""",
        "bug_line": 3,
        "line_range": "The bug is in lines 1-3.",
        "bug_type": "Assignment used instead of comparison.",
        "fix_hint": "Use strict equality, ===, in the if condition.",
        "accepted_answers": [
            """const role = "guest";

if (role === "admin") {
  console.log("Welcome, admin");
} else {
  console.log("Welcome, guest");
}"""
        ],
        "explanation": (
            "A single equals sign assigns a new value. The assignment changes role to "
            "\"admin\" and evaluates to a truthy string, so the admin branch runs."
        ),
    },
    {
        "id": "javascript-missing-brace",
        "language": "JavaScript",
        "title": "The unfinished block",
        "prompt": "Fix the function so the code after it is no longer trapped inside.",
        "bugged_code": """function shout(message) {
  return message.toUpperCase();

console.log(shout("debug"));""",
        "fixed_code": """function shout(message) {
  return message.toUpperCase();
}

console.log(shout("debug"));""",
        "bug_line": 3,
        "line_range": "Inspect lines 1-4.",
        "bug_type": "Missing closing curly brace.",
        "fix_hint": "Close the function block before the console.log call.",
        "accepted_answers": [
            """function shout(message) {
  return message.toUpperCase();
}

console.log(shout("debug"));"""
        ],
        "explanation": (
            "Curly braces mark the function body. Without the closing brace, JavaScript "
            "keeps parsing as though the function has not ended."
        ),
    },
    {
        "id": "javascript-missing-parenthesis",
        "language": "JavaScript",
        "title": "The open call",
        "prompt": "Fix the console call so the message can print.",
        "bugged_code": """const topic = "arrays";

console.log("Practice " + topic;""",
        "fixed_code": """const topic = "arrays";

console.log("Practice " + topic);""",
        "bug_line": 3,
        "line_range": "The syntax problem is on line 3.",
        "bug_type": "Missing closing parenthesis.",
        "fix_hint": "Close console.log before the semicolon.",
        "accepted_answers": [
            """const topic = "arrays";

console.log("Practice " + topic);"""
        ],
        "explanation": (
            "Function calls need matching parentheses. The parser reaches the semicolon while "
            "still waiting for the console.log call to close."
        ),
    },
    {
        "id": "javascript-string-quote",
        "language": "JavaScript",
        "title": "The split string",
        "prompt": "Fix the string literal so the variable can be created.",
        "bugged_code": """const message = "Debugging builds focus;
console.log(message);""",
        "fixed_code": """const message = "Debugging builds focus";
console.log(message);""",
        "bug_line": 1,
        "line_range": "The issue is on line 1.",
        "bug_type": "Unterminated string literal.",
        "fix_hint": "Add the missing closing quote before the semicolon.",
        "accepted_answers": [
            """const message = "Debugging builds focus";
console.log(message);""",
            """const message = 'Debugging builds focus';
console.log(message);""",
        ],
        "explanation": (
            "A quoted string must close with the same kind of quote that opened it. Without "
            "the closing quote, JavaScript treats the rest of the line as part of the string."
        ),
    },
    {
        "id": "javascript-const-reassignment",
        "language": "JavaScript",
        "title": "The locked counter",
        "prompt": "Fix the variable declaration so the counter can change.",
        "bugged_code": """const count = 0;
count = count + 1;

console.log(count);""",
        "fixed_code": """let count = 0;
count = count + 1;

console.log(count);""",
        "bug_line": 1,
        "line_range": "The declaration on line 1 controls whether reassignment is allowed.",
        "bug_type": "Reassigning a const variable.",
        "fix_hint": "Use let for a variable that needs to be reassigned.",
        "accepted_answers": [
            """let count = 0;
count = count + 1;

console.log(count);""",
            """let count = 0;
count += 1;

console.log(count);""",
        ],
        "explanation": (
            "const prevents reassignment of the variable binding. Because count changes on "
            "the next line, it should be declared with let."
        ),
    },
    {
        "id": "javascript-array-index",
        "language": "JavaScript",
        "title": "The missing last item",
        "prompt": "Fix the index so the final language is printed.",
        "bugged_code": """const languages = ["Python", "JavaScript", "SQL"];

console.log(languages[3]);""",
        "fixed_code": """const languages = ["Python", "JavaScript", "SQL"];

console.log(languages[2]);""",
        "bug_line": 3,
        "line_range": "The index is on line 3.",
        "bug_type": "Array index is one too high.",
        "fix_hint": "Use index 2 for the third item.",
        "accepted_answers": [
            """const languages = ["Python", "JavaScript", "SQL"];

console.log(languages[2]);""",
            """const languages = ["Python", "JavaScript", "SQL"];

console.log(languages[languages.length - 1]);""",
        ],
        "explanation": (
            "JavaScript arrays are zero-indexed. A three-item array has indexes 0, 1, and 2, "
            "so index 3 returns undefined."
        ),
    },
    {
        "id": "javascript-length-case",
        "language": "JavaScript",
        "title": "The capital L",
        "prompt": "Fix the property name so the number of tasks is printed.",
        "bugged_code": """const tasks = ["read", "fix", "test"];

console.log(tasks.Length);""",
        "fixed_code": """const tasks = ["read", "fix", "test"];

console.log(tasks.length);""",
        "bug_line": 3,
        "line_range": "The property name on line 3 has the bug.",
        "bug_type": "Property name has the wrong capitalization.",
        "fix_hint": "Use lowercase length.",
        "accepted_answers": [
            """const tasks = ["read", "fix", "test"];

console.log(tasks.length);"""
        ],
        "explanation": (
            "JavaScript property names are case-sensitive. Length and length are different "
            "properties, and arrays expose length in lowercase."
        ),
    },
    {
        "id": "javascript-object-key",
        "language": "JavaScript",
        "title": "The missing quotes",
        "prompt": "Fix the object lookup so it reads the display name.",
        "bugged_code": """const user = { name: "Ari", level: 4 };

console.log(user[displayName]);""",
        "fixed_code": """const user = { name: "Ari", level: 4 };

console.log(user["name"]);""",
        "bug_line": 3,
        "line_range": "The lookup on line 3 is using the wrong key expression.",
        "bug_type": "Bracket lookup uses an undefined variable.",
        "fix_hint": "Use a string key, or use dot notation for the name property.",
        "accepted_answers": [
            """const user = { name: "Ari", level: 4 };

console.log(user["name"]);""",
            """const user = { name: "Ari", level: 4 };

console.log(user.name);""",
        ],
        "explanation": (
            "Bracket notation evaluates what is inside the brackets. displayName is treated "
            "as a variable, not a literal key, so it fails unless that variable exists."
        ),
    },
    {
        "id": "javascript-function-return",
        "language": "JavaScript",
        "title": "The quiet multiplier",
        "prompt": "Fix the function so doubled receives the calculated value.",
        "bugged_code": """function double(number) {
  number * 2;
}

const doubled = double(6);
console.log(doubled);""",
        "fixed_code": """function double(number) {
  return number * 2;
}

const doubled = double(6);
console.log(doubled);""",
        "bug_line": 2,
        "line_range": "Look inside the function on line 2.",
        "bug_type": "Missing return statement.",
        "fix_hint": "Return the expression from the function.",
        "accepted_answers": [
            """function double(number) {
  return number * 2;
}

const doubled = double(6);
console.log(doubled);"""
        ],
        "explanation": (
            "A function without return gives undefined to its caller. The multiplication runs, "
            "but its result is discarded unless it is returned."
        ),
    },
    {
        "id": "javascript-arrow-object-return",
        "language": "JavaScript",
        "title": "The invisible object",
        "prompt": "Fix the arrow function so it returns an object.",
        "bugged_code": """const makeUser = name => { name: name };

console.log(makeUser("Mina"));""",
        "fixed_code": """const makeUser = name => ({ name: name });

console.log(makeUser("Mina"));""",
        "bug_line": 1,
        "line_range": "The arrow function body is on line 1.",
        "bug_type": "Object literal parsed as a block body.",
        "fix_hint": "Wrap the object literal in parentheses.",
        "accepted_answers": [
            """const makeUser = name => ({ name: name });

console.log(makeUser("Mina"));""",
            """const makeUser = name => {
  return { name: name };
};

console.log(makeUser("Mina"));""",
        ],
        "explanation": (
            "After an arrow, braces are treated as a function block unless wrapped in "
            "parentheses. The object literal needs parentheses or an explicit return."
        ),
    },
    {
        "id": "javascript-template-literal",
        "language": "JavaScript",
        "title": "The literal placeholder",
        "prompt": "Fix the greeting so it includes the value of name.",
        "bugged_code": """const name = "Nia";
const greeting = "Hello, ${name}";

console.log(greeting);""",
        "fixed_code": """const name = "Nia";
const greeting = `Hello, ${name}`;

console.log(greeting);""",
        "bug_line": 2,
        "line_range": "The string on line 2 uses the wrong kind of quotes.",
        "bug_type": "Template placeholder inside a normal string.",
        "fix_hint": "Use backticks for a template literal.",
        "accepted_answers": [
            """const name = "Nia";
const greeting = `Hello, ${name}`;

console.log(greeting);""",
            """const name = "Nia";
const greeting = "Hello, " + name;

console.log(greeting);""",
        ],
        "explanation": (
            "${name} is only interpolated inside a template literal. In normal quotes, it is "
            "just text."
        ),
    },
    {
        "id": "javascript-map-return",
        "language": "JavaScript",
        "title": "The empty map",
        "prompt": "Fix the callback so map creates doubled numbers.",
        "bugged_code": """const numbers = [1, 2, 3];

const doubled = numbers.map(number => {
  number * 2;
});

console.log(doubled);""",
        "fixed_code": """const numbers = [1, 2, 3];

const doubled = numbers.map(number => {
  return number * 2;
});

console.log(doubled);""",
        "bug_line": 4,
        "line_range": "The callback body is lines 3-5.",
        "bug_type": "Missing return inside a block-bodied arrow function.",
        "fix_hint": "Return number * 2 from the map callback.",
        "accepted_answers": [
            """const numbers = [1, 2, 3];

const doubled = numbers.map(number => {
  return number * 2;
});

console.log(doubled);""",
            """const numbers = [1, 2, 3];

const doubled = numbers.map(number => number * 2);

console.log(doubled);""",
        ],
        "explanation": (
            "An arrow function with braces needs an explicit return. Without it, each callback "
            "returns undefined, so map builds an array of undefined values."
        ),
    },
    {
        "id": "javascript-for-loop-boundary",
        "language": "JavaScript",
        "title": "The extra iteration",
        "prompt": "Fix the loop so it prints only real scores.",
        "bugged_code": """const scores = [80, 91, 77];

for (let index = 0; index <= scores.length; index++) {
  console.log(scores[index]);
}""",
        "fixed_code": """const scores = [80, 91, 77];

for (let index = 0; index < scores.length; index++) {
  console.log(scores[index]);
}""",
        "bug_line": 3,
        "line_range": "The loop condition is on line 3.",
        "bug_type": "Off-by-one loop boundary.",
        "fix_hint": "Use < instead of <= when comparing with length.",
        "accepted_answers": [
            """const scores = [80, 91, 77];

for (let index = 0; index < scores.length; index++) {
  console.log(scores[index]);
}""",
            """const scores = [80, 91, 77];

for (const score of scores) {
  console.log(score);
}""",
        ],
        "explanation": (
            "The final valid index is length - 1. Using <= length runs one extra time and "
            "tries to read scores[length], which is undefined."
        ),
    },
    {
        "id": "javascript-parseint-string",
        "language": "JavaScript",
        "title": "The text total",
        "prompt": "Fix the addition so the two values are treated as numbers.",
        "bugged_code": """const first = "10";
const second = "5";

console.log(first + second);""",
        "fixed_code": """const first = "10";
const second = "5";

console.log(Number(first) + Number(second));""",
        "bug_line": 4,
        "line_range": "The addition happens on line 4.",
        "bug_type": "String concatenation instead of numeric addition.",
        "fix_hint": "Convert both strings to numbers before adding.",
        "accepted_answers": [
            """const first = "10";
const second = "5";

console.log(Number(first) + Number(second));""",
            """const first = "10";
const second = "5";

console.log(parseInt(first) + parseInt(second));""",
        ],
        "explanation": (
            "When + sees strings, it concatenates them. Converting the values first makes + "
            "perform numeric addition."
        ),
    },
    {
        "id": "javascript-scope-let",
        "language": "JavaScript",
        "title": "The hidden message",
        "prompt": "Fix the scope so the message can be printed after the if block.",
        "bugged_code": """if (true) {
  let message = "Ready";
}

console.log(message);""",
        "fixed_code": """let message;

if (true) {
  message = "Ready";
}

console.log(message);""",
        "bug_line": 2,
        "line_range": "The variable is declared inside lines 1-3.",
        "bug_type": "Block-scoped variable used outside its block.",
        "fix_hint": "Declare message before the block, then assign it inside.",
        "accepted_answers": [
            """let message;

if (true) {
  message = "Ready";
}

console.log(message);""",
            """let message = "Ready";

if (true) {
}

console.log(message);""",
        ],
        "explanation": (
            "let is block-scoped, so message only exists inside the curly braces where it was "
            "declared. Code after the block cannot read it."
        ),
    },
    {
        "id": "javascript-array-push-return",
        "language": "JavaScript",
        "title": "The number instead of a list",
        "prompt": "Fix the push usage so items remains an array.",
        "bugged_code": """let items = ["notebook", "pen"];
items = items.push("eraser");

console.log(items);""",
        "fixed_code": """let items = ["notebook", "pen"];
items.push("eraser");

console.log(items);""",
        "bug_line": 2,
        "line_range": "The mistake is on line 2.",
        "bug_type": "Assigning the return value of push.",
        "fix_hint": "Call push without assigning its result back to the array.",
        "accepted_answers": [
            """let items = ["notebook", "pen"];
items.push("eraser");

console.log(items);""",
            """let items = ["notebook", "pen"];
items = [...items, "eraser"];

console.log(items);""",
        ],
        "explanation": (
            "push mutates the array and returns the new length. Assigning that return value "
            "back to items replaces the array with a number."
        ),
    },
    {
        "id": "javascript-destructuring-name",
        "language": "JavaScript",
        "title": "The wrong property",
        "prompt": "Fix the destructuring so the city prints correctly.",
        "bugged_code": """const profile = { name: "Jules", city: "Boston" };
const { location } = profile;

console.log(location);""",
        "fixed_code": """const profile = { name: "Jules", city: "Boston" };
const { city } = profile;

console.log(city);""",
        "bug_line": 2,
        "line_range": "The destructuring pattern on line 2 asks for the wrong property.",
        "bug_type": "Destructuring a property that does not exist.",
        "fix_hint": "Destructure city, because that is the key in the object.",
        "accepted_answers": [
            """const profile = { name: "Jules", city: "Boston" };
const { city } = profile;

console.log(city);""",
            """const profile = { name: "Jules", city: "Boston" };
const location = profile.city;

console.log(location);""",
        ],
        "explanation": (
            "Destructuring uses property names. The object has city, not location, so location "
            "is assigned undefined."
        ),
    },
    {
        "id": "javascript-try-catch",
        "language": "JavaScript",
        "title": "The catch without braces",
        "prompt": "Fix the catch block syntax.",
        "bugged_code": """try {
  JSON.parse("{bad json}");
} catch (error)
  console.log("Could not parse JSON");
}""",
        "fixed_code": """try {
  JSON.parse("{bad json}");
} catch (error) {
  console.log("Could not parse JSON");
}""",
        "bug_line": 3,
        "line_range": "The catch header and body are lines 3-5.",
        "bug_type": "Missing opening curly brace for a catch block.",
        "fix_hint": "Add { after catch (error).",
        "accepted_answers": [
            """try {
  JSON.parse("{bad json}");
} catch (error) {
  console.log("Could not parse JSON");
}"""
        ],
        "explanation": (
            "catch uses a block body. The opening brace after catch (error) begins the handler, "
            "and the closing brace ends it."
        ),
    },
    {
        "id": "javascript-async-await",
        "language": "JavaScript",
        "title": "The early promise",
        "prompt": "Fix the async function so data holds the resolved value.",
        "bugged_code": """async function loadName() {
  return "Ada";
}

const data = loadName();
console.log(data);""",
        "fixed_code": """async function loadName() {
  return "Ada";
}

async function showName() {
  const data = await loadName();
  console.log(data);
}

showName();""",
        "bug_line": 5,
        "line_range": "The call on line 5 returns a Promise.",
        "bug_type": "Async function result used without await.",
        "fix_hint": "Await the async function call inside another async function.",
        "accepted_answers": [
            """async function loadName() {
  return "Ada";
}

async function showName() {
  const data = await loadName();
  console.log(data);
}

showName();""",
            """async function loadName() {
  return "Ada";
}

loadName().then(data => {
  console.log(data);
});"""
        ],
        "explanation": (
            "An async function always returns a Promise. await pauses until the Promise resolves "
            "and gives data the resolved value instead of the Promise object."
        ),
    },
    {
        "id": "javascript-not-operator",
        "language": "JavaScript",
        "title": "The flipped login",
        "prompt": "Fix the condition so the welcome message prints when the user is logged in.",
        "bugged_code": """const isLoggedIn = true;

if (!isLoggedIn) {
  console.log("Welcome back");
}""",
        "fixed_code": """const isLoggedIn = true;

if (isLoggedIn) {
  console.log("Welcome back");
}""",
        "bug_line": 3,
        "line_range": "The boolean check is on line 3.",
        "bug_type": "Unwanted logical NOT operator.",
        "fix_hint": "Remove ! so the condition checks for true.",
        "accepted_answers": [
            """const isLoggedIn = true;

if (isLoggedIn) {
  console.log("Welcome back");
}"""
        ],
        "explanation": (
            "! flips a boolean value. Since isLoggedIn is already true, !isLoggedIn becomes "
            "false and the welcome branch is skipped."
        ),
    },
    {
        "id": "javascript-object-missing-comma",
        "language": "JavaScript",
        "title": "The crowded object",
        "prompt": "Fix the object literal so both settings are valid.",
        "bugged_code": """const settings = {
  theme: "dark"
  fontSize: 16
};

console.log(settings);""",
        "fixed_code": """const settings = {
  theme: "dark",
  fontSize: 16
};

console.log(settings);""",
        "bug_line": 2,
        "line_range": "Inspect lines 2-3.",
        "bug_type": "Missing comma between object properties.",
        "fix_hint": "Add a comma after the theme property.",
        "accepted_answers": [
            """const settings = {
  theme: "dark",
  fontSize: 16
};

console.log(settings);"""
        ],
        "explanation": (
            "Object properties must be separated by commas. Without the comma, JavaScript "
            "cannot tell where one property ends and the next begins."
        ),
    },
    {
        "id": "javascript-array-missing-comma",
        "language": "JavaScript",
        "title": "The joined strings",
        "prompt": "Fix the array so it contains three separate labels.",
        "bugged_code": """const labels = ["bug", "hint" "fix"];

console.log(labels);""",
        "fixed_code": """const labels = ["bug", "hint", "fix"];

console.log(labels);""",
        "bug_line": 1,
        "line_range": "The array literal on line 1 is missing a separator.",
        "bug_type": "Missing comma between array items.",
        "fix_hint": "Add a comma between \"hint\" and \"fix\".",
        "accepted_answers": [
            """const labels = ["bug", "hint", "fix"];

console.log(labels);"""
        ],
        "explanation": (
            "Array items need commas between them. Two adjacent strings without a comma make "
            "the array syntax invalid."
        ),
    },
    {
        "id": "javascript-strict-equality",
        "language": "JavaScript",
        "title": "The loose match",
        "prompt": "Fix the comparison so the string value is not treated like a number.",
        "bugged_code": """const answer = "5";

if (answer == 5) {
  console.log("Correct");
}""",
        "fixed_code": """const answer = "5";

if (answer === 5) {
  console.log("Correct");
}""",
        "bug_line": 3,
        "line_range": "The comparison operator is on line 3.",
        "bug_type": "Loose equality allows type coercion.",
        "fix_hint": "Use === when the type should match too.",
        "accepted_answers": [
            """const answer = "5";

if (answer === 5) {
  console.log("Correct");
}"""
        ],
        "explanation": (
            "== can convert values before comparing them, so the string \"5\" can match the "
            "number 5. === compares both value and type."
        ),
    },
    {
        "id": "javascript-default-parameter",
        "language": "JavaScript",
        "title": "The missing greeting",
        "prompt": "Fix the function so calling it without a name still works.",
        "bugged_code": """function greet(name) {
  return "Hello, " + name.toUpperCase();
}

console.log(greet());""",
        "fixed_code": """function greet(name = "friend") {
  return "Hello, " + name.toUpperCase();
}

console.log(greet());""",
        "bug_line": 1,
        "line_range": "The function parameter is on line 1.",
        "bug_type": "Missing default value for an optional argument.",
        "fix_hint": "Give name a default string value.",
        "accepted_answers": [
            """function greet(name = "friend") {
  return "Hello, " + name.toUpperCase();
}

console.log(greet());""",
            """function greet(name) {
  name = name || "friend";
  return "Hello, " + name.toUpperCase();
}

console.log(greet());""",
        ],
        "explanation": (
            "When greet is called without an argument, name is undefined. Calling toUpperCase "
            "on undefined throws an error, so the function needs a fallback value."
        ),
    },
    {
        "id": "javascript-reduce-initial",
        "language": "JavaScript",
        "title": "The empty total",
        "prompt": "Fix the reduce call so it works even when the array is empty.",
        "bugged_code": """const points = [];

const total = points.reduce((sum, point) => sum + point);
console.log(total);""",
        "fixed_code": """const points = [];

const total = points.reduce((sum, point) => sum + point, 0);
console.log(total);""",
        "bug_line": 3,
        "line_range": "The reduce call is on line 3.",
        "bug_type": "Missing initial value for reduce.",
        "fix_hint": "Pass 0 as the second argument to reduce.",
        "accepted_answers": [
            """const points = [];

const total = points.reduce((sum, point) => sum + point, 0);
console.log(total);"""
        ],
        "explanation": (
            "reduce needs a starting accumulator when the array might be empty. Without an "
            "initial value, there is no first item to use as the starting sum."
        ),
    },
    {
        "id": "javascript-includes-case",
        "language": "JavaScript",
        "title": "The capital method",
        "prompt": "Fix the method call so the role check works.",
        "bugged_code": """const roles = ["editor", "admin"];

if (roles.Contains("admin")) {
  console.log("Allowed");
}""",
        "fixed_code": """const roles = ["editor", "admin"];

if (roles.includes("admin")) {
  console.log("Allowed");
}""",
        "bug_line": 3,
        "line_range": "The array method on line 3 is wrong.",
        "bug_type": "Incorrect array method name and capitalization.",
        "fix_hint": "Use includes with a lowercase i.",
        "accepted_answers": [
            """const roles = ["editor", "admin"];

if (roles.includes("admin")) {
  console.log("Allowed");
}"""
        ],
        "explanation": (
            "JavaScript arrays use includes to test for an item. Method names are case-sensitive, "
            "so Contains is not the same as includes."
        ),
    },
    {
        "id": "javascript-class-constructor",
        "language": "JavaScript",
        "title": "The nameless badge",
        "prompt": "Fix the class so the constructor stores the badge title.",
        "bugged_code": """class Badge {
  constructor(title) {
    title = title;
  }
}

const badge = new Badge("Debugging");
console.log(badge.title);""",
        "fixed_code": """class Badge {
  constructor(title) {
    this.title = title;
  }
}

const badge = new Badge("Debugging");
console.log(badge.title);""",
        "bug_line": 3,
        "line_range": "The constructor assignment is on line 3.",
        "bug_type": "Constructor parameter not assigned to the instance.",
        "fix_hint": "Assign the value to this.title.",
        "accepted_answers": [
            """class Badge {
  constructor(title) {
    this.title = title;
  }
}

const badge = new Badge("Debugging");
console.log(badge.title);"""
        ],
        "explanation": (
            "title = title only assigns the parameter to itself. this.title creates an instance "
            "property that can be read later from badge.title."
        ),
    },
    {
        "id": "javascript-this-callback",
        "language": "JavaScript",
        "title": "The lost object context",
        "prompt": "Fix the callback so it can read this.name.",
        "bugged_code": """const user = {
  name: "Sam",
  sayLater: function () {
    setTimeout(function () {
      console.log(this.name);
    }, 100);
  }
};

user.sayLater();""",
        "fixed_code": """const user = {
  name: "Sam",
  sayLater: function () {
    setTimeout(() => {
      console.log(this.name);
    }, 100);
  }
};

user.sayLater();""",
        "bug_line": 4,
        "line_range": "The callback starts on line 4.",
        "bug_type": "this changes inside a regular callback function.",
        "fix_hint": "Use an arrow function for the setTimeout callback.",
        "accepted_answers": [
            """const user = {
  name: "Sam",
  sayLater: function () {
    setTimeout(() => {
      console.log(this.name);
    }, 100);
  }
};

user.sayLater();"""
        ],
        "explanation": (
            "A regular function gets its own this value when it is called. An arrow function "
            "keeps the this value from sayLater, so this.name still refers to the user."
        ),
    },
    {
        "id": "javascript-null-property",
        "language": "JavaScript",
        "title": "The missing profile",
        "prompt": "Fix the code so it safely reads a missing profile.",
        "bugged_code": """const user = null;

console.log(user.name);""",
        "fixed_code": """const user = null;

console.log(user?.name);""",
        "bug_line": 3,
        "line_range": "The property access is on line 3.",
        "bug_type": "Reading a property from null.",
        "fix_hint": "Use optional chaining before .name.",
        "accepted_answers": [
            """const user = null;

console.log(user?.name);""",
            """const user = null;

if (user) {
  console.log(user.name);
}"""
        ],
        "explanation": (
            "null has no properties, so user.name throws a TypeError. Optional chaining stops "
            "the lookup and returns undefined when user is null or undefined."
        ),
    },
    {
        "id": "javascript-spread-array",
        "language": "JavaScript",
        "title": "The nested list",
        "prompt": "Fix the combined array so the new items are not nested.",
        "bugged_code": """const current = ["debug"];
const next = ["test", "ship"];

const all = [current, ...next];
console.log(all);""",
        "fixed_code": """const current = ["debug"];
const next = ["test", "ship"];

const all = [...current, ...next];
console.log(all);""",
        "bug_line": 4,
        "line_range": "The array merge happens on line 4.",
        "bug_type": "Array inserted instead of spread.",
        "fix_hint": "Spread current the same way next is spread.",
        "accepted_answers": [
            """const current = ["debug"];
const next = ["test", "ship"];

const all = [...current, ...next];
console.log(all);""",
            """const current = ["debug"];
const next = ["test", "ship"];

const all = current.concat(next);
console.log(all);""",
        ],
        "explanation": (
            "Putting current directly inside the new array makes it one nested element. "
            "...current expands its items into the surrounding array."
        ),
    },
]


HTML_PROBLEMS = [
    {
        "id": "html-missing-doctype",
        "language": "HTML",
        "title": "The missing document mode",
        "prompt": "Fix the document so browsers use standards mode.",
        "bugged_code": """<html>
  <head>
    <title>Debug Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
  </body>
</html>""",
        "fixed_code": """<!doctype html>
<html>
  <head>
    <title>Debug Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
  </body>
</html>""",
        "bug_line": 1,
        "line_range": "Look before line 1.",
        "bug_type": "Missing HTML doctype.",
        "fix_hint": "Add <!doctype html> at the top of the file.",
        "accepted_answers": [
            """<!doctype html>
<html>
  <head>
    <title>Debug Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
  </body>
</html>"""
        ],
        "explanation": "The doctype tells browsers to render the page in modern standards mode instead of older compatibility behavior.",
    },
    {
        "id": "html-missing-head-close",
        "language": "HTML",
        "title": "The swallowed body",
        "prompt": "Fix the structure so the body is not inside the head.",
        "bugged_code": """<!doctype html>
<html>
  <head>
    <title>Practice</title>
  <body>
    <p>Hello</p>
  </body>
</html>""",
        "fixed_code": """<!doctype html>
<html>
  <head>
    <title>Practice</title>
  </head>
  <body>
    <p>Hello</p>
  </body>
</html>""",
        "bug_line": 5,
        "line_range": "Inspect lines 3-5.",
        "bug_type": "Missing closing head tag.",
        "fix_hint": "Close </head> before opening <body>.",
        "accepted_answers": [
            """<!doctype html>
<html>
  <head>
    <title>Practice</title>
  </head>
  <body>
    <p>Hello</p>
  </body>
</html>"""
        ],
        "explanation": "The head contains metadata, not page content. Closing it before body keeps the document tree valid and predictable.",
    },
    {
        "id": "html-unclosed-list-item",
        "language": "HTML",
        "title": "The runaway list",
        "prompt": "Fix the list markup so each task is its own item.",
        "bugged_code": """<ul>
  <li>Read docs
  <li>Fix bug
  <li>Run tests
</ul>""",
        "fixed_code": """<ul>
  <li>Read docs</li>
  <li>Fix bug</li>
  <li>Run tests</li>
</ul>""",
        "bug_line": 2,
        "line_range": "The list items are on lines 2-4.",
        "bug_type": "List items are not explicitly closed.",
        "fix_hint": "Add a matching </li> for each list item.",
        "accepted_answers": [
            """<ul>
  <li>Read docs</li>
  <li>Fix bug</li>
  <li>Run tests</li>
</ul>"""
        ],
        "explanation": "Browsers often infer closing list tags, but explicit closing tags make nesting clearer and prevent accidental structure bugs.",
    },
    {
        "id": "html-link-href",
        "language": "HTML",
        "title": "The link without a destination",
        "prompt": "Fix the anchor so it actually links to the docs page.",
        "bugged_code": """<a src="/docs">Read the docs</a>""",
        "fixed_code": """<a href="/docs">Read the docs</a>""",
        "bug_line": 1,
        "line_range": "The wrong attribute is on line 1.",
        "bug_type": "Anchor uses src instead of href.",
        "fix_hint": "Use href for links.",
        "accepted_answers": ["""<a href="/docs">Read the docs</a>"""],
        "explanation": "Anchor elements navigate with href. src is for embedded resources such as images and scripts.",
    },
    {
        "id": "html-image-alt",
        "language": "HTML",
        "title": "The silent image",
        "prompt": "Fix the image so it has useful alternative text.",
        "bugged_code": """<img src="diagram.png">""",
        "fixed_code": """<img src="diagram.png" alt="Debugging workflow diagram">""",
        "bug_line": 1,
        "line_range": "The image tag is on line 1.",
        "bug_type": "Image missing alt text.",
        "fix_hint": "Add an alt attribute that describes the image.",
        "accepted_answers": ["""<img src="diagram.png" alt="Debugging workflow diagram">"""],
        "explanation": "Alt text gives screen readers and failed image loads meaningful information about the image content.",
    },
    {
        "id": "html-label-for",
        "language": "HTML",
        "title": "The disconnected label",
        "prompt": "Fix the form label so it is connected to the input.",
        "bugged_code": """<label for="email">Email</label>
<input id="user-email" type="email">""",
        "fixed_code": """<label for="user-email">Email</label>
<input id="user-email" type="email">""",
        "bug_line": 1,
        "line_range": "Compare the attributes on lines 1-2.",
        "bug_type": "Label for value does not match input id.",
        "fix_hint": "Make the label's for attribute match the input id.",
        "accepted_answers": [
            """<label for="user-email">Email</label>
<input id="user-email" type="email">"""
        ],
        "explanation": "A label connects to an input when for and id match exactly. That improves accessibility and click behavior.",
    },
    {
        "id": "html-button-type",
        "language": "HTML",
        "title": "The accidental submit",
        "prompt": "Fix the button so it does not submit the form.",
        "bugged_code": """<form>
  <button>Show hint</button>
</form>""",
        "fixed_code": """<form>
  <button type="button">Show hint</button>
</form>""",
        "bug_line": 2,
        "line_range": "The button is on line 2.",
        "bug_type": "Button defaults to submit inside a form.",
        "fix_hint": "Add type=\"button\".",
        "accepted_answers": [
            """<form>
  <button type="button">Show hint</button>
</form>"""
        ],
        "explanation": "Inside a form, a button without a type submits by default. type=\"button\" makes it a plain interactive button.",
    },
    {
        "id": "html-input-required",
        "language": "HTML",
        "title": "The optional required field",
        "prompt": "Fix the input so the browser requires a value.",
        "bugged_code": """<input type="text" required="false">""",
        "fixed_code": """<input type="text" required>""",
        "bug_line": 1,
        "line_range": "The boolean attribute is on line 1.",
        "bug_type": "Boolean attribute used with a false string.",
        "fix_hint": "Use required only when the field should be required.",
        "accepted_answers": ["""<input type="text" required>"""],
        "explanation": "HTML boolean attributes are true when present. required=\"false\" still makes the field required because the attribute exists.",
    },
    {
        "id": "html-table-section",
        "language": "HTML",
        "title": "The header in the body",
        "prompt": "Fix the table so header cells are in a table head.",
        "bugged_code": """<table>
  <tbody>
    <tr><th>Name</th><th>Score</th></tr>
    <tr><td>Ada</td><td>98</td></tr>
  </tbody>
</table>""",
        "fixed_code": """<table>
  <thead>
    <tr><th>Name</th><th>Score</th></tr>
  </thead>
  <tbody>
    <tr><td>Ada</td><td>98</td></tr>
  </tbody>
</table>""",
        "bug_line": 2,
        "line_range": "The table sections are lines 2-4.",
        "bug_type": "Header row placed in tbody instead of thead.",
        "fix_hint": "Move the header row into a <thead> section.",
        "accepted_answers": [
            """<table>
  <thead>
    <tr><th>Name</th><th>Score</th></tr>
  </thead>
  <tbody>
    <tr><td>Ada</td><td>98</td></tr>
  </tbody>
</table>"""
        ],
        "explanation": "thead and tbody communicate table structure to browsers and assistive technology, especially for data tables.",
    },
    {
        "id": "html-semantic-main",
        "language": "HTML",
        "title": "The generic main content",
        "prompt": "Fix the markup so the primary content uses a semantic landmark.",
        "bugged_code": """<div id="main">
  <h1>Dashboard</h1>
</div>""",
        "fixed_code": """<main>
  <h1>Dashboard</h1>
</main>""",
        "bug_line": 1,
        "line_range": "The wrapper on line 1 is too generic.",
        "bug_type": "Using a div where a main landmark fits.",
        "fix_hint": "Use <main> for the page's primary content.",
        "accepted_answers": [
            """<main>
  <h1>Dashboard</h1>
</main>"""
        ],
        "explanation": "Semantic landmarks such as main help browsers and assistive technologies understand page regions.",
    },
    {
        "id": "html-heading-order",
        "language": "HTML",
        "title": "The skipped heading",
        "prompt": "Fix the heading level so the section follows the page title.",
        "bugged_code": """<h1>Lessons</h1>
<h4>Syntax bugs</h4>""",
        "fixed_code": """<h1>Lessons</h1>
<h2>Syntax bugs</h2>""",
        "bug_line": 2,
        "line_range": "The heading level on line 2 is too deep.",
        "bug_type": "Skipped heading level.",
        "fix_hint": "Use h2 for a section directly under h1.",
        "accepted_answers": [
            """<h1>Lessons</h1>
<h2>Syntax bugs</h2>"""
        ],
        "explanation": "Headings create an outline. Skipping levels can make the page structure harder to understand.",
    },
    {
        "id": "html-nested-interactive",
        "language": "HTML",
        "title": "The button inside a link",
        "prompt": "Fix the interactive markup so controls are not nested.",
        "bugged_code": """<a href="/practice">
  <button>Start</button>
</a>""",
        "fixed_code": """<a href="/practice">Start</a>""",
        "bug_line": 1,
        "line_range": "The nesting spans lines 1-3.",
        "bug_type": "Nested interactive elements.",
        "fix_hint": "Use either a link or a button, not both nested together.",
        "accepted_answers": ["""<a href="/practice">Start</a>"""],
        "explanation": "Interactive elements should not be nested because click, keyboard, and accessibility behavior becomes ambiguous.",
    },
    {
        "id": "html-script-defer",
        "language": "HTML",
        "title": "The early script",
        "prompt": "Fix the script tag so it waits for the HTML to be parsed.",
        "bugged_code": """<head>
  <script src="app.js"></script>
</head>""",
        "fixed_code": """<head>
  <script src="app.js" defer></script>
</head>""",
        "bug_line": 2,
        "line_range": "The script tag is on line 2.",
        "bug_type": "Script loads before the document is parsed.",
        "fix_hint": "Add the defer attribute.",
        "accepted_answers": [
            """<head>
  <script src="app.js" defer></script>
</head>"""
        ],
        "explanation": "defer downloads the script without blocking parsing and runs it after the document is ready.",
    },
    {
        "id": "html-lang-attribute",
        "language": "HTML",
        "title": "The language-less page",
        "prompt": "Fix the root element so the document language is declared.",
        "bugged_code": """<html>
  <body>
    <p>Hello</p>
  </body>
</html>""",
        "fixed_code": """<html lang="en">
  <body>
    <p>Hello</p>
  </body>
</html>""",
        "bug_line": 1,
        "line_range": "The root html tag is on line 1.",
        "bug_type": "Missing lang attribute.",
        "fix_hint": "Add lang=\"en\" to the html element.",
        "accepted_answers": [
            """<html lang="en">
  <body>
    <p>Hello</p>
  </body>
</html>"""
        ],
        "explanation": "The lang attribute helps screen readers, search engines, and translation tools understand the document language.",
    },
    {
        "id": "html-meta-viewport",
        "language": "HTML",
        "title": "The desktop-sized mobile page",
        "prompt": "Fix the head so the layout can scale on mobile devices.",
        "bugged_code": """<head>
  <title>Practice</title>
</head>""",
        "fixed_code": """<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Practice</title>
</head>""",
        "bug_line": 2,
        "line_range": "The missing metadata belongs inside the head.",
        "bug_type": "Missing viewport meta tag.",
        "fix_hint": "Add a viewport meta tag before the title.",
        "accepted_answers": [
            """<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Practice</title>
</head>"""
        ],
        "explanation": "The viewport meta tag tells mobile browsers to match the layout viewport to the device width.",
    },
]


CSS_PROBLEMS = [
    {
        "id": "css-missing-semicolon",
        "language": "CSS",
        "title": "The blended declarations",
        "prompt": "Fix the rule so both color and background apply.",
        "bugged_code": """.alert {
  color: white
  background: crimson;
}""",
        "fixed_code": """.alert {
  color: white;
  background: crimson;
}""",
        "bug_line": 2,
        "line_range": "The missing punctuation is on line 2.",
        "bug_type": "Missing semicolon between declarations.",
        "fix_hint": "Add a semicolon after white.",
        "accepted_answers": [
            """.alert {
  color: white;
  background: crimson;
}"""
        ],
        "explanation": "Semicolons separate CSS declarations. Without one, the next property can be parsed incorrectly or ignored.",
    },
    {
        "id": "css-class-selector",
        "language": "CSS",
        "title": "The unselected card",
        "prompt": "Fix the selector so it targets elements with class=\"card\".",
        "bugged_code": """card {
  padding: 16px;
}""",
        "fixed_code": """.card {
  padding: 16px;
}""",
        "bug_line": 1,
        "line_range": "The selector is on line 1.",
        "bug_type": "Class selector missing dot.",
        "fix_hint": "Prefix the class name with .",
        "accepted_answers": [
            """.card {
  padding: 16px;
}"""
        ],
        "explanation": "A bare selector targets an element name. A class selector needs a dot before the class name.",
    },
    {
        "id": "css-id-selector",
        "language": "CSS",
        "title": "The wrong profile target",
        "prompt": "Fix the selector so it targets id=\"profile\".",
        "bugged_code": """.profile {
  max-width: 640px;
}""",
        "fixed_code": """#profile {
  max-width: 640px;
}""",
        "bug_line": 1,
        "line_range": "The selector is on line 1.",
        "bug_type": "ID selector written as a class selector.",
        "fix_hint": "Use # for an id selector.",
        "accepted_answers": [
            """#profile {
  max-width: 640px;
}"""
        ],
        "explanation": "Class selectors use ., while id selectors use #. The selector must match the HTML attribute type.",
    },
    {
        "id": "css-missing-unit",
        "language": "CSS",
        "title": "The unitless gap",
        "prompt": "Fix the margin so the browser knows its size.",
        "bugged_code": """.panel {
  margin-top: 24;
}""",
        "fixed_code": """.panel {
  margin-top: 24px;
}""",
        "bug_line": 2,
        "line_range": "The value on line 2 is incomplete.",
        "bug_type": "Length value missing a unit.",
        "fix_hint": "Add px to the margin value.",
        "accepted_answers": [
            """.panel {
  margin-top: 24px;
}"""
        ],
        "explanation": "Most CSS length values need units such as px, rem, or %. A plain number is invalid for margin-top unless the value is 0.",
    },
    {
        "id": "css-box-sizing",
        "language": "CSS",
        "title": "The oversized box",
        "prompt": "Fix the sizing model so padding stays inside the declared width.",
        "bugged_code": """.box {
  width: 200px;
  padding: 24px;
}""",
        "fixed_code": """.box {
  box-sizing: border-box;
  width: 200px;
  padding: 24px;
}""",
        "bug_line": 2,
        "line_range": "The missing sizing rule belongs before line 2.",
        "bug_type": "Content-box sizing makes padding add to width.",
        "fix_hint": "Add box-sizing: border-box.",
        "accepted_answers": [
            """.box {
  box-sizing: border-box;
  width: 200px;
  padding: 24px;
}"""
        ],
        "explanation": "With border-box, width includes content, padding, and border, which makes layout sizing easier to predict.",
    },
    {
        "id": "css-flex-direction",
        "language": "CSS",
        "title": "The vertical toolbar",
        "prompt": "Fix the flex rule so toolbar items sit in a row.",
        "bugged_code": """.toolbar {
  display: flex;
  flex-direction: column;
}""",
        "fixed_code": """.toolbar {
  display: flex;
  flex-direction: row;
}""",
        "bug_line": 3,
        "line_range": "The direction is on line 3.",
        "bug_type": "Wrong flex direction.",
        "fix_hint": "Use row for horizontal layout.",
        "accepted_answers": [
            """.toolbar {
  display: flex;
  flex-direction: row;
}""",
            """.toolbar {
  display: flex;
}""",
        ],
        "explanation": "The default flex direction is row. column stacks items vertically, which is wrong for a horizontal toolbar.",
    },
    {
        "id": "css-align-items",
        "language": "CSS",
        "title": "The off-center row",
        "prompt": "Fix the flex alignment so items are vertically centered.",
        "bugged_code": """.row {
  display: flex;
  justify-content: center;
}""",
        "fixed_code": """.row {
  display: flex;
  align-items: center;
  justify-content: center;
}""",
        "bug_line": 3,
        "line_range": "The rule centers on only one axis.",
        "bug_type": "Missing cross-axis flex alignment.",
        "fix_hint": "Add align-items: center.",
        "accepted_answers": [
            """.row {
  display: flex;
  align-items: center;
  justify-content: center;
}"""
        ],
        "explanation": "justify-content centers along the main axis. align-items centers along the cross axis.",
    },
    {
        "id": "css-grid-template",
        "language": "CSS",
        "title": "The invalid grid columns",
        "prompt": "Fix the grid syntax so it creates three equal columns.",
        "bugged_code": """.gallery {
  display: grid;
  grid-template-columns: repeat(3 1fr);
}""",
        "fixed_code": """.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}""",
        "bug_line": 3,
        "line_range": "The repeat syntax is on line 3.",
        "bug_type": "Missing comma in repeat function.",
        "fix_hint": "Separate the repeat count and track size with a comma.",
        "accepted_answers": [
            """.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}"""
        ],
        "explanation": "repeat() takes two arguments: how many tracks and the track size. CSS functions separate arguments with commas when required.",
    },
    {
        "id": "css-media-query",
        "language": "CSS",
        "title": "The backwards breakpoint",
        "prompt": "Fix the media query so the layout changes on small screens.",
        "bugged_code": """@media (min-width: 600px) {
  .layout {
    grid-template-columns: 1fr;
  }
}""",
        "fixed_code": """@media (max-width: 600px) {
  .layout {
    grid-template-columns: 1fr;
  }
}""",
        "bug_line": 1,
        "line_range": "The breakpoint condition is on line 1.",
        "bug_type": "Using min-width where max-width is intended.",
        "fix_hint": "Use max-width for styles that apply below 600px.",
        "accepted_answers": [
            """@media (max-width: 600px) {
  .layout {
    grid-template-columns: 1fr;
  }
}"""
        ],
        "explanation": "max-width applies up to the breakpoint. min-width applies from the breakpoint upward.",
    },
    {
        "id": "css-position-absolute",
        "language": "CSS",
        "title": "The wandering badge",
        "prompt": "Fix the card so the absolute badge is positioned relative to it.",
        "bugged_code": """.card {
  padding: 16px;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}""",
        "fixed_code": """.card {
  position: relative;
  padding: 16px;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}""",
        "bug_line": 1,
        "line_range": "The missing positioning context belongs in lines 1-3.",
        "bug_type": "Absolute child has no positioned parent.",
        "fix_hint": "Add position: relative to .card.",
        "accepted_answers": [
            """.card {
  position: relative;
  padding: 16px;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}"""
        ],
        "explanation": "An absolutely positioned element is placed relative to the nearest positioned ancestor. position: relative creates that anchor.",
    },
    {
        "id": "css-specificity-order",
        "language": "CSS",
        "title": "The overridden button",
        "prompt": "Fix the order so the primary button stays teal.",
        "bugged_code": """.button.primary {
  background: teal;
}

.button {
  background: gray;
}""",
        "fixed_code": """.button {
  background: gray;
}

.button.primary {
  background: teal;
}""",
        "bug_line": 1,
        "line_range": "Compare the order of the two rules.",
        "bug_type": "Cascade order makes the general rule win in this exercise.",
        "fix_hint": "Place the primary rule after the base button rule.",
        "accepted_answers": [
            """.button {
  background: gray;
}

.button.primary {
  background: teal;
}"""
        ],
        "explanation": "When rules compete, the cascade considers specificity and order. Keeping variants after base styles makes overrides easier to reason about.",
    },
    {
        "id": "css-custom-property",
        "language": "CSS",
        "title": "The unused color token",
        "prompt": "Fix the custom property usage so the heading uses the brand color.",
        "bugged_code": """:root {
  --brand: #0d766e;
}

h1 {
  color: --brand;
}""",
        "fixed_code": """:root {
  --brand: #0d766e;
}

h1 {
  color: var(--brand);
}""",
        "bug_line": 6,
        "line_range": "The custom property is used on line 6.",
        "bug_type": "Custom property used without var().",
        "fix_hint": "Wrap the custom property in var().",
        "accepted_answers": [
            """:root {
  --brand: #0d766e;
}

h1 {
  color: var(--brand);
}"""
        ],
        "explanation": "Custom properties are referenced with var(--name). Writing --brand directly is not a valid color value.",
    },
    {
        "id": "css-pseudo-class",
        "language": "CSS",
        "title": "The hover class",
        "prompt": "Fix the selector so the style applies when the link is hovered.",
        "bugged_code": """.link.hover {
  text-decoration: underline;
}""",
        "fixed_code": """.link:hover {
  text-decoration: underline;
}""",
        "bug_line": 1,
        "line_range": "The selector is on line 1.",
        "bug_type": "Pseudo-class written as a class selector.",
        "fix_hint": "Use :hover instead of .hover.",
        "accepted_answers": [
            """.link:hover {
  text-decoration: underline;
}"""
        ],
        "explanation": ":hover is a pseudo-class for pointer hover state. .hover only matches an element with class=\"hover\".",
    },
    {
        "id": "css-z-index-position",
        "language": "CSS",
        "title": "The ignored layer",
        "prompt": "Fix the modal so z-index can affect its stacking.",
        "bugged_code": """.modal {
  z-index: 10;
}""",
        "fixed_code": """.modal {
  position: fixed;
  z-index: 10;
}""",
        "bug_line": 2,
        "line_range": "The missing related property belongs in the .modal rule.",
        "bug_type": "z-index used without positioning.",
        "fix_hint": "Give the modal a positioned layout, such as position: fixed.",
        "accepted_answers": [
            """.modal {
  position: fixed;
  z-index: 10;
}""",
            """.modal {
  position: absolute;
  z-index: 10;
}"""
        ],
        "explanation": "z-index participates in stacking for positioned elements and some layout contexts. Positioning the modal makes the layer explicit.",
    },
    {
        "id": "css-transition-property",
        "language": "CSS",
        "title": "The instant fade",
        "prompt": "Fix the transition so opacity animates smoothly.",
        "bugged_code": """.tooltip {
  opacity: 0;
  transition: color 200ms ease;
}

.tooltip.visible {
  opacity: 1;
}""",
        "fixed_code": """.tooltip {
  opacity: 0;
  transition: opacity 200ms ease;
}

.tooltip.visible {
  opacity: 1;
}""",
        "bug_line": 3,
        "line_range": "The transition property is on line 3.",
        "bug_type": "Transition targets the wrong property.",
        "fix_hint": "Transition opacity, because opacity is what changes.",
        "accepted_answers": [
            """.tooltip {
  opacity: 0;
  transition: opacity 200ms ease;
}

.tooltip.visible {
  opacity: 1;
}"""
        ],
        "explanation": "A transition only animates the properties it targets. Since opacity changes, opacity must be in the transition.",
    },
]


JAVA_PROBLEMS = [
    {
        "id": "java-missing-semicolon",
        "language": "Java",
        "title": "The unfinished statement",
        "prompt": "Fix the statement so the program compiles.",
        "bugged_code": """public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Java")
    }
}""",
        "fixed_code": """public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}""",
        "bug_line": 3,
        "line_range": "Look at line 3.",
        "bug_type": "Missing semicolon.",
        "fix_hint": "Add a semicolon after the println call.",
        "accepted_answers": ["""public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}"""],
        "explanation": "Java statements usually end with semicolons. Without one, the compiler cannot tell where the statement ends.",
    },
    {
        "id": "java-class-name-case",
        "language": "Java",
        "title": "The lowercase string",
        "prompt": "Fix the type name so the message variable compiles.",
        "bugged_code": """public class Main {
    public static void main(String[] args) {
        string message = "Debugging";
        System.out.println(message);
    }
}""",
        "fixed_code": """public class Main {
    public static void main(String[] args) {
        String message = "Debugging";
        System.out.println(message);
    }
}""",
        "bug_line": 3,
        "line_range": "The bad type name is on line 3.",
        "bug_type": "Java type name has the wrong capitalization.",
        "fix_hint": "Use String with a capital S.",
        "accepted_answers": ["""public class Main {
    public static void main(String[] args) {
        String message = "Debugging";
        System.out.println(message);
    }
}"""],
        "explanation": "Java is case-sensitive. String is a class in the standard library, while string is not a known type.",
    },
    {
        "id": "java-main-signature",
        "language": "Java",
        "title": "The hidden entry point",
        "prompt": "Fix the main method signature so Java can start the program.",
        "bugged_code": """public class Main {
    public static void main(String args) {
        System.out.println("Run");
    }
}""",
        "fixed_code": """public class Main {
    public static void main(String[] args) {
        System.out.println("Run");
    }
}""",
        "bug_line": 2,
        "line_range": "The entry point is on line 2.",
        "bug_type": "main method parameter should be a String array.",
        "fix_hint": "Change String args to String[] args.",
        "accepted_answers": ["""public class Main {
    public static void main(String[] args) {
        System.out.println("Run");
    }
}"""],
        "explanation": "The JVM looks for public static void main(String[] args). A different parameter type is not the standard entry point.",
    },
    {
        "id": "java-single-equals-if",
        "language": "Java",
        "title": "The assigned score",
        "prompt": "Fix the condition so it compares score to 100.",
        "bugged_code": """int score = 100;

if (score = 100) {
    System.out.println("Perfect");
}""",
        "fixed_code": """int score = 100;

if (score == 100) {
    System.out.println("Perfect");
}""",
        "bug_line": 3,
        "line_range": "The condition is on line 3.",
        "bug_type": "Assignment used instead of comparison.",
        "fix_hint": "Use == for numeric equality.",
        "accepted_answers": ["""int score = 100;

if (score == 100) {
    System.out.println("Perfect");
}"""],
        "explanation": "= assigns a value. == compares primitive values and produces the boolean required by if.",
    },
    {
        "id": "java-string-equals",
        "language": "Java",
        "title": "The identity check",
        "prompt": "Fix the string comparison so it checks the text value.",
        "bugged_code": """String role = "admin";

if (role == "admin") {
    System.out.println("Allowed");
}""",
        "fixed_code": """String role = "admin";

if (role.equals("admin")) {
    System.out.println("Allowed");
}""",
        "bug_line": 3,
        "line_range": "The string comparison is on line 3.",
        "bug_type": "Strings compared with == instead of equals.",
        "fix_hint": "Use role.equals(\"admin\").",
        "accepted_answers": ["""String role = "admin";

if (role.equals("admin")) {
    System.out.println("Allowed");
}""", """String role = "admin";

if ("admin".equals(role)) {
    System.out.println("Allowed");
}"""],
        "explanation": "== compares object references. equals compares the characters inside the String.",
    },
    {
        "id": "java-array-index",
        "language": "Java",
        "title": "The fourth score",
        "prompt": "Fix the index so the last score prints.",
        "bugged_code": """int[] scores = {72, 86, 91};

System.out.println(scores[3]);""",
        "fixed_code": """int[] scores = {72, 86, 91};

System.out.println(scores[2]);""",
        "bug_line": 3,
        "line_range": "The index is on line 3.",
        "bug_type": "Array index is out of bounds.",
        "fix_hint": "Use index 2 for the third item.",
        "accepted_answers": ["""int[] scores = {72, 86, 91};

System.out.println(scores[2]);""", """int[] scores = {72, 86, 91};

System.out.println(scores[scores.length - 1]);"""],
        "explanation": "Java arrays are zero-indexed. A three-item array has indexes 0, 1, and 2.",
    },
    {
        "id": "java-length-property",
        "language": "Java",
        "title": "The called array length",
        "prompt": "Fix the array length access.",
        "bugged_code": """int[] scores = {1, 2, 3};

System.out.println(scores.length());""",
        "fixed_code": """int[] scores = {1, 2, 3};

System.out.println(scores.length);""",
        "bug_line": 3,
        "line_range": "The length access is on line 3.",
        "bug_type": "Array length is a field, not a method.",
        "fix_hint": "Use scores.length without parentheses.",
        "accepted_answers": ["""int[] scores = {1, 2, 3};

System.out.println(scores.length);"""],
        "explanation": "Arrays expose length as a field. Strings use length(), but arrays use length.",
    },
    {
        "id": "java-arraylist-import",
        "language": "Java",
        "title": "The missing collection import",
        "prompt": "Fix the code so ArrayList is known.",
        "bugged_code": """public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Ada");
    }
}""",
        "fixed_code": """import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Ada");
    }
}""",
        "bug_line": 3,
        "line_range": "The missing setup belongs before the class.",
        "bug_type": "Missing import.",
        "fix_hint": "Import java.util.ArrayList.",
        "accepted_answers": ["""import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Ada");
    }
}"""],
        "explanation": "ArrayList lives in java.util. Importing it lets the compiler resolve the class name.",
    },
    {
        "id": "java-arraylist-add",
        "language": "Java",
        "title": "The appended list",
        "prompt": "Fix the method call so the item is added.",
        "bugged_code": """ArrayList<String> names = new ArrayList<>();
names.append("Grace");""",
        "fixed_code": """ArrayList<String> names = new ArrayList<>();
names.add("Grace");""",
        "bug_line": 2,
        "line_range": "The method name is on line 2.",
        "bug_type": "Wrong ArrayList method.",
        "fix_hint": "Use add instead of append.",
        "accepted_answers": ["""ArrayList<String> names = new ArrayList<>();
names.add("Grace");"""],
        "explanation": "Java ArrayList uses add to insert elements. append is not an ArrayList method.",
    },
    {
        "id": "java-int-division",
        "language": "Java",
        "title": "The rounded average",
        "prompt": "Fix the calculation so the average can include decimals.",
        "bugged_code": """int total = 5;
int count = 2;
double average = total / count;""",
        "fixed_code": """int total = 5;
int count = 2;
double average = (double) total / count;""",
        "bug_line": 3,
        "line_range": "The division is on line 3.",
        "bug_type": "Integer division before assignment to double.",
        "fix_hint": "Cast one operand to double before dividing.",
        "accepted_answers": ["""int total = 5;
int count = 2;
double average = (double) total / count;""", """int total = 5;
int count = 2;
double average = total / (double) count;"""],
        "explanation": "When both operands are ints, Java performs integer division first. Casting before division preserves the decimal part.",
    },
    {
        "id": "java-missing-new",
        "language": "Java",
        "title": "The uncreated scanner",
        "prompt": "Fix the object creation syntax.",
        "bugged_code": """Scanner scanner = Scanner(System.in);""",
        "fixed_code": """Scanner scanner = new Scanner(System.in);""",
        "bug_line": 1,
        "line_range": "The object creation is on line 1.",
        "bug_type": "Missing new keyword.",
        "fix_hint": "Use new before Scanner.",
        "accepted_answers": ["""Scanner scanner = new Scanner(System.in);"""],
        "explanation": "Constructors are called with new in Java. Without new, the syntax is not a valid object creation expression.",
    },
    {
        "id": "java-constructor-return-type",
        "language": "Java",
        "title": "The method pretending to construct",
        "prompt": "Fix the constructor declaration.",
        "bugged_code": """class User {
    void User(String name) {
        this.name = name;
    }
    String name;
}""",
        "fixed_code": """class User {
    User(String name) {
        this.name = name;
    }
    String name;
}""",
        "bug_line": 2,
        "line_range": "The constructor is on line 2.",
        "bug_type": "Constructor has a return type.",
        "fix_hint": "Remove void from the constructor.",
        "accepted_answers": ["""class User {
    User(String name) {
        this.name = name;
    }
    String name;
}"""],
        "explanation": "Constructors have the same name as the class and no return type. Adding void turns it into a normal method.",
    },
    {
        "id": "java-static-context",
        "language": "Java",
        "title": "The instance field in main",
        "prompt": "Fix the code so main can print the name.",
        "bugged_code": """public class Main {
    String name = "Ada";
    public static void main(String[] args) {
        System.out.println(name);
    }
}""",
        "fixed_code": """public class Main {
    String name = "Ada";
    public static void main(String[] args) {
        Main app = new Main();
        System.out.println(app.name);
    }
}""",
        "bug_line": 4,
        "line_range": "The invalid access is on line 4.",
        "bug_type": "Instance field used from static context.",
        "fix_hint": "Create an instance, then read the field from it.",
        "accepted_answers": ["""public class Main {
    String name = "Ada";
    public static void main(String[] args) {
        Main app = new Main();
        System.out.println(app.name);
    }
}""", """public class Main {
    static String name = "Ada";
    public static void main(String[] args) {
        System.out.println(name);
    }
}"""],
        "explanation": "static methods belong to the class, while instance fields belong to objects. You need an object or a static field.",
    },
    {
        "id": "java-break-switch",
        "language": "Java",
        "title": "The falling switch",
        "prompt": "Fix the switch so case 1 does not fall into case 2.",
        "bugged_code": """int option = 1;
switch (option) {
    case 1:
        System.out.println("Start");
    case 2:
        System.out.println("Stop");
}""",
        "fixed_code": """int option = 1;
switch (option) {
    case 1:
        System.out.println("Start");
        break;
    case 2:
        System.out.println("Stop");
}""",
        "bug_line": 4,
        "line_range": "The missing control statement belongs after line 4.",
        "bug_type": "Missing break in switch case.",
        "fix_hint": "Add break after the first case body.",
        "accepted_answers": ["""int option = 1;
switch (option) {
    case 1:
        System.out.println("Start");
        break;
    case 2:
        System.out.println("Stop");
}"""],
        "explanation": "Without break, Java continues executing the next case. break stops the switch after the matching case.",
    },
    {
        "id": "java-for-loop-boundary",
        "language": "Java",
        "title": "The extra loop",
        "prompt": "Fix the loop so it stays within the array.",
        "bugged_code": """int[] scores = {80, 90, 100};
for (int i = 0; i <= scores.length; i++) {
    System.out.println(scores[i]);
}""",
        "fixed_code": """int[] scores = {80, 90, 100};
for (int i = 0; i < scores.length; i++) {
    System.out.println(scores[i]);
}""",
        "bug_line": 2,
        "line_range": "The loop condition is on line 2.",
        "bug_type": "Off-by-one loop boundary.",
        "fix_hint": "Use < scores.length, not <=.",
        "accepted_answers": ["""int[] scores = {80, 90, 100};
for (int i = 0; i < scores.length; i++) {
    System.out.println(scores[i]);
}"""],
        "explanation": "The last valid index is length - 1. <= length runs one iteration too many.",
    },
    {
        "id": "java-enhanced-for-type",
        "language": "Java",
        "title": "The wrong loop variable type",
        "prompt": "Fix the enhanced for loop variable type.",
        "bugged_code": """String[] names = {"Ada", "Grace"};
for (int name : names) {
    System.out.println(name);
}""",
        "fixed_code": """String[] names = {"Ada", "Grace"};
for (String name : names) {
    System.out.println(name);
}""",
        "bug_line": 2,
        "line_range": "The loop variable is on line 2.",
        "bug_type": "Enhanced for loop variable has the wrong type.",
        "fix_hint": "Use String because names contains strings.",
        "accepted_answers": ["""String[] names = {"Ada", "Grace"};
for (String name : names) {
    System.out.println(name);
}"""],
        "explanation": "The loop variable type must be compatible with each element in the array.",
    },
    {
        "id": "java-null-pointer",
        "language": "Java",
        "title": "The empty name",
        "prompt": "Fix the null check before calling a method.",
        "bugged_code": """String name = null;

if (name.length() > 0) {
    System.out.println(name);
}""",
        "fixed_code": """String name = null;

if (name != null && name.length() > 0) {
    System.out.println(name);
}""",
        "bug_line": 3,
        "line_range": "The unsafe method call is on line 3.",
        "bug_type": "Possible NullPointerException.",
        "fix_hint": "Check name != null before calling length().",
        "accepted_answers": ["""String name = null;

if (name != null && name.length() > 0) {
    System.out.println(name);
}"""],
        "explanation": "Calling a method on null throws NullPointerException. The null check must happen first.",
    },
    {
        "id": "java-char-quotes",
        "language": "Java",
        "title": "The long character",
        "prompt": "Fix the type so the text value is valid.",
        "bugged_code": """char grade = "A";""",
        "fixed_code": """char grade = 'A';""",
        "bug_line": 1,
        "line_range": "The literal is on line 1.",
        "bug_type": "char uses single quotes.",
        "fix_hint": "Use 'A' or change the type to String.",
        "accepted_answers": ["""char grade = 'A';""", """String grade = "A";"""],
        "explanation": "A char literal uses single quotes and holds one character. Double quotes create a String.",
    },
    {
        "id": "java-boolean-case",
        "language": "Java",
        "title": "The capital truth",
        "prompt": "Fix the boolean literal.",
        "bugged_code": """boolean ready = True;""",
        "fixed_code": """boolean ready = true;""",
        "bug_line": 1,
        "line_range": "The boolean value is on line 1.",
        "bug_type": "Boolean literal has the wrong capitalization.",
        "fix_hint": "Use lowercase true.",
        "accepted_answers": ["""boolean ready = true;"""],
        "explanation": "Java boolean literals are lowercase true and false.",
    },
    {
        "id": "java-implements-interface",
        "language": "Java",
        "title": "The extended interface",
        "prompt": "Fix the class declaration so it implements the interface.",
        "bugged_code": """interface Printable {
    void print();
}

class Report extends Printable {
    public void print() {}
}""",
        "fixed_code": """interface Printable {
    void print();
}

class Report implements Printable {
    public void print() {}
}""",
        "bug_line": 5,
        "line_range": "The class declaration is on line 5.",
        "bug_type": "Class uses extends instead of implements for an interface.",
        "fix_hint": "Use implements Printable.",
        "accepted_answers": ["""interface Printable {
    void print();
}

class Report implements Printable {
    public void print() {}
}"""],
        "explanation": "Classes implement interfaces. extends is used for inheriting from a class.",
    },
    {
        "id": "java-override-access",
        "language": "Java",
        "title": "The hidden override",
        "prompt": "Fix the method visibility so it correctly overrides.",
        "bugged_code": """class Parent {
    public void run() {}
}

class Child extends Parent {
    void run() {}
}""",
        "fixed_code": """class Parent {
    public void run() {}
}

class Child extends Parent {
    public void run() {}
}""",
        "bug_line": 6,
        "line_range": "The overriding method is on line 6.",
        "bug_type": "Overriding method has weaker access.",
        "fix_hint": "Make the child method public.",
        "accepted_answers": ["""class Parent {
    public void run() {}
}

class Child extends Parent {
    public void run() {}
}"""],
        "explanation": "An overriding method cannot reduce visibility. A public parent method must remain public in the child.",
    },
    {
        "id": "java-missing-return",
        "language": "Java",
        "title": "The silent method",
        "prompt": "Fix the method so it returns an int.",
        "bugged_code": """int doubleNumber(int number) {
    number * 2;
}""",
        "fixed_code": """int doubleNumber(int number) {
    return number * 2;
}""",
        "bug_line": 2,
        "line_range": "The method body is line 2.",
        "bug_type": "Missing return statement.",
        "fix_hint": "Return number * 2.",
        "accepted_answers": ["""int doubleNumber(int number) {
    return number * 2;
}"""],
        "explanation": "A method declared to return int must return an int on every valid path.",
    },
    {
        "id": "java-unreachable-code",
        "language": "Java",
        "title": "The unreachable print",
        "prompt": "Fix the method so the print statement can run.",
        "bugged_code": """int getScore() {
    return 100;
    System.out.println("Done");
}""",
        "fixed_code": """int getScore() {
    System.out.println("Done");
    return 100;
}""",
        "bug_line": 3,
        "line_range": "The unreachable statement is on line 3.",
        "bug_type": "Code appears after return.",
        "fix_hint": "Move the print before the return.",
        "accepted_answers": ["""int getScore() {
    System.out.println("Done");
    return 100;
}"""],
        "explanation": "return exits the method immediately. Statements after it cannot execute, so Java rejects them.",
    },
    {
        "id": "java-package-order",
        "language": "Java",
        "title": "The late package",
        "prompt": "Fix the file order so the package declaration comes first.",
        "bugged_code": """import java.util.List;
package app;

public class Main {}""",
        "fixed_code": """package app;

import java.util.List;

public class Main {}""",
        "bug_line": 2,
        "line_range": "The package declaration is on line 2.",
        "bug_type": "Package declaration must come before imports.",
        "fix_hint": "Move package app; to the top.",
        "accepted_answers": ["""package app;

import java.util.List;

public class Main {}"""],
        "explanation": "If a Java file has a package declaration, it must be the first non-comment statement.",
    },
    {
        "id": "java-generic-primitive",
        "language": "Java",
        "title": "The primitive list",
        "prompt": "Fix the generic type so the list can store integers.",
        "bugged_code": """ArrayList<int> numbers = new ArrayList<>();""",
        "fixed_code": """ArrayList<Integer> numbers = new ArrayList<>();""",
        "bug_line": 1,
        "line_range": "The generic type is on line 1.",
        "bug_type": "Generic type uses a primitive.",
        "fix_hint": "Use Integer instead of int.",
        "accepted_answers": ["""ArrayList<Integer> numbers = new ArrayList<>();"""],
        "explanation": "Java generics require reference types. Integer is the wrapper type for int.",
    },
    {
        "id": "java-catch-order",
        "language": "Java",
        "title": "The unreachable catch",
        "prompt": "Fix the catch order so the specific exception can be handled.",
        "bugged_code": """try {
    Integer.parseInt("abc");
} catch (Exception ex) {
    System.out.println("Problem");
} catch (NumberFormatException ex) {
    System.out.println("Bad number");
}""",
        "fixed_code": """try {
    Integer.parseInt("abc");
} catch (NumberFormatException ex) {
    System.out.println("Bad number");
} catch (Exception ex) {
    System.out.println("Problem");
}""",
        "bug_line": 3,
        "line_range": "Compare the catch blocks starting on lines 3 and 5.",
        "bug_type": "Broad exception caught before specific exception.",
        "fix_hint": "Catch NumberFormatException before Exception.",
        "accepted_answers": ["""try {
    Integer.parseInt("abc");
} catch (NumberFormatException ex) {
    System.out.println("Bad number");
} catch (Exception ex) {
    System.out.println("Problem");
}"""],
        "explanation": "Exception catches every NumberFormatException first, so the later specific catch can never run.",
    },
    {
        "id": "java-interface-method-body",
        "language": "Java",
        "title": "The interface body",
        "prompt": "Fix the interface method declaration.",
        "bugged_code": """interface RunnableTask {
    void run() {
    }
}""",
        "fixed_code": """interface RunnableTask {
    void run();
}""",
        "bug_line": 2,
        "line_range": "The interface method starts on line 2.",
        "bug_type": "Interface method has a body without default/static.",
        "fix_hint": "End the method declaration with a semicolon.",
        "accepted_answers": ["""interface RunnableTask {
    void run();
}"""],
        "explanation": "Ordinary interface methods are declarations. They do not have bodies unless declared default or static.",
    },
    {
        "id": "java-final-reassign",
        "language": "Java",
        "title": "The locked value",
        "prompt": "Fix the variable so its value can change.",
        "bugged_code": """final int attempts = 0;
attempts++;""",
        "fixed_code": """int attempts = 0;
attempts++;""",
        "bug_line": 1,
        "line_range": "The modifier on line 1 prevents the update.",
        "bug_type": "Reassigning a final variable.",
        "fix_hint": "Remove final if attempts needs to change.",
        "accepted_answers": ["""int attempts = 0;
attempts++;"""],
        "explanation": "final variables can be assigned only once. Incrementing them is a reassignment.",
    },
    {
        "id": "java-missing-parenthesis-method",
        "language": "Java",
        "title": "The uncalled method",
        "prompt": "Fix the method call so the string is lowercased.",
        "bugged_code": """String name = "ADA";
System.out.println(name.toLowerCase);""",
        "fixed_code": """String name = "ADA";
System.out.println(name.toLowerCase());""",
        "bug_line": 2,
        "line_range": "The method call is on line 2.",
        "bug_type": "Method call missing parentheses.",
        "fix_hint": "Add () after toLowerCase.",
        "accepted_answers": ["""String name = "ADA";
System.out.println(name.toLowerCase());"""],
        "explanation": "Methods must be invoked with parentheses. Without them, Java is not calling toLowerCase.",
    },
    {
        "id": "java-while-update",
        "language": "Java",
        "title": "The stuck loop",
        "prompt": "Fix the while loop so it eventually ends.",
        "bugged_code": """int count = 3;
while (count > 0) {
    System.out.println(count);
}""",
        "fixed_code": """int count = 3;
while (count > 0) {
    System.out.println(count);
    count--;
}""",
        "bug_line": 3,
        "line_range": "The loop body is missing an update.",
        "bug_type": "Loop counter is never changed.",
        "fix_hint": "Decrement count inside the loop.",
        "accepted_answers": ["""int count = 3;
while (count > 0) {
    System.out.println(count);
    count--;
}"""],
        "explanation": "The while condition stays true unless count changes. Decrementing count allows the loop to finish.",
    },
]


SQL_PROBLEMS = [
    {
        "id": "sql-select-from-order",
        "language": "SQL",
        "title": "The backwards query",
        "prompt": "Fix the query clause order.",
        "bugged_code": """FROM users
SELECT name;""",
        "fixed_code": """SELECT name
FROM users;""",
        "bug_line": 1,
        "line_range": "The clauses are in the wrong order.",
        "bug_type": "SELECT must come before FROM.",
        "fix_hint": "Start with SELECT, then name the table with FROM.",
        "accepted_answers": ["""SELECT name
FROM users;"""],
        "explanation": "A basic SQL query selects columns first and then identifies the source table.",
    },
    {
        "id": "sql-missing-comma-columns",
        "language": "SQL",
        "title": "The crowded select list",
        "prompt": "Fix the SELECT list so both columns are returned.",
        "bugged_code": """SELECT first_name last_name
FROM users;""",
        "fixed_code": """SELECT first_name, last_name
FROM users;""",
        "bug_line": 1,
        "line_range": "The select list is on line 1.",
        "bug_type": "Missing comma between selected columns.",
        "fix_hint": "Add a comma after first_name.",
        "accepted_answers": ["""SELECT first_name, last_name
FROM users;"""],
        "explanation": "Multiple selected columns must be separated with commas.",
    },
    {
        "id": "sql-where-equals",
        "language": "SQL",
        "title": "The double equals",
        "prompt": "Fix the comparison operator in the WHERE clause.",
        "bugged_code": """SELECT *
FROM users
WHERE role == 'admin';""",
        "fixed_code": """SELECT *
FROM users
WHERE role = 'admin';""",
        "bug_line": 3,
        "line_range": "The comparison is on line 3.",
        "bug_type": "SQL equality uses a single equals sign.",
        "fix_hint": "Use = instead of ==.",
        "accepted_answers": ["""SELECT *
FROM users
WHERE role = 'admin';"""],
        "explanation": "Standard SQL uses = for equality comparisons. == is not portable SQL syntax.",
    },
    {
        "id": "sql-string-quotes",
        "language": "SQL",
        "title": "The unquoted status",
        "prompt": "Fix the filter so the text value is treated as a string.",
        "bugged_code": """SELECT *
FROM orders
WHERE status = shipped;""",
        "fixed_code": """SELECT *
FROM orders
WHERE status = 'shipped';""",
        "bug_line": 3,
        "line_range": "The literal value is on line 3.",
        "bug_type": "String literal missing quotes.",
        "fix_hint": "Put shipped in single quotes.",
        "accepted_answers": ["""SELECT *
FROM orders
WHERE status = 'shipped';"""],
        "explanation": "Unquoted words are read as identifiers such as column names. Text literals need quotes.",
    },
    {
        "id": "sql-null-comparison",
        "language": "SQL",
        "title": "The missing null check",
        "prompt": "Fix the query so it finds rows with no email.",
        "bugged_code": """SELECT *
FROM users
WHERE email = NULL;""",
        "fixed_code": """SELECT *
FROM users
WHERE email IS NULL;""",
        "bug_line": 3,
        "line_range": "The NULL comparison is on line 3.",
        "bug_type": "NULL compared with = instead of IS NULL.",
        "fix_hint": "Use IS NULL.",
        "accepted_answers": ["""SELECT *
FROM users
WHERE email IS NULL;"""],
        "explanation": "NULL means unknown or missing. SQL uses IS NULL and IS NOT NULL to test it.",
    },
    {
        "id": "sql-order-by-position",
        "language": "SQL",
        "title": "The early sort",
        "prompt": "Fix the clause order so filtering happens before sorting.",
        "bugged_code": """SELECT *
FROM products
ORDER BY price
WHERE price > 10;""",
        "fixed_code": """SELECT *
FROM products
WHERE price > 10
ORDER BY price;""",
        "bug_line": 3,
        "line_range": "ORDER BY and WHERE are reversed.",
        "bug_type": "ORDER BY appears before WHERE.",
        "fix_hint": "Place WHERE before ORDER BY.",
        "accepted_answers": ["""SELECT *
FROM products
WHERE price > 10
ORDER BY price;"""],
        "explanation": "SQL clause order places WHERE before ORDER BY.",
    },
    {
        "id": "sql-group-by-aggregate",
        "language": "SQL",
        "title": "The ungrouped role",
        "prompt": "Fix the aggregate query so each role gets a count.",
        "bugged_code": """SELECT role, COUNT(*)
FROM users;""",
        "fixed_code": """SELECT role, COUNT(*)
FROM users
GROUP BY role;""",
        "bug_line": 2,
        "line_range": "The missing grouping belongs after line 2.",
        "bug_type": "Non-aggregated column selected without GROUP BY.",
        "fix_hint": "Group by role.",
        "accepted_answers": ["""SELECT role, COUNT(*)
FROM users
GROUP BY role;"""],
        "explanation": "When selecting an ordinary column with an aggregate, SQL needs GROUP BY to define the groups.",
    },
    {
        "id": "sql-having-vs-where",
        "language": "SQL",
        "title": "The aggregate filter",
        "prompt": "Fix the query so it filters grouped counts.",
        "bugged_code": """SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
WHERE COUNT(*) > 2;""",
        "fixed_code": """SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 2;""",
        "bug_line": 4,
        "line_range": "The aggregate filter is on line 4.",
        "bug_type": "WHERE used for an aggregate condition.",
        "fix_hint": "Use HAVING after GROUP BY.",
        "accepted_answers": ["""SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 2;"""],
        "explanation": "WHERE filters rows before grouping. HAVING filters groups after aggregate values are computed.",
    },
    {
        "id": "sql-inner-join-on",
        "language": "SQL",
        "title": "The join without a match",
        "prompt": "Fix the join so orders match their users.",
        "bugged_code": """SELECT users.name, orders.total
FROM users
JOIN orders;""",
        "fixed_code": """SELECT users.name, orders.total
FROM users
JOIN orders ON orders.user_id = users.id;""",
        "bug_line": 3,
        "line_range": "The JOIN on line 3 is missing a condition.",
        "bug_type": "JOIN missing ON condition.",
        "fix_hint": "Add ON orders.user_id = users.id.",
        "accepted_answers": ["""SELECT users.name, orders.total
FROM users
JOIN orders ON orders.user_id = users.id;"""],
        "explanation": "A join condition tells SQL which rows from each table belong together.",
    },
    {
        "id": "sql-ambiguous-column",
        "language": "SQL",
        "title": "The ambiguous id",
        "prompt": "Fix the selected id so SQL knows which table it comes from.",
        "bugged_code": """SELECT id, name
FROM users
JOIN orders ON orders.user_id = users.id;""",
        "fixed_code": """SELECT users.id, users.name
FROM users
JOIN orders ON orders.user_id = users.id;""",
        "bug_line": 1,
        "line_range": "The ambiguous column is in the SELECT list.",
        "bug_type": "Column name exists in multiple joined tables.",
        "fix_hint": "Qualify id with the table name.",
        "accepted_answers": ["""SELECT users.id, users.name
FROM users
JOIN orders ON orders.user_id = users.id;"""],
        "explanation": "Joined tables often share column names like id. Prefixing the table removes ambiguity.",
    },
    {
        "id": "sql-in-list",
        "language": "SQL",
        "title": "The repeated equality",
        "prompt": "Fix the filter so it matches either role.",
        "bugged_code": """SELECT *
FROM users
WHERE role = ('admin', 'editor');""",
        "fixed_code": """SELECT *
FROM users
WHERE role IN ('admin', 'editor');""",
        "bug_line": 3,
        "line_range": "The multi-value filter is on line 3.",
        "bug_type": "Using = with a list of values.",
        "fix_hint": "Use IN for multiple possible values.",
        "accepted_answers": ["""SELECT *
FROM users
WHERE role IN ('admin', 'editor');"""],
        "explanation": "IN checks whether a value appears in a list. = compares against one value.",
    },
    {
        "id": "sql-like-wildcard",
        "language": "SQL",
        "title": "The exact search",
        "prompt": "Fix the search so it finds names starting with A.",
        "bugged_code": """SELECT *
FROM users
WHERE name LIKE 'A';""",
        "fixed_code": """SELECT *
FROM users
WHERE name LIKE 'A%';""",
        "bug_line": 3,
        "line_range": "The LIKE pattern is on line 3.",
        "bug_type": "LIKE pattern missing wildcard.",
        "fix_hint": "Add % after A.",
        "accepted_answers": ["""SELECT *
FROM users
WHERE name LIKE 'A%';"""],
        "explanation": "% matches any number of characters. Without it, LIKE 'A' matches only the exact string A.",
    },
    {
        "id": "sql-insert-column-count",
        "language": "SQL",
        "title": "The missing inserted value",
        "prompt": "Fix the INSERT so the number of columns and values match.",
        "bugged_code": """INSERT INTO users (name, email)
VALUES ('Ada');""",
        "fixed_code": """INSERT INTO users (name, email)
VALUES ('Ada', 'ada@example.com');""",
        "bug_line": 2,
        "line_range": "The values list is on line 2.",
        "bug_type": "INSERT column count does not match value count.",
        "fix_hint": "Add a value for email.",
        "accepted_answers": ["""INSERT INTO users (name, email)
VALUES ('Ada', 'ada@example.com');"""],
        "explanation": "Each listed column needs a corresponding value in the same order.",
    },
    {
        "id": "sql-update-missing-where",
        "language": "SQL",
        "title": "The global update",
        "prompt": "Fix the UPDATE so it only changes one user.",
        "bugged_code": """UPDATE users
SET role = 'admin';""",
        "fixed_code": """UPDATE users
SET role = 'admin'
WHERE id = 1;""",
        "bug_line": 2,
        "line_range": "The missing filter belongs after line 2.",
        "bug_type": "UPDATE missing WHERE clause.",
        "fix_hint": "Add a WHERE clause for the intended row.",
        "accepted_answers": ["""UPDATE users
SET role = 'admin'
WHERE id = 1;"""],
        "explanation": "Without WHERE, UPDATE changes every row in the table.",
    },
    {
        "id": "sql-delete-missing-where",
        "language": "SQL",
        "title": "The dangerous delete",
        "prompt": "Fix the DELETE so it removes only inactive users.",
        "bugged_code": """DELETE FROM users;""",
        "fixed_code": """DELETE FROM users
WHERE active = false;""",
        "bug_line": 1,
        "line_range": "The missing filter belongs after the DELETE.",
        "bug_type": "DELETE missing WHERE clause.",
        "fix_hint": "Add WHERE active = false.",
        "accepted_answers": ["""DELETE FROM users
WHERE active = false;"""],
        "explanation": "DELETE without WHERE removes all rows. A WHERE clause limits the deletion.",
    },
    {
        "id": "sql-alias-syntax",
        "language": "SQL",
        "title": "The quoted alias",
        "prompt": "Fix the alias syntax so the count has a readable name.",
        "bugged_code": """SELECT COUNT(*) = total_users
FROM users;""",
        "fixed_code": """SELECT COUNT(*) AS total_users
FROM users;""",
        "bug_line": 1,
        "line_range": "The alias is on line 1.",
        "bug_type": "Alias written with = instead of AS.",
        "fix_hint": "Use AS total_users.",
        "accepted_answers": ["""SELECT COUNT(*) AS total_users
FROM users;""", """SELECT COUNT(*) total_users
FROM users;"""],
        "explanation": "AS gives an expression a result column name. = is a comparison operator.",
    },
    {
        "id": "sql-distinct-position",
        "language": "SQL",
        "title": "The misplaced distinct",
        "prompt": "Fix the query so it returns unique countries.",
        "bugged_code": """SELECT country DISTINCT
FROM users;""",
        "fixed_code": """SELECT DISTINCT country
FROM users;""",
        "bug_line": 1,
        "line_range": "The DISTINCT keyword is misplaced on line 1.",
        "bug_type": "DISTINCT belongs after SELECT.",
        "fix_hint": "Place DISTINCT before the selected column.",
        "accepted_answers": ["""SELECT DISTINCT country
FROM users;"""],
        "explanation": "DISTINCT modifies the SELECT result set and appears immediately after SELECT.",
    },
    {
        "id": "sql-limit-order",
        "language": "SQL",
        "title": "The early limit",
        "prompt": "Fix the query so it sorts before limiting.",
        "bugged_code": """SELECT *
FROM products
LIMIT 5
ORDER BY price DESC;""",
        "fixed_code": """SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;""",
        "bug_line": 3,
        "line_range": "LIMIT and ORDER BY are reversed.",
        "bug_type": "LIMIT appears before ORDER BY.",
        "fix_hint": "Put LIMIT after ORDER BY.",
        "accepted_answers": ["""SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;"""],
        "explanation": "In common SQL dialects, ORDER BY comes before LIMIT so rows are sorted before the result is trimmed.",
    },
    {
        "id": "sql-between-and",
        "language": "SQL",
        "title": "The incomplete range",
        "prompt": "Fix the BETWEEN expression.",
        "bugged_code": """SELECT *
FROM orders
WHERE total BETWEEN 10 100;""",
        "fixed_code": """SELECT *
FROM orders
WHERE total BETWEEN 10 AND 100;""",
        "bug_line": 3,
        "line_range": "The range expression is on line 3.",
        "bug_type": "BETWEEN missing AND.",
        "fix_hint": "Add AND between the lower and upper bounds.",
        "accepted_answers": ["""SELECT *
FROM orders
WHERE total BETWEEN 10 AND 100;"""],
        "explanation": "BETWEEN requires a lower bound, AND, and an upper bound.",
    },
    {
        "id": "sql-create-table-comma",
        "language": "SQL",
        "title": "The crowded columns",
        "prompt": "Fix the CREATE TABLE statement.",
        "bugged_code": """CREATE TABLE users (
  id INTEGER PRIMARY KEY
  name TEXT
);""",
        "fixed_code": """CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT
);""",
        "bug_line": 2,
        "line_range": "The column definitions are lines 2-3.",
        "bug_type": "Missing comma between column definitions.",
        "fix_hint": "Add a comma after the id column definition.",
        "accepted_answers": ["""CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT
);"""],
        "explanation": "Column definitions inside CREATE TABLE are separated with commas.",
    },
    {
        "id": "sql-primary-key-spelling",
        "language": "SQL",
        "title": "The misspelled key",
        "prompt": "Fix the primary key declaration.",
        "bugged_code": """CREATE TABLE users (
  id INTEGER PRIMARYKEY
);""",
        "fixed_code": """CREATE TABLE users (
  id INTEGER PRIMARY KEY
);""",
        "bug_line": 2,
        "line_range": "The constraint is on line 2.",
        "bug_type": "PRIMARY KEY must be two words.",
        "fix_hint": "Write PRIMARY KEY with a space.",
        "accepted_answers": ["""CREATE TABLE users (
  id INTEGER PRIMARY KEY
);"""],
        "explanation": "PRIMARY KEY is a two-word SQL constraint. Combining the words changes the token.",
    },
    {
        "id": "sql-count-column-null",
        "language": "SQL",
        "title": "The missing rows in count",
        "prompt": "Fix the count so every row is included.",
        "bugged_code": """SELECT COUNT(email)
FROM users;""",
        "fixed_code": """SELECT COUNT(*)
FROM users;""",
        "bug_line": 1,
        "line_range": "The count expression is on line 1.",
        "bug_type": "COUNT(column) skips NULL values.",
        "fix_hint": "Use COUNT(*) to count rows.",
        "accepted_answers": ["""SELECT COUNT(*)
FROM users;"""],
        "explanation": "COUNT(email) counts non-NULL email values. COUNT(*) counts rows.",
    },
    {
        "id": "sql-left-join-filter",
        "language": "SQL",
        "title": "The filtered-out left join",
        "prompt": "Fix the query so users without orders are preserved.",
        "bugged_code": """SELECT users.name, orders.total
FROM users
LEFT JOIN orders ON orders.user_id = users.id
WHERE orders.status = 'paid';""",
        "fixed_code": """SELECT users.name, orders.total
FROM users
LEFT JOIN orders
  ON orders.user_id = users.id
 AND orders.status = 'paid';""",
        "bug_line": 4,
        "line_range": "The right-table filter is on line 4.",
        "bug_type": "WHERE filter turns a LEFT JOIN into an inner-style result.",
        "fix_hint": "Move the right-table filter into the ON clause.",
        "accepted_answers": ["""SELECT users.name, orders.total
FROM users
LEFT JOIN orders
  ON orders.user_id = users.id
 AND orders.status = 'paid';"""],
        "explanation": "A WHERE condition on the right table removes NULL joined rows. Putting it in ON keeps unmatched left rows.",
    },
    {
        "id": "sql-union-column-count",
        "language": "SQL",
        "title": "The uneven union",
        "prompt": "Fix the UNION so both queries return the same number of columns.",
        "bugged_code": """SELECT name, email FROM users
UNION
SELECT name FROM admins;""",
        "fixed_code": """SELECT name, email FROM users
UNION
SELECT name, email FROM admins;""",
        "bug_line": 3,
        "line_range": "Compare the SELECT lists on lines 1 and 3.",
        "bug_type": "UNION queries have different column counts.",
        "fix_hint": "Select the same number of columns on both sides.",
        "accepted_answers": ["""SELECT name, email FROM users
UNION
SELECT name, email FROM admins;"""],
        "explanation": "UNION stacks result sets, so each SELECT must produce the same number of compatible columns.",
    },
    {
        "id": "sql-case-end",
        "language": "SQL",
        "title": "The unfinished case",
        "prompt": "Fix the CASE expression.",
        "bugged_code": """SELECT
  CASE WHEN score >= 70 THEN 'pass' ELSE 'retry' AS result
FROM exams;""",
        "fixed_code": """SELECT
  CASE WHEN score >= 70 THEN 'pass' ELSE 'retry' END AS result
FROM exams;""",
        "bug_line": 2,
        "line_range": "The CASE expression is on line 2.",
        "bug_type": "CASE expression missing END.",
        "fix_hint": "Add END before the alias.",
        "accepted_answers": ["""SELECT
  CASE WHEN score >= 70 THEN 'pass' ELSE 'retry' END AS result
FROM exams;"""],
        "explanation": "CASE expressions must be closed with END before they can be aliased or selected.",
    },
    {
        "id": "sql-subquery-parentheses",
        "language": "SQL",
        "title": "The bare subquery",
        "prompt": "Fix the IN subquery syntax.",
        "bugged_code": """SELECT *
FROM users
WHERE id IN SELECT user_id FROM orders;""",
        "fixed_code": """SELECT *
FROM users
WHERE id IN (SELECT user_id FROM orders);""",
        "bug_line": 3,
        "line_range": "The subquery starts on line 3.",
        "bug_type": "Subquery missing parentheses.",
        "fix_hint": "Wrap the SELECT subquery in parentheses.",
        "accepted_answers": ["""SELECT *
FROM users
WHERE id IN (SELECT user_id FROM orders);"""],
        "explanation": "Subqueries used as expressions need parentheses so SQL can parse them as one value-producing expression.",
    },
    {
        "id": "sql-join-table-alias",
        "language": "SQL",
        "title": "The unknown alias",
        "prompt": "Fix the table alias used in the join condition.",
        "bugged_code": """SELECT u.name, o.total
FROM users u
JOIN orders ord ON o.user_id = u.id;""",
        "fixed_code": """SELECT u.name, o.total
FROM users u
JOIN orders o ON o.user_id = u.id;""",
        "bug_line": 3,
        "line_range": "The aliases are inconsistent on line 3.",
        "bug_type": "Alias used before it is defined.",
        "fix_hint": "Alias orders as o, or use ord consistently.",
        "accepted_answers": ["""SELECT u.name, o.total
FROM users u
JOIN orders o ON o.user_id = u.id;""", """SELECT u.name, ord.total
FROM users u
JOIN orders ord ON ord.user_id = u.id;"""],
        "explanation": "Once a table has an alias, queries must use that alias consistently.",
    },
    {
        "id": "sql-desc-keyword",
        "language": "SQL",
        "title": "The descending typo",
        "prompt": "Fix the sort direction keyword.",
        "bugged_code": """SELECT *
FROM products
ORDER BY price DESCENDING;""",
        "fixed_code": """SELECT *
FROM products
ORDER BY price DESC;""",
        "bug_line": 3,
        "line_range": "The sort direction is on line 3.",
        "bug_type": "Invalid descending sort keyword.",
        "fix_hint": "Use DESC.",
        "accepted_answers": ["""SELECT *
FROM products
ORDER BY price DESC;"""],
        "explanation": "SQL uses ASC and DESC for sort direction. DESCENDING is not the standard keyword.",
    },
    {
        "id": "sql-not-equal",
        "language": "SQL",
        "title": "The JavaScript inequality",
        "prompt": "Fix the not-equal operator.",
        "bugged_code": """SELECT *
FROM users
WHERE role !== 'admin';""",
        "fixed_code": """SELECT *
FROM users
WHERE role <> 'admin';""",
        "bug_line": 3,
        "line_range": "The comparison operator is on line 3.",
        "bug_type": "JavaScript inequality used in SQL.",
        "fix_hint": "Use <> for not equal.",
        "accepted_answers": ["""SELECT *
FROM users
WHERE role <> 'admin';""", """SELECT *
FROM users
WHERE role != 'admin';"""],
        "explanation": "SQL commonly uses <> for not equal. !== is a JavaScript operator, not standard SQL.",
    },
    {
        "id": "sql-trailing-comma",
        "language": "SQL",
        "title": "The dangling select comma",
        "prompt": "Fix the SELECT list syntax.",
        "bugged_code": """SELECT name, email,
FROM users;""",
        "fixed_code": """SELECT name, email
FROM users;""",
        "bug_line": 1,
        "line_range": "The extra comma is on line 1.",
        "bug_type": "Trailing comma before FROM.",
        "fix_hint": "Remove the comma after email.",
        "accepted_answers": ["""SELECT name, email
FROM users;"""],
        "explanation": "A comma means another selected expression is coming. FROM cannot appear immediately after a dangling comma.",
    },
]
