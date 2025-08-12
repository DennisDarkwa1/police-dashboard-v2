import streamlit as st
from PIL import Image

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="POLICE SERVICE NORTHERN IRELAND",
    layout="wide"
)

# -------------------------
# Title
# -------------------------
st.title("🚓 POLICE SERVICE NORTHERN IRELAND")
st.markdown("### Interactive Dashboard - Crime Data Insights & Forecasts")

# -------------------------
# Tabs
# -------------------------
tab1, tab2, tab3 = st.tabs([
    "Anti-Social Behaviour Overview",
    "Crime Insights Dashboard",
    "Forecast for the Next Six Months"
])

# -------------------------
# TAB 1 - Anti-Social Behaviour
# -------------------------
with tab1:
    st.header("Anti-Social Behaviour in Northern Ireland")
    st.markdown("""
    Anti-social behaviour is the **highest recorded crime** in the dataset.  
    It includes actions that cause harassment, alarm, or distress to people in the community.  
    Law enforcement agencies are focusing efforts to address these issues and maintain public safety.
    """)
    
    # Display image
    try:
        img = Image.open("uk_police_arrest.jpg")  # Ensure this file is in the repo root
        st.image(img, caption="UK Police arresting suspect for anti-social behaviour", use_column_width=True)
    except FileNotFoundError:
        st.error("Image 'uk_police_arrest.jpg' not found. Please add it to the repo.")

# -------------------------
# TAB 2 - Crime Insights Dashboard
# -------------------------
with tab2:
    st.header("Crime Insights Dashboard")
    st.markdown("Visual representation of key crime trends in Northern Ireland.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("seasonal_crime.png", caption="Seasonal Crime Patterns", use_column_width=True)
        st.image("Monthly_crime.png", caption="Monthly Crime Trends", use_column_width=True)
        st.image("heatmap.png", caption="Crime Heatmap", use_column_width=True)

    with col2:
        st.image("Top_10_crime_location.png", caption="Top 10 Crime Locations", use_column_width=True)
        st.image("Crime_type.png", caption="Crime Type Distribution", use_column_width=True)
        st.image("Time_series_crime_count.png", caption="Crime Count Over Time", use_column_width=True)

# -------------------------
# TAB 3 - Forecast
# -------------------------
with tab3:
    st.header("Crime Forecast for the Next Six Months")
    st.markdown("Predictive analysis based on historical crime data to anticipate trends.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("Monthly_crime_count.png", caption="Monthly Crime Count", use_column_width=True)
    with col2:
        st.image("Crime_forecast.png", caption="Forecasted Crime Trends", use_column_width=True)

