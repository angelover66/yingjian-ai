import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="百胜中国营建 AI赋能",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

st.markdown("""
<style>
    .stApp {background: #FAFAF9;}
    .stMainBlockContainer, .block-container {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;
    }
    #MainMenu, header, footer, .stDeployButton,
    [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

with open(Path(__file__).parent / "index_streamlit.html", "r") as f:
    html = f.read()

st.components.v1.html(html, height=7500, scrolling=True)
