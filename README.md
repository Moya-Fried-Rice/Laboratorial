# Labor Statistics Forecasting App

This Streamlit application loads pre-trained SARIMAX models for labor statistics and provides a simple forecasting UI.

## Models Available

The app loads models for:
- Employment Rate (ER): Total, Male, Female
- Labor Force Participation Rate (LFPR): Total, Male, Female
- Underemployment Rate (UER): Total, Male, Female
- Unemployment Rate (UR): Total, Male, Female

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the App

Run the Streamlit app:
```
streamlit run app.py
```

## Usage

1. Select a model from the dropdown.
2. Choose the number of forecast steps (months).
3. Click "Generate Forecast" to view the forecasted values and chart.

## Troubleshooting

- Ensure all model files are present in the `models/` folder.
- Make sure Python environment has the required packages installed.