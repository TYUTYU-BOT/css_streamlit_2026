import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Projects | Asekhona Tyutyuza",
    page_icon="📁",
    layout="centered",
)

# =========================================================
# EXTERNAL LINKS
# =========================================================
SUMMARY_URL = "https://github.com/TYUTYU-BOT/maish-2025-hackathon#readme"
REPO_URL    = "https://github.com/TYUTYU-BOT/maish-2025-hackathon"
DEMO_URL    = ""  # Add Streamlit or YouTube demo when available

# =========================================================
# PAGE HEADER
# =========================================================
st.title("Projects")

st.markdown(
    """
This page presents selected **projects and project concepts** that demonstrate my
interests in **data science**, **machine learning**, and **interactive application development**.

The focus is on practical problem-solving, applied analytics, and translating ideas
into functional, user-facing tools.
"""
)

st.markdown("---")

# =========================================================
# FEATURED PROJECT
# =========================================================
st.subheader("Featured Project — MAISH 2025 Hackathon (🥇 1st Place)")

st.markdown(
    """
**Problem:** Limited access to timely, data-driven insights for small-scale farmers  
**Solution:** AI-powered agricultural decision-support system  
**Outcome:** First place in a 3-day national hackathon
"""
)

with st.expander("Project overview & technical details"):
    st.markdown(
        """
Developed an AI-assisted tool designed to support farmers through:

- Crop and livestock disease detection  
- Supply and resource optimization  
- Data-informed decision support  

**Skills & Tools:** Python, data analysis, machine learning concepts,
rapid prototyping, collaborative development under time constraints  

**Team:** Asekhona Tyutyuza, Brightness Mapule Masilela
"""
    )

# ---------------------------------------------------------
# LINKS
# ---------------------------------------------------------
cols = st.columns(3)

def link_button_fallback(label: str, url: str):
    """Fallback button for Streamlit versions without st.link_button."""
    st.markdown(
        f"""
<a href="{url}" target="_blank" rel="noopener noreferrer"
   style="display:inline-block; text-decoration:none;
          background:#0E1117; color:white;
          padding:0.5rem 0.85rem; border-radius:6px;
          border:1px solid #30363d;">{label}</a>
""",
        unsafe_allow_html=True,
    )

HAS_LINK_BUTTON = hasattr(st, "link_button")

with cols[0]:
    if HAS_LINK_BUTTON:
        st.link_button("Project summary", SUMMARY_URL)
    else:
        link_button_fallback("Project summary", SUMMARY_URL)

with cols[1]:
    if HAS_LINK_BUTTON:
        st.link_button("GitHub repository", REPO_URL)
    else:
        link_button_fallback("GitHub repository", REPO_URL)

with cols[2]:
    if DEMO_URL:
        if HAS_LINK_BUTTON:
            st.link_button("Live demo", DEMO_URL)
        else:
            link_button_fallback("Live demo", DEMO_URL)
    else:
        st.caption("Demo to be added")

st.markdown("---")

# =========================================================
# CONCEPT & PLANNED PROJECTS
# =========================================================


