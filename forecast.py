import streamlit as st
import pickle
import os
import pandas as pd
import plotly.graph_objects as go
from dateutil.relativedelta import relativedelta

st.set_page_config(layout="wide")

# -----------------------------
# Session state flags
# -----------------------------
if 'forecasts_generated' not in st.session_state:
    st.session_state.forecasts_generated = False
if 'prev_filters' not in st.session_state:
    st.session_state.prev_filters = None

# -----------------------------
# Load models
# -----------------------------
models_dir = 'models/'
models = {}
for file in os.listdir(models_dir):
    if file.endswith('.pkl'):
        name = file.replace('sarimax_model_', '').replace('.pkl', '')
        with open(os.path.join(models_dir, file), 'rb') as f:
            models[name] = pickle.load(f)

last_date = models['ER_Total'].data.dates[-1]

# -----------------------------
# UI Filters
# -----------------------------
st.title("Labor Statistics Forecasting")

categories = ['LFPR', 'ER', 'UR', 'UER']
category_names = {
    'LFPR': 'Labor Force Participation Rate',
    'ER': 'Employment Rate',
    'UR': 'Unemployment Rate',
    'UER': 'Underemployment Rate'
}

genders = ['Total', 'Male', 'Female']

selected_categories = st.sidebar.multiselect(
    "Select Categories", categories, default=categories, format_func=lambda x: category_names[x]
)
selected_genders = st.sidebar.multiselect("Select Genders", genders, default=genders)

# Year and month
current_year = pd.Timestamp.now().year
years = list(range(current_year, current_year + 10))
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

selected_year = st.sidebar.slider("Select Year", min_value=min(years), max_value=max(years), value=years[1])
selected_month = st.sidebar.slider("Select Month", 1, 12, 7)
selected_month_name = month_names[selected_month - 1]
target_date = pd.Timestamp(year=selected_year, month=selected_month, day=1)

# Historical start date
min_date = pd.Timestamp(models['ER_Total'].data.dates[0])
start_years = list(range(min_date.year, last_date.year + 1))
selected_start_year = st.sidebar.slider("Start Year", min_value=min(start_years), max_value=max(start_years), value=start_years[0])
selected_start_month = st.sidebar.slider("Start Month", 1, 12, 1)
selected_start_date = pd.Timestamp(year=selected_start_year, month=selected_start_month, day=1)

# -----------------------------
# Reset forecasts if filters change
# -----------------------------
current_filters = (tuple(selected_categories), tuple(selected_genders), selected_year, selected_month, selected_start_year, selected_start_month)
if st.session_state.prev_filters != current_filters:
    st.session_state.forecasts_generated = False
    st.session_state.prev_filters = current_filters

# -----------------------------
# Validation
# -----------------------------
if not selected_categories:
    st.error("Please select at least one category.")
if not selected_genders:
    st.error("Please select at least one gender.")

# -----------------------------
# Forecast button
# -----------------------------
steps = (target_date.year - last_date.year) * 12 + (target_date.month - last_date.month)

if steps <= 0:
    st.error("Please select a date after the last historical date.")
