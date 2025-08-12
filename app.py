import streamlit as st
import os
from PIL import Image

# Path to your plots folder (adjust if necessary)
PLOTS_FOLDER = os.path.expanduser("~/Desktop/police-dashboard")

# Function to load images
def load_image(filename):
    return Image.open(os.path.join(PLOTS_FOLDER, filename))

# App title
st.set_page_config(page_title="POLICE SERVICE NORTHERN IRELAND", layout="wide")
st.title("POLICE SERVICE NORTHERN IRELAND")

# Tabs
tab1, tab2, tab3 = st.tabs(["📌 Introduction", "📊 Descriptive Analysis", "📈 Forecast for Next Six Months"])

# ---------------- Tab 1: Introduction ----------------
with tab1:
    st.subheader("Anti-Social Behaviour: The Most Reported Crime")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Police_arrest_UK.jpg/640px-Police_arrest_UK.jpg",
        caption="UK Police arresting a suspect for anti-social behaviour",
        use_container_width=True
    )
    st.markdown("""
    Anti-social behaviour is the **most frequently recorded crime** in the dataset, 
    making up a significant portion of all reported incidents.
    This category includes harassment, vandalism, intimidation, and other acts 
    that disrupt public peace and safety.
    
    The following dashboard provides detailed insights into crime patterns in Northern Ireland.
    """)

# ---------------- Tab 2: Descriptive Analysis ----------------
with tab2:
    st.subheader("Crime Insights Overview")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(load_image("Crime_type.png"), caption="Crime Types Distribution", use_container_width=True)
    with col2:
        st.image(load_image("Top_10_crime_location.png"), caption="Top 10 Crime Locations", use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image(load_image("Monthly_crime.png"), caption="Monthly Crime Trend", use_container_width=True)
    with col4:
        st.image(load_image("heatmap.png"), caption="Crime Heatmap (Seasonality)", use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        st.image(load_image("seasonal_crime.png"), caption="Seasonal Crime Trends", use_container_width=True)
    with col6:
        st.image(load_image("Time_series_crime_count.png"), caption="Crime Counts Over Time", use_container_width=True)

# ---------------- Tab 3: Forecast ----------------
with tab3:
    st.subheader("Crime Forecast for the Next Six Months")

    col1, col2 = st.columns(2)
    with col1:
        st.image(load_image("Monthly_crime_count.png"), caption="Monthly Crime Counts", use_container_width=True)
    with col2:
        st.image(load_image("Crime_forecast.png"), caption="Forecasted Crime Trends", use_container_width=True)

    st.markdown("""
    The forecast model predicts crime trends for the next **six months**.
    It is based on historical data patterns and seasonality effects, 
    helping to anticipate potential spikes in incidents.
    """)


