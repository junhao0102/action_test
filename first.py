"""first.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

new_word = st.text_input("Magic word:")

if st.button("Set the magic word"):
    st.session_state.magic_word = new_word