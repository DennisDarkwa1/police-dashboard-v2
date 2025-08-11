import streamlit as st
from PIL import Image
import os

# Path to your plots folder
PLOTS_FOLDER = os.path.expanduser("~/Desktop/police-dashboard/plots")

def load_image(filename):
    return Image.open(os.path.join(PLOTS_FOLDER, filename))

# --- Dashboard Title ---
st.set_page_config(page_title="Police Service Northern Ireland", layout="wide")
st.title("🚔 POLICE SERVICE NORTHERN IRELAND")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["👮 Anti-Social Behaviour", "📊 Descriptive Dashboard", "🔮 6-Month Forecast"])

# --- Tab 1: Anti-Social Behaviour ---
with tab1:
    st.subheader("Anti-Social Behaviour: The Most Reported Crime")
    st.image("https://ichef.bbci.co.uk/news/976/cpsprodpb/11E65/production/_125632732_policearrest.jpg", 
             caption="UK Police making an arrest for anti-social behaviour", use_column_width=True)
    st.markdown("""
        **Anti-social behaviour** accounts for the largest proportion of crimes in the dataset.  
        These incidents often include disorderly conduct, vandalism, harassment, and public disturbances.  
        Tackling these offences remains a key priority for the Police Service of Northern Ireland to maintain 
        public safety and community confidence.
    """)

# --- Tab 2: Descriptive Dashboard ---
with tab2:
    st.subheader("Descriptive Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(load_image("seasonal_crime.png"), caption="Seasonal Crime Trends")
        st.image(load_image("Top_10_crime_location.png"), caption="Top 10 Crime Locations")
    
    with col2:
        st.image(load_image("Monthly_crime.png"), caption="Monthly Crime Overview")
        st.image(load_image("Time_series_crime_count.png"), caption="Crime Count Over Time")

# --- Tab 3: Forecast ---
with tab3:
    st.subheader("Crime Forecast: Next Six Months")
    st.image(load_image("Monthly_crime_count.png"), caption="Forecast of Monthly Crime Counts")
    st.markdown("""
        Using time-series analysis, we have forecasted crime trends for the next six months.  
        This helps in resource planning and proactive policing strategies.
    """)

