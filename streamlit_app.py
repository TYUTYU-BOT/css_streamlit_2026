import streamlit as st
from PIL import Image, UnidentifiedImageError
from pathlib import Path

st.set_page_config(
    page_title="Asekhona Tyutyuza • Research Profile",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Helper ----------
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

def badge(label, color="#4F46E5"):
    return f"""
    <span style='background:{color}; padding:4px 10px; border-radius:999px; color:white; font-size:0.85rem; margin-right:6px;'>
        {label}
    </span>
    """

# ---------- Header ----------
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    avatar_path = ASSETS / "avatar.png"
    if avatar_path.exists():
        try:
            avatar = Image.open(avatar_path)
            st.image(avatar, caption="Asekhona Tyutyuza", use_container_width=True)
        except UnidentifiedImageError:
            st.warning("Couldn't read assets/avatar.png. Please upload a valid PNG image.")
    else:
        st.info("Add an avatar image to assets/avatar.png")

with col2:
    banner_path = ASSETS / "banner.png"
    if banner_path.exists():
        try:
            st.image(str(banner_path), use_container_width=True)
        except UnidentifiedImageError:
            st.warning("Couldn't read assets/banner.png. Please upload a valid PNG image.")
    else:
        st.info("Add a banner image to assets/banner.png")

    st.markdown("")  # spacer
    st.markdown(
        """
        <div style='display:flex; align-items:center; gap:12px; flex-wrap:wrap;'>
            <div>🎓 Student</div>
            <div>📍 South Africa</div>
            <div>✉️ <a href='mailto:asekhonatyutyuza@gmail.com'>asekhonatyutyuza@gmail.com</a></div>
            <div>🔗 
                <a href="https://github.com/TYUTYU-BOT" target="_blank" rel="noopener noreferrer">GitHub</a> ·
                <a href="https://www.linkedin.com/in/asekhona-tyutyuza-7504162b3" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ---------- About ----------
st.subheader("About")
st.write(
    """
    I'm **Asekhona Tyutyuza**, a student passionate about data, user-centered design, and building helpful tools.
    This profile showcases my interests, coursework projects, and any research I've been exploring. Replace the placeholders
    below with your real content to make it truly yours.
    """
)

# ---------- Research Interests ----------
st.subheader("Research Interests")
st.markdown(
    badge("Data Visualization")
    + badge("Human–Computer Interaction")
    + badge("Machine Learning", "#06B6D4")
    + badge("Open Science", "#16A34A"),
    unsafe_allow_html=True,
)

# ---------- Highlights ----------
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

        • Streamlit   • Git/GitHub   • Technical Writing
        """
    )

st.markdown("---")

# ---------- Featured Projects ----------
st.subheader("Featured Projects")
proj1, proj2 = st.columns(2, gap="large")
with proj1:
    st.markdown("#### 📊 Coursework Notebook to App")
    st.write("Turn a Jupyter notebook into an interactive web app with Streamlit, enabling parameter tweaks and live charts.")
    if st.button("View demo code", key="p1"):
        st.code(
            """
import streamlit as st
st.title('Hello Streamlit')
st.slider('Try me', 0, 10, 5)
            """,
            language='python',
        )
with proj2:
    st.markdown("#### 🗂️ Research Paper Organizer")
    st.write("A simple tool to tag, filter, and export reading lists (CSV/JSON). Great for literature reviews.")

st.markdown("---")

# ---------- Publications (Examples) ----------
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

# ---------- Contact ----------
st.subheader("Contact")
with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks! This is a demo form—replace with a real endpoint (e.g., Formspree).")

st.caption("Built with ❤️ using Streamlit. Customize this page in `streamlit_app.py`.")
