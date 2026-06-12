import streamlit as st
import re

st.set_page_config(
    page_title="百胜中国营建 AI赋能",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Read HTML
with open("index.html", "r") as f:
    html = f.read()

# Extract CSS and replace CSS variables with fixed hex
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css = css_match.group(1) if css_match else ""
for var, val in [("var(--red)", "#E4002B"), ("var(--red-dark)", "#B8001F"), ("var(--red-light)", "#FF1A45"),
    ("var(--gold)", "#C8963E"), ("var(--gold-light)", "#E8C97A"), ("var(--bg)", "#FAFAF9"),
    ("var(--surface)", "#FFFFFF"), ("var(--text)", "#1A1A1A"), ("var(--text-secondary)", "#5A5A5A"),
    ("var(--text-muted)", "#8A8A8A"), ("var(--border)", "#E8E5E0"), ("var(--shadow-sm)", "0 1px 3px rgba(0,0,0,0.04)"),
    ("var(--shadow-md)", "0 4px 24px rgba(0,0,0,0.06)"), ("var(--shadow-lg)", "0 12px 48px rgba(0,0,0,0.10)"),
    ("var(--shadow-red)", "0 8px 32px rgba(228,0,43,0.15)"), ("var(--radius)", "16px"),
    ("var(--radius-sm)", "10px"), ("var(--transition)", "0.3s cubic-bezier(0.4, 0, 0.2, 1)")]:
    css = css.replace(var, val)

# Extract body content (everything between <body> and </body>)
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
body = body_match.group(1) if body_match else ""

# Extract script
script_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
script = script_match.group(1) if script_match else ""

# Remove nav scroll logic (conflicts with streamlit)
script = re.sub(r'// Scroll spy.*?(?=// Reveal on scroll)', '', script, flags=re.DOTALL)
# Fix scroll spy to work in streamlit context
script = script.replace("window.addEventListener('scroll'", "document.getElementById('app-root').addEventListener('scroll'")

# Inject everything directly - no iframe, no fixed height
st.markdown(f"""
<style>
/* Streamlit reset */
.stApp {{background: #FAFAF9 !important; padding: 0 !important; margin: 0 !important;}}
.stMainBlockContainer {{padding: 0 !important; margin: 0 !important; max-width: 100% !important;}}
.block-container {{padding: 0 !important; margin: 0 !important; max-width: 100% !important;}}
.st-emotion-cache-13ln4jf {{padding: 0 !important; max-width: 100% !important;}}
section.main > div {{padding: 0 !important;}}
#MainMenu, header, footer, .stDeployButton, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {{display: none !important;}}

/* Fix body for streamlit context */
body {{overflow-x: hidden;}}
#app-root {{height: 100vh; overflow-y: auto;}}

{css}
</style>

<div id="app-root">
{body}
</div>

<script>
(function() {{
    var appRoot = document.getElementById('app-root');
    if (!appRoot) return;

    // Nav background on scroll
    var nav = document.getElementById('nav');
    var backTop = document.getElementById('backTop');
    var sections = document.querySelectorAll('section[id]');
    var navLinks = document.querySelectorAll('.nav-links a');

    if (nav && appRoot) {{
        appRoot.addEventListener('scroll', function() {{
            var y = appRoot.scrollTop;
            if (nav) nav.classList.toggle('scrolled', y > 50);
            if (backTop) backTop.classList.toggle('visible', y > 600);

            var current = '';
            sections.forEach(function(s) {{
                if (y >= s.offsetTop - 100) current = s.id;
            }});
            navLinks.forEach(function(a) {{
                a.classList.toggle('active', a.getAttribute('href') === '#' + current);
            }});
        }});
    }}

    if (backTop && appRoot) {{
        backTop.addEventListener('click', function() {{
            appRoot.scrollTo({{top: 0, behavior: 'smooth'}});
        }});
    }}

    // Reveal animations
    var observer = new IntersectionObserver(function(entries) {{
        entries.forEach(function(e) {{ if (e.isIntersecting) e.target.classList.add('visible'); }});
    }}, {{threshold: 0.15, rootMargin: '0px 0px -40px 0px'}});

    document.querySelectorAll('.reveal').forEach(function(el) {{ observer.observe(el); }});

    // Table row hover
    document.querySelectorAll('tbody tr').forEach(function(row) {{
        row.addEventListener('mouseenter', function() {{ row.style.background = 'rgba(228,0,43,0.04)'; }});
        row.addEventListener('mouseleave', function() {{ row.style.background = ''; }});
    }});
}})();
</script>
""", unsafe_allow_html=True)
