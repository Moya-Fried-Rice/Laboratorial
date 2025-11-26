import streamlit as st

st.title("About Laboratorial")

st.markdown("""
## Predictive Labor Market Analytics

Laboratorial is a Streamlit-based application designed for forecasting key labor market statistics using advanced time series modeling techniques.

### Features

- **Interactive Forecasting**: Generate forecasts for various labor market indicators
- **Multiple Models**: Support for Employment Rate, Labor Force Participation Rate, Underemployment Rate, and Unemployment Rate
- **Demographic Breakdown**: Separate models for Total, Male, and Female categories
- **Visual Analytics**: Interactive charts and data visualizations

### Technical Details

- **Modeling Approach**: SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous factors)
- **Framework**: Built with Streamlit for web-based deployment
- **Data**: Pre-trained models stored in the `models/` directory

### Models Available

The application includes pre-trained models for:
- **Employment Rate (ER)**: Total, Male, Female
- **Labor Force Participation Rate (LFPR)**: Total, Male, Female  
- **Underemployment Rate (UER)**: Total, Male, Female
- **Unemployment Rate (UR)**: Total, Male, Female

### Getting Started

1. Navigate to the Forecast page
2. Select your desired model and forecast horizon
3. Click "Generate Forecast" to view predictions

For more information, check the README.md file in the project root.
""")

st.markdown("---")
st.markdown("*Laboratorial © 2025 · Predictive Labor Market Analytics*")
