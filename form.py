import streamlit as st
import datetime

st.title("User Information form")

with st.form(key="user_info_form"):
    name = st.text_input("Enter your name:")
    age = st.number_input(
        "Enter your age:",
    )
    gender = st.selectbox("Gender", ["Male", "Female", "X"])
    dob = st.date_input(
        "Enter your birth date",
        max_value=datetime.datetime.now(),
        min_value=datetime.datetime(2000, 1, 1),
    )

    submit = st.form_submit_button(label="Submit")
    if submit:
        st.text_area(f"you entered {name}, {age}, {gender}, {dob}")
