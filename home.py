import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>
    :root {
        --primary: #0F72BA;
        --primary-dark: #054BAA;
        --accent: #00D9FF;
        --surface: #0D1B2A;
        --surface-light: #1B263B;
        --text-primary: #E7F0F7;
        --text-secondary: #B0C4DE;
        --border: #415A77;
        --success: #10B981;
    }

    body {
        background-color: var(--surface);
        color: var(--text-primary);
    }

    .main {
        background-color: var(--surface);
    }

    .stMarkdown {
        color: var(--text-primary);
    }

    /* Hero Section Styling */
    .hero-container {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
        border-radius: 12px;
        padding: 40px;
        margin-bottom: 30px;
        border: 1px solid var(--border);
        box-shadow: 0 8px 24px rgba(15, 114, 186, 0.2);
    }

    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin: 0 0 20px 0;
        letter-spacing: -0.5px;
    }

    .hero-description {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.6;
        margin: 0;
    }

    /* Card Grid Styling */
    .metric-card {
        background-color: var(--surface-light);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }

    .metric-card:hover {
        border-color: var(--accent);
        background-color: rgba(0, 217, 255, 0.05);
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0, 217, 255, 0.15);
    }

    .metric-icon {
        width: 80px;
        height: 80px;
        margin: 0 auto 16px;
        opacity: 0.9;
    }

    .metric-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin: 12px 0;
    }

    .metric-description {
        font-size: 0.9rem;
        color: var(--text-secondary);
        line-height: 1.5;
        margin: 0;
    }

    /* CTA Section */
    .cta-section {
        text-align: center;
        margin-top: 50px;
        padding: 40px;
        background-color: var(--surface-light);
        border-radius: 12px;
        border: 1px solid var(--border);
    }

    .cta-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 12px;
    }

    .cta-subtitle {
        font-size: 1rem;
        color: var(--text-secondary);
        margin-bottom: 20px;
    }

    /* Enhanced styling for st.page_link() to match CTA button design */
    .stPageLink {
        display: flex !important;
        justify-content: center !important;
        margin-top: 24px !important;
    }

    [data-testid="stPageLink"] {
        display: inline-block !important;
    }

    [data-testid="stPageLink"] a {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
        color: white !important;
        padding: 14px 40px !important;
        border-radius: 8px !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border: none !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(15, 114, 186, 0.35) !important;
        display: inline-block !important;
    }

    [data-testid="stPageLink"] a:hover {
        background: linear-gradient(135deg, var(--primary-dark) 0%, #033A7A 100%) !important;
        box-shadow: 0 10px 28px rgba(15, 114, 186, 0.5) !important;
        transform: translateY(-3px) !important;
    }
</style>
""", unsafe_allow_html=True)

# Add logo to sidebar
st.sidebar.image("assets/images/laboratorial_logo.png", use_container_width=True)

st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">Labor Force Participation Rate</h1>
    <p class="hero-description">
        The LFPR is a key indicator of a country's labor market health and economic potential. 
        A higher participation rate means a larger portion of the working-age population is engaged in or actively seeking work, 
        which can drive economic growth, increase productivity, and generate higher tax revenues. 
        Conversely, a declining LFPR may signal demographic challenges, discouraged workers, or structural barriers to employment, 
        which can limit economic expansion and social welfare. Policymakers, economists, and businesses use LFPR trends to guide decisions on workforce development, social programs, and economic policy.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="metric-card">
        <img src="https://cdn-icons-png.flaticon.com/512/2907/2907256.png" class="metric-icon" alt="Employment Rate">
        <h3 class="metric-title">Employment Rate</h3>
        <p class="metric-description">
            The Employment Rate measures the proportion of the working-age population that is currently employed. 
            A high employment rate indicates strong job availability and economic stability, while a low rate may reflect economic slowdown or structural unemployment.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="metric-icon" alt="Unemployment Rate">
        <h3 class="metric-title">Unemployment Rate</h3>
        <p class="metric-description">
            The Unemployment Rate measures the share of the labor force that is jobless but actively seeking work. 
            A rising unemployment rate can signal economic distress, whereas a low rate indicates a healthy job market.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135714.png" class="metric-icon" alt="Underemployment Rate">
        <h3 class="metric-title">Underemployment Rate</h3>
        <p class="metric-description">
            The Underemployment Rate captures workers who are employed part-time or in positions below their skill level but desire full-time or more suitable work. 
            High underemployment may indicate inefficiencies in the labor market or skill mismatches.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 3rem;">
""", unsafe_allow_html=True)
st.page_link("forecast.py", label="📈 Explore Future Forecasts")
st.markdown("</div>", unsafe_allow_html=True)



