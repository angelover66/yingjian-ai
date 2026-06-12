import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="百胜中国营建 AI赋能",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Kill every bit of Streamlit spacing
st.markdown("""
<style>
    html, body, #root, .stApp, .main, .st-emotion-cache-0 {
        margin: 0 !important; padding: 0 !important;
    }
    .stApp {background: #FAFAF9 !important; overflow: hidden;}
    .stMainBlockContainer, .block-container, [data-testid="stVerticalBlock"] {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;
        gap: 0 !important;
    }
    .stMainBlockContainer > div {padding: 0 !important; margin: 0 !important;}
    section.main > div {padding: 0 !important;}
    .stIFrame {display: block !important; margin: 0 !important; padding: 0 !important;}
    #MainMenu, header, footer, .stDeployButton,
    [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

with open(Path(__file__).parent / "index_streamlit.html", "r") as f:
    html = f.read()

st.components.v1.html(html, height=7800, scrolling=True)
