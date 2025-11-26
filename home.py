import streamlit as st

st.set_page_config(layout="wide")

# Add logo to sidebar
st.sidebar.image("assets/images/laboratorial_logo.png")

# --- LFPR Section (big highlight) ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; justify-content: center; height: 300px; text-align: center;">
            <h1>Labor Force Participation Rate</h1>
            <p>
                The LFPR is a key indicator of a country’s labor market health and economic potential. 
                A higher participation rate means a larger portion of the working-age population is engaged in or actively seeking work, 
                which can drive economic growth, increase productivity, and generate higher tax revenues. 
                Conversely, a declining LFPR may signal demographic challenges, discouraged workers, or structural barriers to employment, 
                which can limit economic expansion and social welfare. Policymakers, economists, and businesses use LFPR trends to guide decisions on workforce development, social programs, and economic policy.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: center; height: 300px;">
            <img src="https://cdn-icons-png.flaticon.com/512/8327/8327833.png" width="120">
        </div>
        """, unsafe_allow_html=True
    )

# --- Other Categories Row (3 columns) ---
col1, col2, col3 = st.columns(3)

# Employment Rate
with col1:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/2907/2907256.png" width="100"><br>
            <h3>Employment Rate</h3>
            <p>
                The Employment Rate measures the proportion of the working-age population that is currently employed. 
                A high employment rate indicates strong job availability and economic stability, while a low rate may reflect economic slowdown or structural unemployment.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# Unemployment Rate
with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="100"><br>
            <h3>Unemployment Rate</h3>
            <p>
                The Unemployment Rate measures the share of the labor force that is jobless but actively seeking work. 
                A rising unemployment rate can signal economic distress, whereas a low rate indicates a healthy job market.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# Underemployment Rate
with col3:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135714.png" width="100"><br>
            <h3>Underemployment Rate</h3>
            <p>
                The Underemployment Rate captures workers who are employed part-time or in positions below their skill level but desire full-time or more suitable work. 
                High underemployment may indicate inefficiencies in the labor market or skill mismatches.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# Centered button to forecast page
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-top: 50px;">
    """, unsafe_allow_html=True
)
st.page_link("forecast.py", label="See Future Values")
st.markdown("</div>", unsafe_allow_html=True)