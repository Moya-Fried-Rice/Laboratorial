import streamlit as st
import pickle
import os
import pandas as pd
import plotly.graph_objects as go
from dateutil.relativedelta import relativedelta

st.set_page_config(layout="wide")

st.markdown("""
<style>
    /* Metric Cards */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #0F72BA 0%, #0a5089 100%);
        padding: 24px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 4px 16px rgba(15, 114, 186, 0.15);
        transition: all 0.3s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(15, 114, 186, 0.25);
        border-color: rgba(0, 212, 255, 0.3);
    }
    [data-testid="stMetricLabel"] {
        color: rgba(255,255,255,0.85) !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        letter-spacing: 0.3px !important;
    }
    [data-testid="stMetricValue"] {
        color: #00d4ff !important;
        font-size: 32px !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricDelta"] {
        color: #00d4ff !important;
        font-size: 13px !important;
    }

    /* Sidebar Sections */
    .sidebar-header {
        background: linear-gradient(135deg, #0F72BA 0%, #0a5089 100%);
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 28px;
        border-bottom: 3px solid #00d4ff;
        box-shadow: 0 4px 12px rgba(15, 114, 186, 0.15);
    }
    .sidebar-header h2 {
        color: white;
        margin: 0;
        font-size: 22px;
        font-weight: 700;
    }
    .sidebar-header p {
        color: rgba(255,255,255,0.7);
        margin: 8px 0 0 0;
        font-size: 13px;
        font-weight: 400;
    }

    .sidebar-section-title {
        font-size: 12px;
        font-weight: 700;
        color: #0F72BA;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 14px;
        display: block;
        padding: 8px 0;
        border-bottom: 2px solid #e5e7eb;
    }

    /* Slider styling */
    [data-testid="stSlider"] div[role="slider"] {
        background-color: #0F72BA !important;
    }

    [data-testid="stSlider"] div[role="slider"]::after {
        background-color: #0F72BA !important;
    }

    /* Multiselect styling */
    [data-testid="stMultiSelect"] div[data-baseweb="select"] {
        border-color: #0F72BA !important;
    }

    [data-testid="stMultiSelect"] div[data-baseweb="select"]:focus-within {
        border-color: #0F72BA !important;
        box-shadow: 0 0 0 3px rgba(15, 114, 186, 0.1) !important;
    }

    [data-testid="stMultiSelect"] div[role="button"] {
        background-color: #0F72BA !important;
        border-color: #0F72BA !important;
    }

    /* Slider track color */
    div.stSlider > div > div > div {
        background-color: #0F72BA !important;
    }

    /* Multi-select tag/chip background */
    [data-baseweb="tag"] {
        background-color: #0F72BA !important;
    }

    [data-baseweb="tag"] span {
        color: white !important;
    }

    /* Slider thumb/handle */
    div[role="slider"] {
        background: #0F72BA !important;
    }

    /* Category and Gender select boxes accent */
    .stSelectbox [data-baseweb="select"] {
        border-color: #0F72BA !important;
    }

    .stSelectbox [data-baseweb="select"]:hover {
        border-color: #0a5089 !important;
    }

    .stSelectbox [data-baseweb="select"]:focus-within {
        border-color: #0F72BA !important;
        box-shadow: 0 0 0 3px rgba(15, 114, 186, 0.1) !important;
    }

    /* Section Headers */
    .section-header {
        background: linear-gradient(135deg, #0F72BA 0%, #0a5089 100%);
        padding: 20px 24px;
        border-radius: 10px;
        margin: 32px 0 20px 0;
        border-left: 5px solid #00d4ff;
        box-shadow: 0 4px 12px rgba(15, 114, 186, 0.12);
    }
    .section-header h3 {
        color: white;
        margin: 0;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 0.2px;
    }
    .section-header span {
        color: #00d4ff;
        font-weight: 700;
    }

    /* Chart Containers */
    .chart-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #eef2f7 100%);
        padding: 0;
        border-radius: 12px;
        margin-bottom: 28px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        overflow: hidden;
    }
    .chart-container-title {
        background: linear-gradient(135deg, #0F72BA 0%, #0a5089 100%);
        color: white;
        padding: 18px 24px;
        font-weight: 700;
        font-size: 16px;
        border-bottom: 1px solid rgba(0, 212, 255, 0.2);
        letter-spacing: 0.2px;
    }
    .chart-content {
        padding: 24px;
    }

    /* Data Table */
    .data-table-header {
        background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%);
        padding: 15px 16px;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        margin-top: 16px;
        margin-bottom: 12px;
    }
    .data-table-header p {
        margin: 0;
        color: #1f2937;
        font-weight: 600;
        font-size: 13px;
    }

    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 80px 40px;
        background: linear-gradient(135deg, #f5f7fa 0%, #eef2f7 100%);
        border-radius: 12px;
        margin-top: 40px;
        border: 1px dashed #d1d5db;
    }
    .empty-state-icon {
        font-size: 64px;
        margin-bottom: 20px;
    }
    .empty-state h3 {
        color: #0F72BA;
        margin: 0 0 10px 0;
        font-size: 20px;
        font-weight: 700;
    }
    .empty-state p {
        color: #6b7280;
        font-size: 15px;
        margin: 0;
        line-height: 1.5;
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #0F72BA 0%, #0a5089 100%) !important;
        color: white !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(15, 114, 186, 0.2) !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0a5089 0%, #073d5c 100%) !important;
        border-color: #00d4ff !important;
        box-shadow: 0 6px 16px rgba(15, 114, 186, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    /* Divider */
    .divider {
        margin: 40px 0;
        border-top: 2px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

models_dir = 'models/'
models = {}
for file in os.listdir(models_dir):
    if file.endswith('.pkl'):
        name = file.replace('sarimax_model_', '').replace('.pkl', '')
        with open(os.path.join(models_dir, file), 'rb') as f:
            models[name] = pickle.load(f)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h1 style="margin: 0; color: #0F72BA; font-size: 32px; font-weight: 700; letter-spacing: -0.5px;">Labor Statistics Forecasting</h1>
        <p style="margin: 12px 0 0 0; color: #6b7280; font-size: 16px; font-weight: 400;">Generate and analyze labor market predictions with precision</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("""
    <div class="sidebar-header">
        <h2>Forecast Parameters</h2>
        <p>Configure your analysis settings</p>
    </div>
""", unsafe_allow_html=True)

categories = ['LFPR', 'ER', 'UR', 'UER']
category_names = {
    'LFPR': 'Labor Force Participation Rate',
    'ER': 'Employment Rate',
    'UR': 'Unemployment Rate',
    'UER': 'Underemployment Rate'
}

genders = ['Total', 'Male', 'Female']

st.sidebar.markdown('<span class="sidebar-section-title">Select Data</span>', unsafe_allow_html=True)
selected_categories = st.sidebar.multiselect(
    "Categories", categories, default=categories, format_func=lambda x: category_names[x], key="categories"
)
selected_genders = st.sidebar.multiselect("Genders", genders, default=genders, key="genders")

st.sidebar.markdown('<span class="sidebar-section-title">Target Date</span>', unsafe_allow_html=True)
current_year = pd.Timestamp.now().year
years = list(range(current_year, current_year + 10))
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

selected_year = st.sidebar.slider("Year", min_value=min(years), max_value=max(years), value=years[1], key="target_year")
selected_month = st.sidebar.slider("Month", 1, 12, 7, key="target_month")
selected_month_name = month_names[selected_month - 1]
target_date = pd.Timestamp(year=selected_year, month=selected_month, day=1)

st.sidebar.markdown('<span class="sidebar-section-title">Historical Data Range</span>', unsafe_allow_html=True)
min_date = pd.Timestamp(models['ER_Total'].data.dates[0])
last_date = pd.Timestamp(models['ER_Total'].data.dates[-1])
start_years = list(range(min_date.year, last_date.year + 1))
selected_start_year = st.sidebar.slider("Start Year", min_value=min(start_years), max_value=max(start_years),
                                        value=start_years[0], key="start_year")
selected_start_month = st.sidebar.slider("Start Month", 1, 12, 1, key="start_month")
selected_start_date = pd.Timestamp(year=selected_start_year, month=selected_start_month, day=1)

# Initialize session state variables if not already present
if 'forecasts_generated' not in st.session_state:
    st.session_state.forecasts_generated = False
if 'prev_filters' not in st.session_state:
    st.session_state.prev_filters = None
if 'lfpr_forecasts' not in st.session_state:
    st.session_state.lfpr_forecasts = {}
if 'er_forecasts' not in st.session_state:
    st.session_state.er_forecasts = {}
if 'ur_forecasts' not in st.session_state:
    st.session_state.ur_forecasts = {}
if 'uer_forecasts' not in st.session_state:
    st.session_state.uer_forecasts = {}
if 'forecast_series' not in st.session_state:
    st.session_state.forecast_series = {}

current_filters = (tuple(selected_categories), tuple(selected_genders), selected_year, selected_month,
                   selected_start_year, selected_start_month)
if st.session_state.prev_filters != current_filters:
    st.session_state.forecasts_generated = False
    st.session_state.lfpr_forecasts = {}
    st.session_state.er_forecasts = {}
    st.session_state.ur_forecasts = {}
    st.session_state.uer_forecasts = {}
    st.session_state.forecast_series = {}
    st.session_state.prev_filters = current_filters

if not selected_categories:
    st.error("Please select at least one category.")
if not selected_genders:
    st.error("Please select at least one gender.")

steps = (target_date.year - last_date.year) * 12 + (target_date.month - last_date.month)

if steps <= 0:
    st.error("Please select a date after the last historical date.")
else:
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("Generate Forecasts", use_container_width=True):
            st.session_state.forecasts_generated = True

    if not st.session_state.forecasts_generated:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">📈</div>
            <h3>No forecasts generated yet</h3>
            <p>Click the button above to generate labor market forecasts<br>based on your selected parameters.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if not st.session_state.forecast_series:
            for gender in selected_genders:
                lfpr_forecast = models[f'LFPR_{gender}'].forecast(steps=steps)
                st.session_state.lfpr_forecasts[gender] = lfpr_forecast.iloc[-1]
                st.session_state.forecast_series[f'LFPR_{gender}'] = lfpr_forecast
                er_forecast = models[f'ER_{gender}'].forecast(steps=steps)
                st.session_state.er_forecasts[gender] = er_forecast.iloc[-1]
                st.session_state.forecast_series[f'ER_{gender}'] = er_forecast
                ur_forecast = models[f'UR_{gender}'].forecast(steps=steps)
                st.session_state.ur_forecasts[gender] = ur_forecast.iloc[-1]
                st.session_state.forecast_series[f'UR_{gender}'] = ur_forecast
                uer_forecast = models[f'UER_{gender}'].forecast(steps=steps)
                st.session_state.uer_forecasts[gender] = uer_forecast.iloc[-1]
                st.session_state.forecast_series[f'UER_{gender}'] = uer_forecast

        if 'Total' in selected_genders:
            st.markdown(f"""
                <div class="section-header">
                    <h3>Forecasted Values for <span>{selected_month_name} {selected_year}</span></h3>
                </div>
            """, unsafe_allow_html=True)

            cols = st.columns(len(selected_categories))
            for idx, cat in enumerate(selected_categories):
                with cols[idx]:
                    total_value = {
                        'LFPR': st.session_state.lfpr_forecasts['Total'],
                        'ER': st.session_state.er_forecasts['Total'],
                        'UR': st.session_state.ur_forecasts['Total'],
                        'UER': st.session_state.uer_forecasts['Total']
                    }[cat]
                    previous = models[f'{cat}_Total'].data.endog[-1]
                    delta = total_value - previous
                    st.metric(label=category_names[cat], value=f"{total_value:.2f}%", delta=f"{delta:+.2f}%")

        st.markdown("""
            <div class="section-header">
                <h3>Combined Forecast Overview</h3>
            </div>
        """, unsafe_allow_html=True)

        color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
                      '#17becf', '#aec7e8', '#ffbb78']
        fig_combined = go.Figure()
        for cat in selected_categories:
            for gender in selected_genders:
                model_name = f"{cat}_{gender}"
                model = models[model_name]
                historical = pd.Series(model.data.endog, index=model.data.dates)
                historical = historical[historical.index >= selected_start_date]
                forecast = st.session_state.forecast_series[model_name]
                color = color_list[categories.index(cat) * 3 + genders.index(gender)]
                fig_combined.add_trace(go.Scatter(
                    x=historical.index, y=historical.values,
                    mode='lines',
                    name=f'{category_names[cat]} {gender} Historical',
                    line=dict(color=color),
                    opacity=0.6,
                    hovertemplate='%{x}<br>%{y:.2f}<extra></extra>',
                    legendgroup=f'{cat}_{gender}'
                ))
                fig_combined.add_trace(go.Scatter(
                    x=forecast.index, y=forecast.values,
                    mode='lines',
                    name=f'{category_names[cat]} {gender} Forecast',
                    line=dict(color=color, dash='dash'),
                    hovertemplate='%{x}<br>%{y:.2f}<extra></extra>',
                    legendgroup=f'{cat}_{gender}'
                ))

        fig_combined.add_shape(
            type="line",
            x0=selected_start_date,
            x1=selected_start_date,
            y0=0,
            y1=1,
            line=dict(dash="dash", color="#0F72BA", width=2),
            xref="x", yref="paper"
        )
        fig_combined.add_annotation(
            x=selected_start_date,
            y=0.95,
            text="Forecast Start",
            showarrow=False,
            xref="x",
            yref="paper",
            xanchor="left",
            bgcolor="#0F72BA",
            bordercolor="#0F72BA",
            font=dict(color="white", size=12)
        )

        fig_combined.update_layout(
            xaxis_title="Date",
            yaxis_title="Value (%)",
            hovermode="x unified",
            height=600,
            template="plotly_white",
            plot_bgcolor="rgba(240, 242, 247, 0.5)",
            paper_bgcolor="white",
            font=dict(family="sans-serif", size=14, color="#000000"),
            xaxis=dict(title_font=dict(size=14, color="#000000"), tickfont=dict(size=12, color="#000000")),
            yaxis=dict(title_font=dict(size=14, color="#000000"), tickfont=dict(size=12, color="#000000")),
            legend=dict(font=dict(size=12, color="#000000"), bgcolor="rgba(255,255,255,0.9)", bordercolor="#d1d5db",
                        borderwidth=1)
        )
        st.plotly_chart(fig_combined, use_container_width=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown("""
            <div class="section-header">
                <h3>Category Deep Dive Analysis</h3>
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        for i, cat in enumerate(selected_categories):
            col = col1 if i % 2 == 0 else col2
            with col:
                st.markdown(f"""
                    <div class="chart-container">
                        <div class="chart-container-title">{category_names[cat]}</div>
                        <div class="chart-content">
                """, unsafe_allow_html=True)

                fig = go.Figure()
                forecast_values = {}
                for gender in selected_genders:
                    model_name = f"{cat}_{gender}"
                    model = models[model_name]
                    historical = pd.Series(model.data.endog, index=model.data.dates)
                    historical = historical[historical.index >= selected_start_date]
                    forecast = st.session_state.forecast_series[model_name]
                    color = color_list[categories.index(cat) * 3 + genders.index(gender)]
                    fig.add_trace(go.Scatter(
                        x=historical.index, y=historical.values,
                        mode='lines',
                        name=f'{gender} Historical',
                        line=dict(color=color),
                        opacity=0.6,
                        hovertemplate='%{x}<br>%{y:.2f}<extra></extra>'
                    ))
                    fig.add_trace(go.Scatter(
                        x=forecast.index, y=forecast.values,
                        mode='lines',
                        name=f'{gender} Forecast',
                        line=dict(color=color, dash='dash'),
                        hovertemplate='%{x}<br>%{y:.2f}<extra></extra>'
                    ))
                    fig.add_trace(go.Scatter(
                        x=[target_date], y=[forecast.iloc[-1]],
                        mode='markers',
                        marker=dict(size=10, color=color, symbol='circle', line=dict(width=2, color='white')),
                        name=f'{gender} Target',
                        showlegend=False,
                        hovertemplate=f'{gender} Target<br>%{{x}}<br>%{{y:.2f}}<extra></extra>'
                    ))
                    forecast_values[gender] = forecast.iloc[-1]

                fig.add_shape(
                    type="line",
                    x0=selected_start_date,
                    x1=selected_start_date,
                    y0=0,
                    y1=1,
                    line=dict(dash="dash", color="#0F72BA", width=2),
                    xref="x", yref="paper"
                )
                fig.add_annotation(
                    x=selected_start_date,
                    y=0.95,
                    text="Forecast Start",
                    showarrow=False,
                    xref="x",
                    yref="paper",
                    xanchor="left",
                    bgcolor="#0F72BA",
                    bordercolor="#0F72BA",
                    font=dict(color="white", size=12)
                )
                fig.update_layout(
                    xaxis_title="Date",
                    yaxis_title=category_names[cat],
                    hovermode="x unified",
                    height=400,
                    template="plotly_white",
                    plot_bgcolor="rgba(240, 242, 247, 0.5)",
                    paper_bgcolor="white",
                    font=dict(family="sans-serif", size=14, color="#000000"),
                    xaxis=dict(title_font=dict(size=14, color="#000000"), tickfont=dict(size=12, color="#000000")),
                    yaxis=dict(title_font=dict(size=14, color="#000000"), tickfont=dict(size=12, color="#000000")),
                    margin=dict(l=50, r=20, t=20, b=50),
                    legend=dict(font=dict(size=12, color="#000000"), bgcolor="rgba(255,255,255,0.9)",
                                bordercolor="#d1d5db", borderwidth=1)
                )
                st.plotly_chart(fig, use_container_width=True)

                st.markdown(f"""
                    <div class="data-table-header">
                        <p>Forecasted Values for {selected_month_name} {selected_year}</p>
                    </div>
                """, unsafe_allow_html=True)

                values_df = pd.DataFrame({
                    'Gender': selected_genders,
                    'Value (%)': [f"{forecast_values[gender]:.2f}" for gender in selected_genders]
                })
                st.dataframe(values_df, use_container_width=True, hide_index=True)

                st.markdown('</div></div>', unsafe_allow_html=True)
