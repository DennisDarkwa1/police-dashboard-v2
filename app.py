import streamlit as st
from PIL import Image
import os

st.title("🚓 Police Crime Data Dashboard")
st.write("Visual insights into crime trends, types, and forecasts.")

# Path to your plot images
plot_folder = "plots"

# Map of display names to image file names
image_files = {
    "Crime Forecast": "Crime_forecast.png",
    "Crime Types": "Crime_type.png",
    "Heatmap": "heatmap.png",
    "Monthly Crime Count": "Monthly_crime_count.png",
    "Monthly Crime Trend": "Monthly_crime.png",
    "Seasonal Crime Pattern": "seasonal_crime.png",
    "Time Series Crime Count": "Time_series_crime_count.png",
    "Top 10 Crime Locations": "Top_10_crime_location.png"
}

# Sidebar for plot selection
selected_plot = st.sidebar.selectbox("📊 Select a plot to view:", list(image_files.keys()))

# Load and display the selected image
image_path = os.path.join(plot_folder, image_files[selected_plot])
image = Image.open(image_path)
st.image(image, caption=selected_plot, use_column_width=True)

