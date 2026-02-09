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
# GLOBAL STYLING
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

h1 { font-size: 3rem; font-weight: 700; }
h2 { font-size: 2rem; margin-top: 2.5rem; }
h3 { font-size: 1.4rem; }

.card {
    padding: 1.6rem;
    border-radius: 14px;
    border: 1px solid #1E293B;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 30px rgba(56,189,248,0.15);
}

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
# HERO SECTION
# =========================================================
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    show_image(AVATAR, caption="Asekhona Tyutyuza", fallback=FALLBACK)

with col2:
    show_image(BANNER)

    st.markdown("""
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
            <li>Exploratory data analysis in Python</li>
            <li>Interactive dashboards with Streamlit</li>
            <li>Applied machine learning problems</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h3>🛠 Technical Skills</h3>
        <ul>
            <li>Python (pandas, numpy)</li>
            <li>matplotlib, seaborn</li>
            <li>Streamlit, Git, GitHub</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# CONTACT
# =========================================================
st.subheader("Contact")

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Email address")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send message 🚀")

    if submitted:
        if len(name.strip()) < 2:
            st.warning("Please enter your full name.")
        elif not valid_email(email):
            st.warning("Please provide a valid email address.")
        elif len(message.strip()) < 10:
            st.warning("Message must be at least 10 characters.")
        else:
            st.success("Thank you — your message has been received.")

st.markdown("---")
st.caption("© 2026 Asekhona Tyutyuza · Data Science & Machine Learning Portfolio")
