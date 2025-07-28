import streamlit as st
from PIL import Image
import os

def load_image(name):
    return Image.open(os.path.join("plots", name))

# Page Title
st.title("🚔 POLICE SERVICE NORTHERN IRELAND")

# Tabs
tab_descriptive, tab_predictive = st.tabs(["📊 Descriptive Analysis", "📈 Forecast for the Next Six Months"])

with tab_descriptive:
    st.header("Descriptive Analysis")

    st.image(load_image("Monthly_crime.png"), caption="Monthly Crime Overview")
    st.markdown("This plot shows the monthly trend of reported crimes, helping identify peak periods during the year.")
    
    st.image(load_image("Crime_type.png"), caption="Crime Types Distribution")
    st.markdown("Breakdown of crimes by type, showing the proportion of each crime category within the dataset.")
    
    st.image(load_image("seasonal_crime.png"), caption="Seasonal Crime Trends")
    st.markdown("Analysis of seasonal variations in crime, helping anticipate fluctuations throughout the year.")

    st.image(load_image("Time_series_crime_count.png"), caption="Time Series Crime Count")
    st.markdown("A time series plot showing the overall crime count over time for long-term trend analysis.")

    st.image(load_image("heatmap.png"), caption="Crime Heatmap")
    st.markdown("A geographical heatmap highlighting crime hotspots across the region.")

    st.image(load_image("Top_10_crime_location.png"), caption="Top 10 Crime Locations")
    st.markdown("The top 10 locations with the highest crime rates. Useful for targeted intervention strategies.")

with tab_predictive:
    st.header("Forecast for the Next Six Months")

    months = st.slider("Select Forecast Horizon (Months)", min_value=1, max_value=12, value=6)
    st.write(f"Displaying crime forecast for the next {months} month(s).")

    st.image(load_image("Monthly_crime_count.png"), caption="Monthly Crime Count Overview")
    st.markdown("Alternative monthly crime overview used as a baseline comparison for forecast accuracy.")

    st.image(load_image("Crime_forecast.png"), caption="Crime Forecast")
    st.markdown("Forecasted crime counts based on predictive models, projecting trends into the next six months.")

