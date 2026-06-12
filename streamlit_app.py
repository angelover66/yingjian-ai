import streamlit as st

st.set_page_config(
    page_title="百胜中国营建 AI赋能",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Nuke Streamlit padding completely
st.markdown("""
<style>
    .stApp {background: #FAFAF9;}
    .stMainBlockContainer, .block-container, .st-emotion-cache-13ln4jf {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;
    }
    section.main > div {padding: 0 !important;}
    .stApp > header, .stApp > div:first-child {display: none !important;}
    #MainMenu, header, footer, .stDeployButton,
    [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"], #GithubIcon {display: none !important;}
</style>
""", unsafe_allow_html=True)

# Read HTML
with open("index.html", "r") as f:
    html = f.read()

# Patch CSS variables to fixed hex so they render in iframe
html = html.replace("var(--red)", "#E4002B")
html = html.replace("var(--red-dark)", "#B8001F")
html = html.replace("var(--red-light)", "#FF1A45")
html = html.replace("var(--gold)", "#C8963E")
html = html.replace("var(--gold-light)", "#E8C97A")
html = html.replace("var(--bg)", "#FAFAF9")
html = html.replace("var(--surface)", "#FFFFFF")
html = html.replace("var(--text)", "#1A1A1A")
html = html.replace("var(--text-secondary)", "#5A5A5A")
html = html.replace("var(--text-muted)", "#8A8A8A")
html = html.replace("var(--border)", "#E8E5E0")

# Remove the navy background from the hero section if any
html = html.replace('background: rgba(250,250,249,0.85)', 'background: rgba(250,250,249,0.95)')

# Set height to show full content. The page is ~8000px of vertical content.
st.components.v1.html(html, height=8000, scrolling=True)
