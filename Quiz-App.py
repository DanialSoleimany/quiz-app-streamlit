import streamlit as st

# Define quiz questions, answers, and options
questions_data = [
    {
        "question": "**What is the output of this code?**  \n animal = 'bear'  \nanimal = 'lion'  \n print(animal)",
        "answer": "'lion'",
        "options": ["'bear'", "animal", "'lion'", "error"]
    },
    {
        "question": "**What is the output of this code?**  \n name = 'Jack'  \nName = 'Sara'  \n print(name)",
        "answer": "'Jack'",
        "options": ["'Sara'", "Name", "name", "'Jack'"]
    },
    {
        "question": "**Which one is valid in naming a variable?**",
        "answer": "myQuestion = 'How to program an application?'",
        "options": [
            "1_number = 1000",
            "my_variable! = 'Hello World!'",
            "myQuestion = 'How to program an application?'",
            "my-name = 'Jeff'"
        ]
    },
    {
        "question": "**Which one causes error?**",
        "answer": """print("Hello World')""",
        "options": [
            """print("Hello World')""",
            """print("This is my saying: \ "Be friend with yourself!\ " ") """,
            """print('I\ 'm the greatest person in history')""",
            """print('2' + str(2))"""
        ]
    },
    {
        "question": "**Among the following options, which one does not accurately represent a benefit of comments in Python?**",
        "answer": "Optimize the code",
        "options": [
            "Optimize the code",
            "Explain Python code",
            "Prevent execution when testing code",
            "Make the code more readable"
        ]
    },
    {
        "question": "**The output of which one is 33?**",
        "answer": "'3' + str(3)",
        "options": [
            "str(3) + 3",
            "3 + int(3.3)",
            "'3' + str(3)",
            "3 + float(3)"
        ]
    },
    {
        "question": """**Which options are correct?**    \n 1\) 3 + int(2.2) -> output = 5.    \n 2\) float(32) + int(3.4) -> output = 35.0    \n 3\) 2 + '3' -> output = 5    \n 4\) str(2) * 2 = 22""",
        "answer": "2, 4",
        "options": [
            "1, 2, 3",
            "1, 2, 4",
            "2, 3",
            "2, 4"
        ]
    },
    {
        "question": "**Which one is correct in naming variables?**",
        "answer": "myName = 'Carl'",
        "options": [
            "type = 4",
            "myName = 'Carl'",
            "for = 'This is a string'",
            "my music = 'Top in Playlist'"
        ]
    },
    {
        "question": "**Which one is not a feature of a variable in Python?**",
        "answer": "It's a data type in Python",
        "options": [
            "It is created the moment you first assign a value to it",
            "A Container for storing data values",
            "It's a data type in Python",
            "Python has no command for declaring a variable"
        ]
    },
    {
        "question": "**Which one shows the snake_case?**",
        "answer": "my_interesting_music = 'Pop Musics.'",
        "options": [
            "myVariable = 'This is a variable'",
            "BagOfMyBrother = 'So Cool!'",
            "my_interesting_music = 'Pop Musics.'",
            "None of them"
        ]
    }
]

# Display quiz questions
st.write(""" # Quiz Web Application - Part. 1 \n
Challenge yourself with these **10 questions**.\n
**Let's Get Started!**""")

# Function to display a quiz question and collect answer
def display_question(question_data, key):
    user_answer = st.radio(question_data["question"], question_data["options"])
    btn = st.button("Submit", key=key)
    if btn:
        if user_answer == question_data["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect!")

# Iterate over each question
for i, question_data in enumerate(questions_data, start=1):
    key = f"Q{i}"
    with st.expander(f"Question {i}"):
        display_question(question_data, key)
