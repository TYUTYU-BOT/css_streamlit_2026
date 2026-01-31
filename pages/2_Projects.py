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
    These projects reflect my growing interests in data analysis, visualization, and
    building interactive applications with Python and Streamlit.
    
    Each project focuses on practical problem-solving and applying concepts learned
    through coursework and independent exploration.
    """
)

st.markdown("---")

# ---------- Project 1 ----------
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
    - User-friendly layout for non-technical users  
    
    **Tools & Skills:** Python, Streamlit, Data Visualization
    """
)

st.markdown("---")

# ---------- Project 2 ----------
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

st.markdown("---")

# Placeholder for future projects
st.subheader("➕ More Projects Coming Soon")
st.markdown(
    """
    This section will be updated as I continue working on new coursework,
    experiments, and personal projects.
    """
)

# Footer
#st.caption("Projects are continuously updated as part of my learning journey.")
