import streamlit as st
from streamlit_tags import st_tags

st.title("test")
labels_from_st_tags = st_tags(value=["사회/경제", "안전", "교통"],maxtags=3,label="")
