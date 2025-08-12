import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Police Dashboard v2", layout="wide")

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
HERO_IMG = BASE_DIR / "IMG_2429.jpeg"

# Image files in /plots
files = {
    "crime_type": PLOTS_DIR / "Crime_type.png",
    "top10_loc": PLOTS_DIR / "Top_10_crime_location.png",
    "heatmap": PLOTS_DIR / "heatmap.png",
    "monthly": PLOTS_DIR / "Monthly_crime.png",
    "seasonal": PLOTS_DIR / "seasonal_crime.png",
    "ts_count": PLOTS_DIR / "Time_series_crime_count.png",
    "monthly_count": PLOTS_DIR / "Monthly_crime_count.png",
    "forecast": PLOTS_DIR / "Crime_forecast.png",
}

def safe_image(path: Path, caption: str = ""):
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing file: `{path.name}` (expected at {path})")

# --- Dashboard title ---
st.title("🚓 POLICE SERVICE NORTHERN IRELAND")

tab1, tab2, tab3 = st.tabs([
    "Most Common Crime",
    "Descriptive Analysis",
    "6-Month Forecast",
])

# --- Tab 1: Anti-social behaviour as most common ---
with tab1:
    st.subheader("Anti-social Behaviour — Most Recorded Category")
    st.markdown(
        """
**Summary**
- Anti-social behaviour appears as the **most common** recorded crime category in the dataset.
- This typically spans noise complaints, public disorder, harassment, and related nuisance reports.
        """
    )
    safe_image(HERO_IMG)

# --- Tab 2: Descriptive analysis ---
with tab2:
    st.subheader("Descriptive Analysis")

    # Row 1
    c1, c2 = st.columns(2)
    with c1:
        safe_image(files["crime_type"], caption="Crime Type Distribution")
    with c2:
        safe_image(files["top10_loc"], caption="Top 10 Crime Locations")

    # Row 2
    c3, c4 = st.columns(2)
    with c3:
        safe_image(files["heatmap"], caption="Crime Heatmap")
    with c4:
        safe_image(files["monthly"], caption="Monthly Crime Count")

    # Row 3
    c5, c6 = st.columns(2)
    with c5:
        safe_image(files["seasonal"], caption="Seasonal Crime Pattern")
    with c6:
        safe_image(files["ts_count"], caption="Time Series — Crime Count")

# --- Tab 3: Forecast ---
with tab3:
    st.subheader("Forecast — Next 6 Months")
    st.markdown("Projection based on recent monthly trends.")
    c1, c2 = st.columns(2)
    with c1:
        safe_image(files["monthly_count"], caption="Monthly Crime Count (Historical)")
    with c2:
        safe_image(files["forecast"], caption="Forecasted Crime (Next 6 Months)")

