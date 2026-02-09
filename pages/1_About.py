import streamlit as st

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="About | Asekhona Tyutyuza",
    page_icon="👋",
    layout="centered",
)

# ---------------------------------------------------------
# Page header
# ---------------------------------------------------------
st.title("About")

st.markdown(
    """
    Hello, I’m **Asekhona Tyutyuza** — an aspiring data scientist with a strong interest
    in **data-driven problem solving**, **visual analytics**, and building
    **interactive applications** using Python and Streamlit.

    I am motivated by the challenge of transforming complex data into
    clear, accessible insights through thoughtful analysis and design.
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Academic & Professional Focus
# ---------------------------------------------------------
st.subheader("Academic & Professional Focus")

st.markdown(
    """
    My current focus areas include:

    - Developing a strong foundation in **data science, analytics, and machine learning**
    - Designing **interactive dashboards and analytical tools** for data exploration
    - Applying best practices in **clean code, reproducibility, and usability**
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Areas of Interest
# ---------------------------------------------------------
st.subheader("Areas of Interest")

st.markdown(
    """
    - Data Visualization and Storytelling  
    - Applied Data Science and Analytics  
    - Interactive Web Applications  
    - Research Methods and Technical Writing  
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Goals & Vision
# ---------------------------------------------------------
st.subheader("Goals & Vision")

st.markdown(
    """
    My goal is to continue developing practical, industry- and research-relevant skills
    through coursework, structured training programmes, and hands-on projects.

    This portfolio serves as a living record of my learning journey and a platform
    to showcase selected work that reflects my growth in data science,
    analytical thinking, and software development.
    """
)
