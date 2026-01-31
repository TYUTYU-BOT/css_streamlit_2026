import streamlit as st
from PIL import Image, UnidentifiedImageError
from pathlib import Path
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
AVATAR = ASSETS / "avatar.png"
BANNER = ASSETS / "banner.png"
FALLBACK = ASSETS / "download.png"  # any valid PNG you already have

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

def show_image(path: Path, caption: str = "", use_container_width=True, fallback: Path | None = None):
    """Safely show an image; optionally use a fallback if invalid or missing."""
    if path.exists():
        try:
            with Image.open(path) as img:
                st.image(img, caption=caption, use_container_width=use_container_width)
                return True
        except UnidentifiedImageError:
            st.warning(f"Found '{path.as_posix()}' but it is not a valid PNG.")
        except Exception as e:
            st.error(f"Unexpected error reading {path.name}: {e}")
    else:
        st.info(f"Add an image to {path.as_posix()}")

    # fallback path
    if fallback and fallback.exists():
        with Image.open(fallback) as img:
            st.image(img, caption="(Placeholder)", use_container_width=use_container_width)
        return False
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
    This profile showcases my interests, coursework projects, and any research I've been exploring.
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
        • Exploring reproducible data science workflows with Streamlit.  
        • Learning effective storytelling with data and accessible UI patterns.  
        • Building small, useful apps for students and researchers.
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
# Featured Projects (example placeholders)
# ---------------------------------------------------------
st.subheader("Featured Projects")
proj1, proj2 = st.columns(2, gap="large")

with proj1:
    st.markdown("#### 🏆 MAISH 2025 Hackathon — 1st Place")
    st.write(
        """
        Built an AI‑powered agricultural solution that supports farmers with predictive insights
        for smarter and more sustainable decisions (e.g., disease detection, supply optimization).
        """
    )
    a, b, c = st.columns(3)
    with a:
        st.link_button("Summary", "https://github.com/TYUTYU-BOT")  # replace with your write‑up URL
    with b:
        st.link_button("GitHub", "https://github.com/TYUTYU-BOT")   # replace with repo URL
    with c:
        st.link_button("Demo", "https://your-demo-url.example")     # replace with live demo URL or video

with proj2:
    st.markdown("#### 🗂️ Planned: Research Paper Organizer")
    st.write(
        "Concept to tag, filter, and export reading lists (CSV/JSON). Useful for literature reviews."
    )

st.markdown("---")

# ---------------------------------------------------------
# Publications (Examples)
# ---------------------------------------------------------
st.subheader("Publications (Examples)")
with st.expander("Example: Structured Abstract"):
    st.markdown(
        """
**Title:** Learning with Interactive Dashboards  
**Authors:** Your Name, Collaborator  
**Year:** 2025  
**Abstract:** This placeholder demonstrates how you can summarize a paper—problem, method, results, and implications.
        """
    )

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
            # This is a demo: replace with an integration (e.g., Formspree, EmailJS, webhook)
            st.success("Thanks! This is a demo form — connect a real endpoint to receive messages.")

st.caption("Built with ❤️ using Streamlit. Customize this page in `streamlit_app.py`.")

# ---------------------------------------------------------
# Optional: quick diagnostics (expand if you need to debug images)
# ---------------------------------------------------------
with st.expander("Debug (images)"):
    st.write(
        {
            "BASE_DIR": str(BASE_DIR),
            "ASSETS": str(ASSETS),
            "avatar_exists": AVATAR.exists(),
            "banner_exists": BANNER.exists(),
            "fallback_exists": FALLBACK.exists(),
        }
    )
