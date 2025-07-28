import streamlit as st
from PIL import Image
import os

def load_image(name):
    return Image.open(os.path.join("plots", name))

st.set_page_config(page_title="POLICE SERVICE NORTHERN IRELAND", layout="wide")

st.title("🚔 POLICE SERVICE NORTHERN IRELAND")

tab_descriptive, tab_forecast = st.tabs(["📊 Descriptive Analysis", "📈 Forecast for Six Months"])

with tab_descriptive:
    st.header("Descriptive Analysis")
    
    st.image(load_image("Monthly_crime.png"), caption="Monthly Crime Overview")
    st.markdown("Shows total reported crimes per month to understand general crime frequency over time.")
    
    st.image(load_image("Crime_type.png"), caption="Types of Crimes")
    st.markdown("Illustrates distribution of various crime types to identify dominant offenses.")
    
    st.image(load_image("seasonal_crime.png"), caption="Seasonal Crime Patterns")
    st.markdown("Displays how crime rates fluctuate with seasons, helping anticipate trends throughout the year.")
    
    st.image(load_image("Time_series_crime_count.png"), caption="Time Series of Crime Counts")
    st.markdown("Reveals how total crime counts have changed over time, capturing trends and patterns.")
    
    st.image(load_image("heatmap.png"), caption="Crime Heatmap")
    st.markdown("Heatmap showing crime hotspots based on geographic concentration of incidents.")
    
    st.image(load_image("Top_10_crime_location.png"), caption="Top 10 Crime-Prone Locations")
    st.markdown("Highlights the top 10 locations with the highest number of reported crimes.")

with tab_forecast:
    st.header("Forecast for Six Months")
    
    st.image(load_image("Monthly_crime_count.png"), caption="Crime Count by Month")
    st.markdown("Visual summary of crime counts per month to support forecasting analysis.")
    
    st.image(load_image("Crime_forecast.png"), caption="Six-Month Crime Forecast")
    st.markdown("Forecasted crime trends over the next six months based on predictive time series modeling.")

