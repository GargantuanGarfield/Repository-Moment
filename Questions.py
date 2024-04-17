# Will: embedded lists for each question type
# The type of question will act as its difficulty with True-False being the easiest and jeopardy being the hardest
choices = ["int()", "float", "boolean", "for loop", "killer app", "pickle", "import", "break", "function", "type", "in"
           , "matplot", "scroll down", "objected oriented programming"]

MCQ = {1: {"A data value represented by True or False": choices[2]}, 2:
    {"Module that lets you read and write to files in binary": choices[5]},
    3: {"The Module you import to generate graphs": choices[11]}, 4: {"Classes are used as apart of what?": choices[13]}
    , 5: {"The Keyword used to check whether a value is found in another, such as a list.": choices[10]}}


TFQ = {1: {" The \"int()\" function in Python can convert a string containing a floating-point number "
        "to an integer without loss of information": "false"}, 2: {" Variables in different blocks "
        "of codes, such as functions, can have the same name without causing errors": "true"},
        3: {" Tuples are mutable": "false"}, 4: {" \".keys()\" will return all the keys "
        "in the specified list": "true"}, 5: {"  Python is a compiled language": "False"}}

JEOPARDY = {1: {"In Python, this type of method is automatically called when an instance of a class is created.":
            "init"}, 2: {"This type of Python exception occurs when an invalid operation is performed on an object, "
            "such as dividing by zero or accessing an index out of range.": "typeerror"}, 3:
            {"a block of code which only runs when it is called": "Function"}, 4: {"A loop based on a conditional":
            "while loop"}, 5: {"This syntax in Python is used to create a list through a for loop on a single line":
            "list comprehension"}}

FITB = {1: {"In Python, the ______ statement is used to handle exceptions and perform error handling."
            : "try/accept"}, 2: {"Python's built-in function ______() is used to convert a string to an integer."
            : "int"}, 3: {"The ______() method in Python is used to remove "
            "the last element from a list and return it.": "int"}, 4: {"Python's ______() function is used to determine "
            "the length of a sequence, such as a list or a string.": "len"}, 5: {"The ______() method in Python is used"
            " to add elements to the end of a list.": "append"}}


