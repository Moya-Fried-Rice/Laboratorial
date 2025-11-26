import streamlit as st

# Page config
st.set_page_config(
    page_title="Laboratorial",
    page_icon=":material/android_cell_4_bar:",
    layout="wide"
)

# Define pages with material icons
home_page = st.Page(
    "home.py",
    title="Home",
    icon=":material/home:"
)

forecast_page = st.Page(
    "forecast.py",
    title="Forecast",
    icon=":material/stacked_line_chart:"
)

about_page = st.Page(
    "about.py",
    title="About",
    icon=":material/info:"
)

# Navigation (simple, clean)
# st.sidebar.image("assets/images/laboratorial_logo.png")
pg = st.navigation(
    pages=[home_page, forecast_page, about_page],
    position="sidebar",  # or "top"
)

# Run selected page
pg.run()

# Footer
st.markdown(
    """
    <br><hr>
    <div style='text-align: center; color: gray; font-size: 13px;'>
        Laboratorial © 2025 · Predictive Labor Market Analytics
    </div>
    """,
    unsafe_allow_html=True
)
