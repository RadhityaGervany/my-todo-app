import functionWebApp as fwa
import streamlit as st
#fixed it by editing the streamlit-script.py file. changed line 6 from streamlit.cli to streamlit.web.cli

todos = fwa.get_todo()

def add_todo():
    todo = st.session_state["adding_new_todo"].strip()  # Remove leading/trailing spaces
    if todo:
        todos.append(todo + "\n")
        fwa.write_todos(todos)
        st.session_state["adding_new_todo"] = ""  # Clear the input field

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todoo in enumerate(todos):
    checkbox = st.checkbox(todoo, key=todoo)
    if checkbox:
        todos.pop(index)
        fwa.write_todos(todos)
        del st.session_state[todoo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter new todo", on_change=add_todo, key="adding_new_todo")

#pip freeze > requirement.txt
