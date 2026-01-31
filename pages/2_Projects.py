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
    This page highlights a selection of **academic and personal projects** I have worked on.
    These projects reflect my interests in **data analysis**, **visualization**, and
    building **interactive applications** with Python and Streamlit.

    Each project focuses on practical problem-solving and applying concepts learned
    through coursework and independent exploration.
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

# Optional buttons (add your links if available)
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
# PROJECT 1
# =========================================================
st.subheader("📊 Student Performance Dashboard")

st.markdown(
    """
    **Description:**  
    An interactive dashboard built with **Streamlit** to explore and visualize student
    performance data. The application allows users to filter data dynamically and
    gain insights through clear, informative charts.

    **Key Features:**
    - Interactive filters for exploring subsets of data  
    - Visual summaries using charts and metrics  
    - User‑friendly layout for non‑technical users  

    **Tools & Skills:** Python, Streamlit, Data Visualization
    """
)

# Optional CTA buttons (plug in links later)
c1, c2 = st.columns(2)
with c1:
    if st.button("Open repo", key="p1_repo"):
        st.info("Add the GitHub link here.")
with c2:
    if st.button("Live demo", key="p1_demo"):
        st.info("Add the Streamlit Cloud link here.")

st.markdown("---")

# =========================================================
# PROJECT 2
# =========================================================
st.subheader("📂 Research Paper Organizer")

st.markdown(
    """
    **Description:**  
    A lightweight tool designed to help students and researchers organize academic
    papers efficiently. The app supports tagging, filtering, and exporting reading lists,
    making it useful for literature reviews and research planning.

    **Key Features:**
    - Tagging and categorization of papers  
    - Simple search and filtering  
    - Export functionality (e.g., CSV or JSON)  

    **Tools & Skills:** Python, Streamlit, Data Management
    """
)

# Optional CTA buttons (plug in links later)
c3, c4 = st.columns(2)
with c3:
    if st.button("Open repo", key="p2_repo"):
        st.info("Add the GitHub link here.")
with c4:
    if st.button("Live demo", key="p2_demo"):
        st.info("Add the Streamlit Cloud link here.")

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

# Footer
#st.caption("Projects are continuously updated as part of my learning journey.")