else:
    if st.sidebar.button("Generate Forecasts"):
        st.session_state.forecasts_generated = True

        # Forecasts
        lfpr_forecasts = {}
        er_forecasts = {}
        ur_forecasts = {}
        uer_forecasts = {}
        for gender in selected_genders:
            lfpr_forecasts[gender] = models[f'LFPR_{gender}'].forecast(steps=steps).iloc[-1]
            er_forecasts[gender] = models[f'ER_{gender}'].forecast(steps=steps).iloc[-1]
            ur_forecasts[gender] = models[f'UR_{gender}'].forecast(steps=steps).iloc[-1]
            uer_forecasts[gender] = models[f'UER_{gender}'].forecast(steps=steps).iloc[-1]

        # Display cards
        if 'Total' in selected_genders:
            st.subheader("Forecasted Percentages")
            cols = st.columns(len(selected_categories))
            for idx, cat in enumerate(selected_categories):
                with cols[idx]:
                    total_value = {
                        'LFPR': lfpr_forecasts['Total'],
                        'ER': er_forecasts['Total'],
                        'UR': ur_forecasts['Total'],
                        'UER': uer_forecasts['Total']
                    }[cat]
                    st.metric(label=f"{category_names[cat]} Total", value=f"{total_value:.2f}%")

        # Combined forecast chart
        st.subheader("Combined Forecast Overview")
        color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78']
        fig_combined = go.Figure()
        for cat in selected_categories:
            for gender in selected_genders:
                model_name = f"{cat}_{gender}"
                model = models[model_name]
                historical = pd.Series(model.data.endog, index=model.data.dates)
                historical = historical[historical.index >= selected_start_date]
                forecast = model.forecast(steps=steps)
                color = color_list[categories.index(cat) * 3 + genders.index(gender)]
                # Historical
                fig_combined.add_trace(go.Scatter(
                    x=historical.index, y=historical.values,
                    mode='lines',
                    name=f'{category_names[cat]} {gender} Historical',
                    line=dict(color=color, opacity=0.6),
                    hovertemplate='%{x}<br>%{y:.2f}<extra></extra>',
                    legendgroup=f'{cat}_{gender}'
                ))
                # Forecast
                fig_combined.add_trace(go.Scatter(
                    x=forecast.index, y=forecast.values,
                    mode='lines',
                    name=f'{category_names[cat]} {gender} Forecast',
                    line=dict(color=color),
                    hovertemplate='%{x}<br>%{y:.2f}<extra></extra>',
                    legendgroup=f'{cat}_{gender}'
                ))

        # Vertical line for forecast start
        fig_combined.add_shape(
            type="line",
            x0=historical.index[-1],
            x1=historical.index[-1],
            y0=0,
            y1=1,
            line=dict(dash="dash", color="red"),
            xref="x", yref="paper"
        )
        fig_combined.add_annotation(
            x=historical.index[-1],
            y=0.95,
            text="Forecast Start",
            showarrow=False,
            xref="x",
            yref="paper",
            xanchor="left"
        )

        fig_combined.update_layout(
            xaxis_title="Date",
            yaxis_title="Value (%)",
            hovermode="x unified",
            height=600
        )
        st.plotly_chart(fig_combined)

        # Individual category charts
        col1, col2 = st.columns(2)
        for i, cat in enumerate(selected_categories):
            col = col1 if i % 2 == 0 else col2
            with col:
                st.subheader(f"{category_names[cat]} Forecast")
                fig = go.Figure()
                forecast_values = {}
                for gender in selected_genders:
                    model_name = f"{cat}_{gender}"
                    model = models[model_name]
                    historical = pd.Series(model.data.endog, index=model.data.dates)
                    historical = historical[historical.index >= selected_start_date]
                    forecast = model.forecast(steps=steps)
                    color = color_list[categories.index(cat) * 3 + genders.index(gender)]
                    # Historical
                    fig.add_trace(go.Scatter(
                        x=historical.index, y=historical.values,
                        mode='lines',
                        name=f'{gender} Historical',
                        line=dict(color=color, opacity=0.6),
                        hovertemplate='%{x}<br>%{y:.2f}<extra></extra>'
                    ))
                    # Forecast
                    fig.add_trace(go.Scatter(
                        x=forecast.index, y=forecast.values,
                        mode='lines',
                        name=f'{gender} Forecast',
                        line=dict(color=color),
                        hovertemplate='%{x}<br>%{y:.2f}<extra></extra>'
                    ))
                    # Target marker
                    fig.add_trace(go.Scatter(
                        x=[target_date], y=[forecast.iloc[-1]],
                        mode='markers',
                        marker=dict(size=10, color=color, symbol='circle'),
                        name=f'{gender} Target',
                        showlegend=False,
                        hovertemplate=f'{gender} Target<br>%{{x}}<br>%{{y:.2f}}<extra></extra>'
                    ))
                    forecast_values[gender] = forecast.iloc[-1]

                fig.add_shape(
                    type="line",
                    x0=historical.index[-1],
                    x1=historical.index[-1],
                    y0=0,
                    y1=1,
                    line=dict(dash="dash", color="red"),
                    xref="x", yref="paper"
                )
                fig.add_annotation(
                    x=historical.index[-1],
                    y=0.95,
                    text="Forecast Start",
                    showarrow=False,
                    xref="x",
                    yref="paper",
                    xanchor="left"
                )
                fig.update_layout(
                    xaxis_title="Date",
                    yaxis_title=category_names[cat],
                    hovermode="x unified"
                )
                st.plotly_chart(fig)

                st.write(f"**Forecasted Values for {selected_month_name} {selected_year}**")
                values_df = pd.DataFrame({
                    'Gender': selected_genders,
                    'Value (%)': [f"{forecast_values[gender]:.2f}" for gender in selected_genders]
                })
                st.table(values_df)

# -----------------------------
# No data illustration
# -----------------------------
if not st.session_state.forecasts_generated:
    st.markdown(
        """
        <div style="text-align:center; margin-top:50px;">
            <img src="https://cdn-icons-png.flaticon.com/512/4076/4076549.png" width="150" style="opacity:0.5"/>
            <h3 style="color:#555;">No data loaded yet</h3>
            <p>Select your categories, genders, and date, then click <strong>Generate Forecasts</strong> to see results.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
