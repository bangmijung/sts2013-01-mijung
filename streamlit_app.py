import streamlit as st
from streamlit_tags import st_tags

st.title("test")
st.multiselect( "Choose countries", ["1","2"], ["China", "United States of America"])
