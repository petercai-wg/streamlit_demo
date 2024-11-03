import streamlit as st


def reset_counter():
    st.session_state.counter = 0


def add_counter():
    st.session_state.counter += 1
    st.rerun()


if "counter" not in st.session_state:
    st.session_state.counter = 0


st.header(f"This page has run {st.session_state.counter} times.")

col1, col2 = st.columns(2)

with col1:
    if st.button("Run it"):
        add_counter()


with col2:
    st.button("Reset", on_click=reset_counter)
