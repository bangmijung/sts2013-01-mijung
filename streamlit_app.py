import streamlit as st
from streamlit_tags import st_tags
st.title("test")
st_tags(
            value=["test","Test2"],
            maxtags=3,
            label=""
        )