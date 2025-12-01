import streamlit as st

# Add logo to sidebar
st.sidebar.image("assets/images/laboratorial_logo.png", use_container_width=True)

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

    /* Hero Section */
    .hero-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
        border-radius: 12px;
        padding: 50px 40px;
        margin-bottom: 40px;
        border: 1px solid var(--border);
        box-shadow: 0 12px 32px rgba(15, 114, 186, 0.2);
    }

    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin: 0 0 16px 0;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.6;
        margin: 0;
    }

    /* Section Headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 40px 0 24px 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .section-icon {
        width: 32px;
        height: 32px;
        opacity: 0.8;
    }

    /* Feature Cards */
    .feature-card {
        background-color: var(--surface-light);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 28px;
        transition: all 0.3s ease;
    }

    .feature-card:hover {
        border-color: var(--accent);
        background-color: rgba(0, 217, 255, 0.05);
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0, 217, 255, 0.15);
    }

    .feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-primary);
        margin: 0 0 8px 0;
    }

    .feature-description {
        font-size: 0.95rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin: 0;
    }

    /* Model Cards */
    .model-card {
        background-color: var(--surface-light);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .model-card:hover {
        border-color: var(--accent);
        background-color: rgba(0, 217, 255, 0.05);
        box-shadow: 0 8px 24px rgba(0, 217, 255, 0.1);
    }

    .model-name {
        font-size: 1rem;
        font-weight: 600;
        color: var(--accent);
        margin: 0;
    }

    .model-variants {
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin: 8px 0 0 0;
    }

    /* Content Text */
    .content-text {
        color: var(--text-secondary);
        line-height: 1.8;
        font-size: 0.95rem;
    }

    .highlight {
        color: var(--accent);
        font-weight: 600;
    }

    /* New Model Container and Variant Badge Styling */
    .model-container {
        background: linear-gradient(135deg, var(--surface-light) 0%, rgba(15, 114, 186, 0.08) 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 24px;
        transition: all 0.3s ease;
        height: 100%;
        margin-bottom: 25px;
    }

    .model-container:hover {
        border-color: var(--accent);
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.08) 0%, rgba(15, 114, 186, 0.12) 100%);
        box-shadow: 0 12px 32px rgba(0, 217, 255, 0.15);
        transform: translateY(-4px);
    }

    .model-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--accent);
        margin: 0 0 16px 0;
        letter-spacing: 0.3px;
    }

    .variants-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .variant-badge {
        display: inline-block;
        background-color: var(--primary);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid var(--primary-dark);
        transition: all 0.2s ease;
    }

    .variant-badge:hover {
        background-color: var(--accent);
        color: var(--surface);
        border-color: var(--accent);
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-header">
    <h1 class="hero-title">Laboratorial</h1>
    <p class="hero-subtitle">Predictive Labor Market Analytics for Data-Driven Insights</p>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<h2 class="section-header">Key Features</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">Interactive Forecasting</h3>
        <p class="feature-description">Generate accurate forecasts for key labor market indicators with customizable time horizons.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">Multiple Models</h3>
        <p class="feature-description">Support for Employment Rate, Labor Force Participation, Underemployment, and Unemployment rates.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">Demographic Breakdown</h3>
        <p class="feature-description">Separate predictive models for Total, Male, and Female population segments.</p>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown("""
<h2 class="section-header">About Laboratorial</h2>
<p class="content-text">
Laboratorial is a Streamlit-based application designed for <span class="highlight">forecasting key labor market statistics</span> using advanced time series modeling techniques. Built to support labor economists, policy makers, and financial analysts, the platform provides actionable insights into workforce trends and economic dynamics.
</p>
""", unsafe_allow_html=True)

# Technical Details
st.markdown("""
<h2 class="section-header">Technical Approach</h2>
<p class="content-text">
Our forecasting engine leverages <span class="highlight">SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous factors)</span> models—a proven statistical methodology for capturing temporal patterns and seasonal variations in labor market data. This approach enables robust predictions while maintaining interpretability.
</p>
""", unsafe_allow_html=True)

# Models Available Section
st.markdown("""
<h2 class="section-header">Labor Market Indicators</h2>
<p class="content-text" style="margin-bottom: 32px;">
Our platform provides four core labor market indicators, each with demographic breakdowns for comprehensive analysis.
</p>
""", unsafe_allow_html=True)

models_data = {
    "Employment Rate (ER)": ["Total", "Male", "Female"],
    "Labor Force Participation (LFPR)": ["Total", "Male", "Female"],
    "Underemployment Rate (UER)": ["Total", "Male", "Female"],
    "Unemployment Rate (UR)": ["Total", "Male", "Female"],
}

col1, col2 = st.columns(2, gap="large")
columns = [col1, col2]

for idx, (model_name, variants) in enumerate(models_data.items()):
    with columns[idx % 2]:
        st.markdown(f"""
        <div class="model-container">
            <p class="model-title">{model_name}</p>
            <div class="variants-container">
                {''.join([f'<span class="variant-badge">{variant}</span>' for variant in variants])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Getting Started Section
st.markdown("""
<h2 class="section-header">Getting Started</h2>
<p class="content-text">
<strong>Step 1:</strong> Navigate to the Forecast page using the sidebar menu.<br>
<strong>Step 2:</strong> Select your desired labor market indicator and demographic segment.<br>
<strong>Step 3:</strong> Specify your forecast horizon and generate predictions.<br>
<strong>Step 4:</strong> Analyze visualizations and export insights for further analysis.
</p>
""", unsafe_allow_html=True)

