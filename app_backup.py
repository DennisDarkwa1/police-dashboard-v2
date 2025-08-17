import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Police Dashboard v2", layout="wide")

# ---------- Paths ----------
BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
HERO_IMG  = BASE_DIR / "IMG_2429.jpeg"

files = {
    "crime_type":    PLOTS_DIR / "Crime_type.png",
    "top10_loc_1":   PLOTS_DIR / "Top_10_crime_location_1.png",  # updated filename
    "heatmap":       PLOTS_DIR / "heatmap.png",
    "monthly":       PLOTS_DIR / "Monthly_crime.png",
    "seasonal":      PLOTS_DIR / "seasonal_crime.png",
    "ts_count":      PLOTS_DIR / "Time_series_crime_count.png",
    "monthly_count": PLOTS_DIR / "Monthly_crime_count.png",
    "forecast":      PLOTS_DIR / "Crime_forecast.png",
}

# ---------- Plot descriptions (used as captions) ----------
desc = {
    "forecast":      "Crime in Northern Ireland is forecasted to rise in the next six months, highlighting the need for proactive policing",
    "seasonal":      "Crime peaks in summer and drops in winter, showing strong seasonal patterns",
    "crime_type":    "Anti-social behavior and violent offences dominate crime in Northern Ireland, while robbery and theft are least common",
    "top10_loc_1":   "Main Street leads as the top crime hotspot, followed by High Street and Antrim Road",
    "heatmap":       "Urban centers like Belfast and Derry show the highest crime concentration, while rural areas remain relatively low",
    "monthly_count": "Crime levels dipped in early 2023 but have since risen back towards previous highs",
    "monthly":       "Crime peaked in late 2022, dipped early 2023, and has since risen again",
    "ts_count":      "Anti-social behavior and violent offences dominate monthly crime trends, while robbery and weapons offences remain low",
}

# ---------- Sidebar controls (make it lively) ----------
st.sidebar.title("🎛️ Controls")
presenter_mode = st.sidebar.toggle("Presenter mode", value=False, help="Big visuals + Next/Prev navigation")
show_desc      = st.sidebar.toggle("Show descriptions", value=True)
layout_choice  = st.sidebar.radio("Layout", ["2-column grid", "1-column focus"], help="Affects tabs 2 & 3")
img_width      = st.sidebar.slider("Image max width (px)", 500, 1400, 1000, help="If using 1-column focus")
st.sidebar.caption("Tip: Toggle Presenter mode during your talk.")

# Toast once when presenter mode turns on
if presenter_mode and not st.session_state.get("presenter_toast_shown"):
    st.toast("🎤 Presenter mode ON")
    st.session_state["presenter_toast_shown"] = True
if not presenter_mode:
    st.session_state["presenter_toast_shown"] = False

def safe_image(path: Path, key: str, caption_key: str | None = None):
    """Render an image safely with optional caption and width control."""
    if not path.exists():
        st.warning(f"Missing file: `{path.name}` (expected at {path})")
        return
    if layout_choice == "1-column focus" or presenter_mode:
        st.image(str(path), use_container_width=False, width=img_width)
    else:
        st.image(str(path), use_container_width=True)
    if show_desc and caption_key:
        st.caption(desc.get(caption_key, ""))

# ---------- Title ----------
st.title("🚓 POLICE SERVICE NORTHERN IRELAND")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["Most Common Crime", "Current Trends", "6-Month Forecast"])

# ---------- Tab 1 ----------
with tab1:
    st.subheader("Anti-social Behaviour — Most Recorded Category")
    st.markdown(
        """
**Summary**
- Anti-social behaviour appears as the **most common** recorded crime category in the dataset.
- This typically spans noise complaints, public disorder, harassment, and related nuisance reports.
        """
    )
    safe_image(HERO_IMG, key="hero")  # no caption

# ---------- Helpers for interactive “slides” ----------
def slide_navigator(state_key: str, items: list[str], title_map: dict[str, str]):
    """Show Next/Prev buttons to move through selected plots like slides."""
    idx = st.session_state.get(state_key, 0)
    col_prev, col_idx, col_next = st.columns([1,2,1])
    with col_prev:
        if st.button("◀ Prev", use_container_width=True, key=f"{state_key}_prev"):
            idx = (idx - 1) % len(items)
    with col_idx:
        st.markdown(f"<div style='text-align:center;'>Slide {idx+1} / {len(items)} — <b>{title_map[items[idx]]}</b></div>", unsafe_allow_html=True)
    with col_next:
        if st.button("Next ▶", use_container_width=True, key=f"{state_key}_next"):
            idx = (idx + 1) % len(items)
    st.session_state[state_key] = idx
    return items[idx]

# ---------- Tab 2: Current Trends (interactive) ----------
with tab2:
    st.subheader("Current Trends")

    # Let presenter choose which plots to show & order
    available_trends = {
        "crime_type": "Crime Type Distribution",
        "top10_loc_1": "Top 10 Crime Locations",
        "heatmap": "Crime Heatmap",
        "monthly": "Monthly Crime Count",
        "seasonal": "Seasonal Crime Pattern",
        "ts_count": "Time Series — Crime Count",
    }
    default_order = ["crime_type", "top10_loc_1", "heatmap", "monthly", "seasonal", "ts_count"]

    selected = st.multiselect(
        "Choose plots to display",
        options=list(available_trends.keys()),
        default=default_order,
        format_func=lambda k: available_trends[k],
        help="Add/remove plots for your story"
    )

    if presenter_mode and selected:
        # Slide deck style
        current_key = slide_navigator("trends_slide_idx", selected, available_trends)
        safe_image(files[current_key], key=f"trends_{current_key}", caption_key=current_key)
    else:
        # Grid or single column
        if layout_choice == "1-column focus":
            for k in selected:
                safe_image(files[k], key=f"trends_{k}", caption_key=k)
                st.divider()
        else:
            # 2-column grid
            rows = [selected[i:i+2] for i in range(0, len(selected), 2)]
            for r in rows:
                c1, c2 = st.columns(2)
                with c1:
                    safe_image(files[r[0]], key=f"trends_{r[0]}", caption_key=r[0])
                if len(r) > 1:
                    with c2:
                        safe_image(files[r[1]], key=f"trends_{r[1]}", caption_key=r[1])

# ---------- Tab 3: Forecast (interactive) ----------
with tab3:
    st.subheader("Forecast — Next 6 Months")
    st.markdown("Projection based on recent monthly trends.")

    forecast_keys = ["monthly_count", "forecast"]
    titles_map = {
        "monthly_count": "Monthly Crime Count (Historical)",
        "forecast": "Forecasted Crime (Next 6 Months)",
    }

    if presenter_mode:
        current_key = slide_navigator("forecast_slide_idx", forecast_keys, titles_map)
        safe_image(files[current_key], key=f"forecast_{current_key}", caption_key=current_key)
    else:
        if layout_choice == "1-column focus":
            for k in forecast_keys:
                safe_image(files[k], key=f"forecast_{k}", caption_key=k)
                st.divider()
        else:
            c1, c2 = st.columns(2)
            with c1:
                safe_image(files["monthly_count"], key="forecast_monthly_count", caption_key="monthly_count")
            with c2:
                safe_image(files["forecast"], key="forecast_forecast", caption_key="forecast")

