import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_tags import st_tags
st.title("test")
options = st.multiselect(
    label = 'What are your favorite colors',
    options = ['Green', 'Yellow', 'Red', 'Blue'],
    default = ['Yellow', 'Red'])
labels_from_st_tags = st_tags(
            value=["사회/경제", "안전", "교통"],
            maxtags=3,
            label=""
        )
