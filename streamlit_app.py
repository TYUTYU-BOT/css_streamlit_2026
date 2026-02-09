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
# PATHS & CONSTANTS
# =========================================================
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

AVATAR   = ASSETS / "download (1).png"
BANNER   = ASSETS / "asekhona.png"
FALLBACK = ASSETS / "download.png"

# =========================================================
# HELPERS
# =========================================================
def badge(label, color="#4F46E5"):
    return f"""
    <span style="
        background:{color};
        padding:4px 10px;
        border-radius:999px;
        color:white;
        font-size:0.85rem;
        margin-right:6px;
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
        except Exception as e:
            st.error(f"Error loading {path.name}: {e}")
    else:
        st.info(f"Missing image: {path.as_posix()}")

    if fallback and fallback.exists():
        try:
            with Image.open(fallback) as img:
                st.image(img, caption="Placeholder", use_container_width=use_container_width)
        except Exception:
            pass
    return False

def valid_email(email: str) -> bool:
    if not email:
        return False
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None

# =========================================================
# HEADER
# =========================================================
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    show_image(AVATAR, caption="Asekhona Tyutyuza", fallback=FALLBACK)

with col2:
    show_image(BANNER)

    st.markdown(
    """
    <h1 style="margin-bottom:0;">Asekhona Tyutyuza</h1>
    <h3 style="margin-top:4px; color:#9CA3AF;">
        Aspiring Data Scientist & Machine Learning Engineer
    </h3>

    <div style="display:flex; gap:14px; flex-wrap:wrap; margin-top:12px;">
        <div>📍 South Africa</div>
        <div>
            ✉️ <a href="mailto:asekhonatyutyuza@gmail.com">asekhonatyutyuza@gmail.com</a>
        </div>
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

    )

st.markdown("---")

# =========================================================
# ABOUT
# =========================================================
st.subheader("About")

st.markdown(
    """
    I am an aspiring data scientist with a strong interest in **machine learning,
    data visualization, and applied analytics**. My work focuses on building
    data-driven tools that transform raw data into clear, actionable insights.

    I am particularly interested in **reproducible workflows**, **interactive
    analytical applications**, and applying data science techniques to real-world
    challenges in research and industry.
    """
)

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

left, right = st.columns(2)

with left:
    st.markdown("### Current Focus")
    st.markdown(
        """
        - Data analysis and exploratory workflows in Python  
        - Building interactive dashboards with Streamlit  
        - Applying machine learning concepts to practical problems
        """
    )

with right:
    st.markdown("### Technical Skills")
    st.markdown(
        """
        - **Python:** pandas, numpy  
        - **Visualization:** matplotlib, seaborn  
        - **Tools:** Streamlit, Git, GitHub  
        - **Other:** Technical writing, rapid prototyping
        """
    )

st.markdown("---")

# =========================================================
# EXPERIENCE & TRAINING
# =========================================================
st.subheader("Experience & Training")

st.markdown(
    """
    **CHPC & NITheCS Coding Summer School — Data Science & Machine Learning**  
    *January 2026 – February 2026*

    - Intensive training in scientific computing and data science  
    - Python-based ETL pipelines, exploratory data analysis, and visualization  
    - Core concepts in machine learning, AI, probability, and statistics  
    - Emphasis on reproducible research workflows and computational thinking
    """
)

st.markdown("---")

# =========================================================
# FEATURED PROJECTS
# =========================================================
st.subheader("Featured Projects")

p1, p2 = st.columns(2, gap="large")

with p1:
    st.markdown("### 🏆 MAISH 2025 Hackathon — 1st Place")
    st.markdown(
        """
        **Problem:** Limited access to timely, data-driven insights for farmers  
        **Solution:** AI-powered agricultural decision-support system  
        **Outcome:** 🥇 First place in a 3-day national hackathon
        """
    )

    st.markdown(
        """
        - Applied machine learning concepts for predictive insights  
        - Built data analysis pipelines under tight time constraints  
        - Collaborated in a multidisciplinary team environment
        """
    )

with p2:
    st.markdown("### 📚 Planned Project — Research Paper Organizer")
    st.markdown(
        """
        A lightweight tool to manage literature reviews by storing metadata,
        tagging papers, filtering results, and exporting reading lists
        to CSV or JSON formats.
        """
    )

st.markdown("---")

# =========================================================
# CONTACT
# =========================================================
st.subheader("Contact")

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Email address")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send message")

    if submitted:
        errors = []

        if len(name.strip()) < 2:
            errors.append("Please enter your full name.")
        if not valid_email(email):
            errors.append("Please provide a valid email address.")
        if len(message.strip()) < 10:
            errors.append("Message must be at least 10 characters.")

        if errors:
            for e in errors:
                st.warning(e)
        else:
            st.success("Thank you — your message has been received.")

st.markdown("---")
st.caption("© 2026 Asekhona Tyutyuza · Data Science & Machine Learning Portfolio")
