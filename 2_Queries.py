import streamlit as st
import pymysql
import pandas as pd

st.set_page_config(page_title="Asteroid SQL Explorer", layout="wide")

# Orbitron Title + Space Theme
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
    
    <h1>🚀 Asteroid SQL Query Explorer</h1>
""", unsafe_allow_html=True)

# Database connection
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='nasa_project'
    )

conn = get_connection()

# Predefined Queries
def query_dict():
    return {
        "Count how many times each asteroid has approached Earth":
        "SELECT name, COUNT(*) AS approach_count FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id GROUP BY name",

        "Average velocity of each asteroid over multiple approaches":
        "SELECT name, AVG(relative_velocity_kmph) AS avg_velocity FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id GROUP BY name",

        "List top 10 fastest asteroids":
        "SELECT name, relative_velocity_kmph FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id ORDER BY relative_velocity_kmph DESC LIMIT 10",

        "Find potentially hazardous asteroids that have approached Earth more than 3 times":
        "SELECT name, COUNT(*) AS total_approaches FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id WHERE is_potentially_hazardous_asteroid = 1 GROUP BY name HAVING total_approaches > 3",

        "Find the month with the most asteroid approaches":
        "SELECT MONTH(close_approach_date) AS month, COUNT(*) AS approaches FROM close_approach GROUP BY month ORDER BY approaches DESC LIMIT 1",

        "Get the asteroid with the fastest ever approach speed":
        "SELECT name, relative_velocity_kmph FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id ORDER BY relative_velocity_kmph DESC LIMIT 1",

        "Sort asteroids by maximum estimated diameter (descending)":
        "SELECT name, estimated_diameter_max_km FROM asteroids ORDER BY estimated_diameter_max_km DESC",

        "Asteroid whose closest approach is getting nearer over time":
        "SELECT name, close_approach_date, miss_distance_km FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id ORDER BY name, close_approach_date ASC",

        "Display name + date + miss distance of closest approach to Earth":
        "SELECT name, close_approach_date, miss_distance_km FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id ORDER BY miss_distance_km ASC LIMIT 1",

        "List names of asteroids that approached with velocity > 50,000 km/h":
        "SELECT name, relative_velocity_kmph FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id WHERE relative_velocity_kmph > 50000",

        "Count how many approaches happened per month":
        "SELECT MONTH(close_approach_date) AS month, COUNT(*) AS count FROM close_approach GROUP BY month",

        "Find asteroid with highest brightness (lowest magnitude value)":
        "SELECT name, absolute_magnitude_h FROM asteroids ORDER BY absolute_magnitude_h ASC LIMIT 1",

        "Count hazardous vs non-hazardous asteroids":
        "SELECT is_potentially_hazardous_asteroid, COUNT(*) as count FROM asteroids GROUP BY is_potentially_hazardous_asteroid",

        "Asteroids that passed closer than the Moon (less than 1 LD)":
        "SELECT name, close_approach_date, miss_distance_lunar FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id WHERE miss_distance_lunar < 1",

        "Asteroids that came within 0.05 AU":
        "SELECT name, close_approach_date, astronomical FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id WHERE astronomical < 0.05"
    }

extra_queries = {
    "Number of unique asteroids tracked":
    "SELECT COUNT(DISTINCT id) AS unique_asteroids FROM asteroids",

    "Hazardous asteroids with very close approach (< 0.01 AU)":
    "SELECT name, close_approach_date, astronomical FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id WHERE is_potentially_hazardous_asteroid = 1 AND astronomical < 0.01",
    "Top 5 asteroids with largest size range (max - min diameter)":
    "SELECT name, (estimated_diameter_max_km - estimated_diameter_min_km) AS size_range FROM asteroids ORDER BY size_range DESC LIMIT 5",

    "Average miss distance for hazardous asteroids":
    "SELECT AVG(miss_distance_km) AS avg_miss_distance FROM close_approach c JOIN asteroids a ON a.id = c.neo_reference_id WHERE is_potentially_hazardous_asteroid = 1",

    "Most frequent orbiting body (besides Earth)":
    "SELECT orbiting_body, COUNT(*) as count FROM close_approach GROUP BY orbiting_body ORDER BY count DESC LIMIT 3"
}

st.markdown("<h3 style='text-align: center;'>📋 Run Predefined SQL Queries Below</h3>", unsafe_allow_html=True)
main_choice = st.selectbox("Choose a query:", list(query_dict().keys()))
if st.button("Run Main Query"):
    df = pd.read_sql(query_dict()[main_choice], conn)
    st.dataframe(df)

st.markdown("---")
st.markdown("<h4>✨ Bonus Insights</h4>", unsafe_allow_html=True)
extra_choice = st.selectbox("Select an extra query:", list(extra_queries.keys()))
if st.button("Run Extra Query"):
    df = pd.read_sql(extra_queries[extra_choice], conn)
    st.dataframe(df)

