import streamlit as st
from streamlit.hello.utils import show_code

st.title("test")
options = st.multiselect(
    label = 'What are your favorite colors',
    options = ['Green', 'Yellow', 'Red', 'Blue'],
    default = ['Yellow', 'Red'])
