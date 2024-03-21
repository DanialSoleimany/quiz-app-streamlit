import streamlit as st


if "Question_1" not in st.session_state:
    st.session_state["Question_1"] = "'lion'"


def quiz(question, answer, options, key):
    user_answer = st.radio(question, options)
    btn = st.button("Submit", key=key)
    if btn:
        if user_answer == answer:
            st.markdown("<p style='color:white;background-color:green;padding:10px;border-radius:20px;'>Correct!</p>",
                        unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:white;background-color:red;padding:10px;border-radius:20px;'>Wrong!</p>",
                        unsafe_allow_html=True)

question_1 = """**What is the output of this code?**\n
animal = 'bear'\n
animal = 'lion'\n
print(animal)"""

answer_1 = "'lion'"
options_1 = ["'bear'", "animal", "'lion'", "error"]

with st.expander("Question 1"):
    quiz(question_1, answer_1, options_1, "Q1")


question_2 = """**What is the output of this code?**\n
name = 'Jack'\n
Name = 'Sara'\n
print(name)"""

answer_2 = "'Jack'"
options_2 = ["'Sara'", "Name", "name", "'Jack'"]

with st.expander("Question 2", expanded=False):
    quiz(question_2, answer_2, options_2, "Q2")

