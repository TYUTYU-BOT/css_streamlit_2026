import streamlit as st
from PIL import Image, UnidentifiedImageError
from pathlib import Path
from typing import Optional
import re

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Asekhona Tyutyuza • Research Profile",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"
AVATAR = ASSETS / "download.png"
BANNER = ASSETS / "download (1).png"
FALLBACK = ASSETS / "download.png"  # optional placeholder PNG

# ---------------------------------------------------------
# Small helpers
# ---------------------------------------------------------
def badge(label, color="#4F46E5"):
    """Return a pill/badge HTML (render with unsafe_allow_html=True)."""
    return f"""
    <span style="background:{color}; padding:4px 10px; border-radius:999px; color:white; font-size:0.85rem; margin-right:6px; display:inline-block;">
        {label}
    </span>
    """

def show_image(path: Path, caption: str = "", use_container_width=True, fallback: Optional[Path] = None):
    """Safely show an image; optionally use a fallback if invalid or missing."""
    if path.exists():
        try:
            with Image.open(path) as img:
                st.image(img, caption=caption, use_container_width=use_container_width)
                return True
        except UnidentifiedImageError:
            st.warning(f"Found '{path.as_posix()}' but it is not a valid image file. Please re-export as PNG.")
        except Exception as e:
            st.error(f"Unexpected error reading {path.name}: {e}")
    else:
        st.info(f"Add an image to {path.as_posix()}")

    if fallback and fallback.exists():
        try:
            with Image.open(fallback) as img:
                st.image(img, caption="(Placeholder)", use_container_width=use_container_width)
        except Exception:
            pass
    return False

def valid_email(email: str) -> bool:
    """Very light email sanity check (not full RFC)."""
    if not email:
        return False
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    show_image(AVATAR, caption="Asekhona Tyutyuza", fallback=FALLBACK)

with col2:
    show_image(BANNER, fallback=None)

    st.markdown("")  # spacer
    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap; line-height:1.6;">
            <div>🎓 Student</div>
            <div>📍 South Africa</div>
            <div>✉️ <a href="mailto:asekhonatyutyuza@gmail.com">asekhonatyutyuza@gmail.com</a></div>
            <div>
                🔗
                <a href="https://github.com/TYUTYU-BOT" target="_blank" rel="noopener noreferrer">GitHub</a>
                ·
                <a href="https://www.linkedin.com/in/asekhona-tyutyuza-7504162b3" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ---------------------------------------------------------
# About
# ---------------------------------------------------------
st.subheader("About")
st.write(
    """
    I'm **Asekhona Tyutyuza**, a student passionate about data, user‑centered design, and building helpful tools.
    This profile showcases my interests, coursework projects, and research directions.
    """
)

# ---------------------------------------------------------
# Research Interests
# ---------------------------------------------------------
st.subheader("Research Interests")
st.markdown(
    badge("Data Visualization")
    + badge("Human–Computer Interaction")
    + badge("Machine Learning", "#06B6D4")
    + badge("Open Science", "#16A34A"),
    unsafe_allow_html=True,
)

st.markdown("---")

# ---------------------------------------------------------
# Highlights
# ---------------------------------------------------------
st.subheader("Highlights")
left, right = st.columns(2)
with left:
    st.markdown("### 📌 Current Focus")
    st.write(
        """
        • Reproducible data science workflows with Streamlit  
        • Storytelling with data and accessible UI patterns  
        • Building small, useful apps for students and researchers
        """
    )
with right:
    st.markdown("### 🧰 Skills")
    st.write(
        """
        • Python (pandas, numpy)  • Visualization (matplotlib, seaborn)  
        • Streamlit  • Git/GitHub  • Technical Writing
        """
    )

st.markdown("---")

# ---------------------------------------------------------
# Featured Projects
# ---------------------------------------------------------
st.subheader("Featured Projects")
proj1, proj2 = st.columns(2, gap="large")

with proj1:
    st.markdown("#### 🏆 MAISH 2025 Hackathon — 1st Place")
    st.write(
        """
        AI‑powered agricultural solution supporting farmers with predictive insights for
        smarter and more sustainable decisions (e.g., disease detection, supply optimization).
        """
    )

    # --- Optional: real links (leave blank to hide) ---
    SUMMARY_URL = ""  # e.g., "https://github.com/TYUTYU-BOT/maish-2025-hackathon#readme"
    REPO_URL    = ""  # e.g., "https://github.com/TYUTYU-BOT/maish-2025-hackathon"
    DEMO_URL    = ""  # e.g., "https://your-app.streamlit.app" or a YouTube demo

    link_cols = st.columns(3)
    if SUMMARY_URL:
        with link_cols[0]:
            st.link_button("Summary", SUMMARY_URL)
    if REPO_URL:
        with link_cols[1]:
            st.link_button("GitHub", REPO_URL)
    if DEMO_URL:
        with link_cols[2]:
            st.link_button("Demo", DEMO_URL)

with proj2:
    st.markdown("#### 🗂️ Planned: Research Paper Organizer")
    st.write("Concept to tag, filter, and export reading lists (CSV/JSON). Useful for literature reviews.")

st.markdown("---")

# ---------------------------------------------------------
# Contact
# ---------------------------------------------------------
st.subheader("Contact")
with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        errors = []
        if len(name.strip()) < 2:
            errors.append("Please enter your full name.")
        if not valid_email(email):
            errors.append("Please provide a valid email address.")
        if len(message.strip()) < 10:
            errors.append("Please enter a brief message (≥ 10 characters).")

        if errors:
            for e in errors:
                st.warning(e)
        else:
            # TODO: Connect to a real endpoint (Formspree, EmailJS, webhook).
            st.success("Thanks! Your message has been recorded.")

