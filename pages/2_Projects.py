import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Projects | Asekhona Tyutyuza",
    page_icon="🧪",
    layout="centered",
)

# --- External links (EDIT THESE) ---
SUMMARY_URL = "https://github.com/TYUTYU-BOT/maish-2025-hackathon#readme"  # or Notion/Google Doc/PDF
REPO_URL    = "https://github.com/TYUTYU-BOT/maish-2025-hackathon"
DEMO_URL    = "https://your-app-url.streamlit.app"  # Streamlit Cloud or a YouTube demo

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

# ---------------- Buttons (prefer link_button if available) ----------------
cols = st.columns(3)

# Try to use st.link_button (Streamlit ≥ 1.31). If unavailable, fall back to HTML buttons.
def link_button_fallback(label: str, url: str):
    st.markdown(
        f"""
        <a href="{url}" target="_blank" rel="noopener noreferrer"
           style="display:inline-block; text-decoration:none; background:#0E1117;
                  color:white; padding:0.5rem 0.85rem; border-radius:6px; border:1px solid #30363d;">
            {label}
        </a>
        """,
        unsafe_allow_html=True,
    )

# Feature-detect st.link_button
HAS_LINK_BUTTON = hasattr(st, "link_button")

with cols[0]:
    if SUMMARY_URL:
        if HAS_LINK_BUTTON:
            st.link_button("View summary", SUMMARY_URL)
        else:
            link_button_fallback("View summary", SUMMARY_URL)
    else:
        st.info("Add a link to a write‑up or README when available.")

with cols[1]:
    if REPO_URL:
        if HAS_LINK_BUTTON:
            st.link_button("GitHub repo", REPO_URL)
        else:
            link_button_fallback("GitHub repo", REPO_URL)
    else:
        st.info("Add a GitHub URL when ready.")

with cols[2]:
    if DEMO_URL and not DEMO_URL.endswith("streamlit.app"):
        # Any URL is fine; just a gentle reminder to deploy when you can
        if HAS_LINK_BUTTON:
            st.link_button("Demo (hosted)", DEMO_URL)
        else:
            link_button_fallback("Demo (hosted)", DEMO_URL)
    elif DEMO_URL:  # keep the link even if it's a placeholder
        if HAS_LINK_BUTTON:
            st.link_button("Demo (hosted)", DEMO_URL)
        else:
            link_button_fallback("Demo (hosted)", DEMO_URL)
    else:
        st.info("Add a demo link when you deploy a prototype.")

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

c1, c2 = st.columns(2)
with c1:
    link_button_fallback("Planned repo", "https://github.com/TYUTYU-BOT")  # replace later
with c2:
    link_button_fallback("Design notes", "https://www.notion.so/")         # replace later

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

c3, c4 = st.columns(2)
with c3:
    link_button_fallback("Planned repo", "https://github.com/TYUTYU-BOT")  # replace later
with c4:
    link_button_fallback("Feature backlog", "https://www.notion.so/")      # replace later

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
