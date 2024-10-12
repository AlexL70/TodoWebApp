import streamlit as st
import modules.functions as fn

class ControlKeys:
    TODO_INPUT: str = "__todo_input__"
    EDIT_BTN: str = "__edit_button__"
    COMPLETE_BTN: str = "__complete__button"
    TODO_ITEM: str = "__todo__item__"
    EDIT_INDEX: str = "__edit__index__"


todos = fn.get_todos()

try:
    edit_index = st.session_state[ControlKeys.EDIT_INDEX]
except KeyError:
    edit_index = None

def add_or_edit_todo():
    item = st.session_state[ControlKeys.TODO_INPUT]
    if item is None or len(item) == 0:
        return
    if edit_index is None:
        todos.append(item)
    else:
        todos[edit_index] = item
        st.session_state[ControlKeys.EDIT_INDEX] = None
    fn.write_todos(todos)
    st.session_state[ControlKeys.TODO_INPUT] = None

def complete_todo():
    for i, item in enumerate(todos):
        completed = st.session_state[f"{ControlKeys.COMPLETE_BTN}{i}"]
        if completed:
            todos.pop(i)
            fn.write_todos(todos)
            break

def edit_mode():
    for i, item in enumerate(todos):
        edited = st.session_state[f"{ControlKeys.EDIT_BTN}{i}"]
        if edited and edit_index is None:
            # Enter edit mode if "Edit" is clicked
            st.session_state[ControlKeys.EDIT_INDEX] = i
            st.session_state[ControlKeys.TODO_INPUT] = item
            break


st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("This app is to increase you productivity.")

col1, col2 = st.columns((4,1))

for index, todo in enumerate(todos):
    row = st.columns((4,1,1))
    disable_buttons = not edit_index is None
    with st.container():
        with row[0]:
            todo_str = f"{index + 1} – {todo}"
            if edit_index == index:
                st.write(f"{todo_str} :red[{'(edited)'}]")
            else:
                st.write(todo_str)
        with row[1]:
            st.button("Edit", key=f"{ControlKeys.EDIT_BTN}{index}", use_container_width=True, on_click=edit_mode, disabled=disable_buttons)
        with row[2]:
            st.button("Complete", key=f"{ControlKeys.COMPLETE_BTN}{index}", use_container_width=True, on_click=complete_todo, disabled=disable_buttons)

if edit_index is None:
    inp_lbl_text = "Enter a todo to be added:"
else:
    inp_lbl_text = f"Editing item #{edit_index + 1}"
st.text_input(label=inp_lbl_text, placeholder="New todo", on_change=add_or_edit_todo, key=ControlKeys.TODO_INPUT)