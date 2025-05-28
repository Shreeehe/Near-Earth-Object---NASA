import streamlit as st
import pymysql
import pandas as pd
from datetime import date, datetime
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Asteroid Overview Dashboard", layout="wide")


# Title
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
    <h1 style='font-family: Orbitron, sans-serif; color: #1E90FF; text-align: center;'>
        🚀 Near Earth Objects
    </h1>
""", unsafe_allow_html=True)

# Connect to DB
@st.cache_resource
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='nasa_project'
    )

# Fetch data
@st.cache_data
def get_data():
    conn = get_connection()
    df = pd.read_sql("""
        SELECT a.*, c.close_approach_date, c.relative_velocity_kmph, 
               c.astronomical, c.miss_distance_km, c.miss_distance_lunar, c.orbiting_body
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
    """, conn)
    conn.close()
    return df

asteroids = get_data()
asteroids["close_approach_date"] = pd.to_datetime(asteroids["close_approach_date"])

# Sidebar Filters
st.sidebar.header("🔎 Filter Criteria")
search_id = st.sidebar.text_input("Asteroid ID")

start_date = st.sidebar.date_input("Start Date", date(2024, 1, 1))
end_date = st.sidebar.date_input("End Date", date(2025, 4, 13))

danger = st.sidebar.selectbox("Hazardous Only?", ["Both", "Yes", "No"])

vel_min, vel_max = st.sidebar.slider("Velocity in km/h", 
    float(asteroids["relative_velocity_kmph"].min()), 
    float(asteroids["relative_velocity_kmph"].max()),
    (10000.0, 100000.0))

# Diameter filter
dia_min, dia_max = st.sidebar.slider("Diameter in Km", 
    float(asteroids["estimated_diameter_min_km"].min()), 
    float(asteroids["estimated_diameter_max_km"].max()),
    (0.0, 5.0))

# Logic to filter data
filtered = asteroids[
    (asteroids["close_approach_date"] >= pd.Timestamp(start_date)) &
    (asteroids["close_approach_date"] <= pd.Timestamp(end_date)) &
    (asteroids["relative_velocity_kmph"] >= vel_min) &
    (asteroids["relative_velocity_kmph"] <= vel_max) &
    (asteroids["estimated_diameter_min_km"] >= dia_min) &
    (asteroids["estimated_diameter_max_km"] <= dia_max)
]

if danger == "Yes":
    filtered = filtered[filtered["is_potentially_hazardous_asteroid"] == 1]
elif danger == "No":
    filtered = filtered[filtered["is_potentially_hazardous_asteroid"] == 0]

if search_id:
    filtered = filtered[filtered["id"].astype(str).str.contains(search_id, case=False)]

# Results Table
st.subheader("Filtered Asteroids")
st.dataframe(filtered)

# Footer note
st.markdown("""
    <div style='text-align: center; margin-top: 3em; font-size: 14px; color: gray;'>
        🚀 This Page was created by Shri ✨ :)
    </div>
""", unsafe_allow_html=True)
