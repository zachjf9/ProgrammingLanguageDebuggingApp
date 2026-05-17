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
