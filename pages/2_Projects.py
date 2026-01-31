import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Projects | Asekhona Tyutyuza",
    page_icon="🧪",
    layout="centered",
)

# Page title
st.title("🧪 Projects")

# Introduction
st.markdown(
    """
    This page highlights a selection of **academic and personal projects** and **concepts** I’m exploring.
    These reflect my interests in **data analysis**, **visualization**, and building **interactive applications**
    with Python and Streamlit.

    Each project focuses on practical problem-solving and applying concepts learned through coursework
    and independent exploration.
    """
)

st.markdown("---")

# =========================================================
# FEATURED / HACKATHON PROJECT 
# =========================================================
st.subheader("🏆 Featured: MAISH 2025 Hackathon — 1st Place")

st.markdown(
    """
    **Project:** AI‑powered agricultural solution  
    **Outcome:** 🥇 First Place (3‑day hackathon)  
    **Focus:** Predictive insights for smarter, more sustainable farming
    """
)

with st.expander("What we built (overview)"):
    st.markdown(
        """
        Built an AI‑driven tool to support farmers with:
        - **Crop & livestock disease detection**
        - **Supply optimization**
        - **Data‑informed decision support**

        **Skills & Tools:** Rapid prototyping, teamwork under time constraints, Python, AI/ML concepts, data analysis.

        **Team:** Asekhona Tyutyuza, Brightness Mapule Masilela
        """
    )

# Optional action buttons (replace st.info with links when ready)
cols = st.columns(3)
with cols[0]:
    if st.button("View summary", key="maish_summary"):
        st.info("Add a link to a write‑up or README when available.")
with cols[1]:
    if st.button("GitHub repo", key="maish_repo"):
        st.info("Add a GitHub URL to the project repository when ready.")
with cols[2]:
    if st.button("Demo (if hosted)", key="maish_demo"):
        st.info("Add a demo link if you deploy a prototype.")

st.markdown("---")

# =========================================================
# CONCEPT / PLANNED PROJECTS (NOT YET BUILT)
# =========================================================
st.subheader("🧩 Concept & Planned Projects")
st.caption("These are project ideas and learning exercises I understand and plan to implement.")

# ---------- Concept Project 1 ----------
st.markdown("### 📊 Concept Project: Student Performance Dashboard")
st.markdown(
    """
    **Overview:**  
    A conceptual Streamlit dashboard to explore student performance data using filters and visualizations.

    **What it would include:**
    - Interactive filters (subject, grade range, time period)
    - Bar/line charts for trends and distribution
    - Summary metrics (average score, pass rate)

    **Tools & Skills (planned):** Python, pandas, Streamlit, data visualization
    """
)

# Optional buttons (placeholders)
c1, c2 = st.columns(2)
with c1:
    if st.button("Planned repo", key="concept_perf_repo"):
        st.info("Add a GitHub link once you start this project.")
with c2:
    if st.button("Design notes", key="concept_perf_notes"):
        st.info("Link a Notion/Docs page with your design notes when available.")

st.markdown("---")

# ---------- Planned Project 2 ----------
st.markdown("### 📂 Planned Project: Research Paper Organizer")
st.markdown(
    """
    **Overview:**  
    A simple tool to manage literature review items (title, authors, year, tags, notes) with search/filter and export.

    **What it would include:**
    - Add/edit entries via a form
    - Tagging and quick search
    - Export reading list to CSV/JSON

    **Tools & Skills (planned):** Python, Streamlit, basic data storage (CSV/SQLite)
    """
)

# Optional buttons (placeholders)
c3, c4 = st.columns(2)
with c3:
    if st.button("Planned repo", key="concept_rpo_repo"):
        st.info("Add the GitHub link once you begin implementation.")
with c4:
    if st.button("Feature backlog", key="concept_rpo_backlog"):
        st.info("Link a backlog/todo list when ready.")
        
st.markdown("---")

# =========================================================
# FUTURE PROJECTS
# =========================================================
st.subheader("➕ More Projects Coming Soon")
st.markdown(
    """
    This section will be updated as I continue working on new coursework,
    experiments, and personal projects.
    """
)

st.caption("Projects are continuously updated as part of my learning journey.")

