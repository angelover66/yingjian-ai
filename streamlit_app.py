import streamlit as st

st.set_page_config(
    page_title="百胜中国营建 AI赋能",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Force light theme and hide Streamlit UI
st.markdown("""
<style>
    #MainMenu, header, footer, .stDeployButton, [data-testid="stToolbar"],
    [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
    .stApp {background: #FAFAF9 !important;}
    .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
    .stMainBlockContainer {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
    .st-emotion-cache-13ln4jf {padding: 0 !important; max-width: 100% !important;}
</style>
""", unsafe_allow_html=True)

# Read and display HTML
with open("index.html", "r") as f:
    html = f.read()

# Make HTML background explicit to prevent dark mode bleed
html = html.replace("var(--bg)", "#FAFAF9")
html = html.replace("var(--surface)", "#FFFFFF")
html = html.replace("var(--text)", "#1A1A1A")
html = html.replace("var(--text-secondary)", "#5A5A5A")
html = html.replace("var(--text-muted)", "#8A8A8A")
html = html.replace("var(--border)", "#E8E5E0")
html = html.replace("var(--red)", "#E4002B")
html = html.replace("var(--red-dark)", "#B8001F")
html = html.replace("var(--gold)", "#C8963E")

st.components.v1.html(html, height=20000, scrolling=True)
