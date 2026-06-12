import streamlit as st
import os

st.set_page_config(
    page_title="百胜中国营建系统 AI赋能机会研究",
    page_icon="🏗️",
    layout="wide"
)

# Hide Streamlit UI
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {margin: 0; padding: 0;}
</style>
""", unsafe_allow_html=True)

# Read and display HTML
html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=10000, scrolling=True)
