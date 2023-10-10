import streamlit as st

st.title("test")
options = st.multiselect(
    label = 'What are your favorite colors',
    options = ['Green', 'Yellow', 'Red', 'Blue'],
    default = ['Yellow', 'Red'])
