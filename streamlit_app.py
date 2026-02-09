import streamlit as st
from PIL import Image, UnidentifiedImageError
from pathlib import Path
from typing import Optional
import re

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Asekhona Tyutyuza | Research & Portfolio",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# GLOBAL STYLING (FONTS + THEME + CARDS)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Headings */
h1 { font-size: 3rem; font-weight: 700; }
h2 { font-size: 2rem; margin-top: 2.5rem; }
h3 { font-size: 1.4rem; }

/* Cards */
.card {
    background-color: #020617;
    padding: 1.6rem;
    border-radius: 14px;
    border: 1px solid #1E293B;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 30px rgba(56,189,248,0.15);
}

/* Sections */
.section {
    margin-top: 3rem;
    margin-bottom: 3rem;
}

/* Links */
a {
    color: #38BDF8;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# PATHS
# =========================================================
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

AVATAR = ASSETS / "download (1).png"
BANNER = ASSETS / "asekhona.png"
FALLBACK = ASSETS / "download.png"

# =========================================================
# HELPERS
# =========================================================
def badge(label, color="#38BDF8"):
    return f"""
    <span style="
        background:{color};
        padding:6px 12px;
        border-radius:999px;
        color:white;
        font-size:0.85rem;
        margin-right:8px;
        display:inline-block;">
        {label}
    </span>
    """

def show_image(
    path: Path,
    caption: str = "",
    use_container_width=True,
    fallback: Optional[Path] = None,
):
    if path.exists():
        try:
            with Image.open(path) as img:
                st.image(img, caption=caption, use_container_width=use_container_width)
                return True
        except UnidentifiedImageError:
            st.warning(f"{path.name} is not a valid image file.")
    elif fallback and fallback.exists():
        st.image(Image.open(fallback), caption="Placeholder", use_container_width=use_container_width)
    return False

def valid_email(email: str) -> bool:
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email or "") is not None

# =========================================================
# HERO / HEADER
# =========================================================
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    show_image(AVATAR, caption="Asekhona Tyutyuza", fallback=FALLBACK)

with col2:
    show_image(BANNER)

    st.markdown("""
    <div class="section">
        <h1>Asekhona Tyutyuza</h1>
        <p style="font-size:1.3rem;">
            Aspiring <strong>Data Scientist</strong> &amp;
            <strong>Machine Learning Engineer</strong>
        </p>

        <p>📍 South Africa</p>

        <p>
            ✉️ <strong>Email:</strong> asekhonatyutyuza@gmail.com<br>
            🔗 <a href="https://github.com/TYUTYU-BOT" target="_blank">GitHub</a><br>
            🔗 <a href="https://www.linkedin.com/in/asekhona-tyutyuza-7504162b3" target="_blank">LinkedIn</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# ABOUT
# =========================================================
st.subheader("About")

st.markdown("""
I am an aspiring data scientist with a strong interest in **machine learning,
data visualization, and applied analytics**. My work focuses on building
data-driven tools that transform raw data into clear, actionable insights.

I am particularly interested in **reproducible workflows**, **interactive
analytical applications**, and applying data science techniques to real-world
challenges in research and industry.
""")

# =========================================================
# RESEARCH INTERESTS
# =========================================================
st.subheader("Research Interests")

st.markdown(
    badge("Data Science & Analytics")
    + badge("Machine Learning", "#06B6D4")
    + badge("Data Visualization")
    + badge("Reproducible Research", "#16A34A"),
    unsafe_allow_html=True,
)

st.markdown("---")

# =========================================================
# HIGHLIGHTS
# =========================================================
st.subheader("Highlights")

c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown("""
    <div class="card">
        <h3>🎯 Current Focus</h3>
        <ul>
            <li>Data analysis & exploratory workflows in Python</li>
            <li>Interactive dashboards with Streamlit</li>
            <li>Applied machine learning concepts</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h3>🛠 Technical Skills</h3>
        <ul>
            <li><strong>Python:</strong> pandas, numpy</li>
            <li><strong>Visualization:</strong> matplotlib, seaborn</li>
            <li><strong>Tools:</strong> Streamlit, Git, GitHub</li>
            <li>Technical writing & rapid prototyping</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# EXPERIENCE & TRAINING
# =========================================================
st.subheader("Experience & Training")

st.markdown("""
<div class="card">
<strong>CHPC & NITheCS Coding Summer School — Data Science & Machine Learning</strong><br>
<em>January 2026 – February 2026</em>

<ul>
    <li>Scientific computing and data science foundations</li>
    <li>Python-based ETL pipelines and exploratory analysis</li>
    <li>Core concepts in machine learning, AI, probability, and statistics</li>
    <li>Strong emphasis on reproducible research workflows</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# FEATURED PROJECTS
# =========================================================
st.subheader("Featured Projects")

p1, p2 = st.columns(2, gap="large")

with p1:
    st.markdown("""
    <div class="card">
        <h3>🏆 MAISH 2025 Hackathon — 1st Place</h3>
        <p><strong>Problem:</strong> Limited access to timely, data-driven insights for farmers</p>
        <p><strong>Solution:</strong> AI-powered agricultural decision-support system</p>
        <p><strong>Outcome:</strong> 🥇 First place in a national hackathon</p>
        <ul>
            <li>Machine learning for predictive insights</li>
            <li>Rapid data pipeline development</li>
            <li>Collaborative problem-solving under pressure</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="card">
        <h3>📚 Planned Project — Research Paper Organizer</h3>
        <p>
        A lightweight tool to manage literature reviews by storing metadata,
        tagging papers, filtering results, and exporting structured reading lists
        to CSV or JSON formats.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# CONTACT
# =========================================================
st.subheader("Contact")

with st.form("contact_form"):

