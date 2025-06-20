import streamlit as st
import pymysql
import pandas as pd
from datetime import date, datetime
import random

st.set_page_config(page_title="Asteroid Insights & Highlights", layout="wide")

# Orbitron Title
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
    <h1 style='font-family: Orbitron, sans-serif; color: #1E90FF; text-align: center;'>
        🌌 Asteroid Insights & Highlights
    </h1>
""", unsafe_allow_html=True)

st.markdown("")

# DB Connection
@st.cache_resource
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='nasa_project'

    )
'Get quick facts, alerts, and curious stats on asteroids zooming by Earth' 
conn = get_connection()

# 1. Asteroid of the Day 
st.subheader("🌟 Asteroid of the Day")
id_query = "SELECT DISTINCT a.id FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id"
id_df = pd.read_sql(id_query, conn)
random_id = random.choice(id_df["id"].tolist())

asteroid_query = f"""
        SELECT * FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE a.id = '{random_id}'
        LIMIT 1
    """
asteroid_day = pd.read_sql(asteroid_query, conn)
st.dataframe(asteroid_day)

# 0. Did You Know? 
st.subheader("🎯 Did You Know?")
trivia = [
    "There are over 1 million known asteroids in our solar system!",
    "Some asteroids have their own moons!",
    "The first asteroid discovered was Ceres in 1801.",
    "Most asteroids are located in the asteroid belt between Mars and Jupiter.",
    "NASA tracks thousands of Near-Earth Objects (NEOs) every day!"
]
st.success(random.choice(trivia))


# 2. quote part
st.subheader("🧠 Space Quote of the Day")
facts = [
    "\"Earth is the cradle of humanity, but one cannot live in a cradle forever.\" — Konstantin Tsiolkovsky",
    "\"The universe is under no obligation to make sense to you.\" — Neil deGrasse Tyson",
    "\"That's one small step for man, one giant leap for mankind.\" — Neil Armstrong",
    "\"Space is not the final frontier. The mind is.\"",
    "\"Somewhere, something incredible is waiting to be known.\" — Carl Sagan"
]
st.info(random.choice(facts))

# 3. footer part
st.markdown("""
    <hr style='margin-top: 3em; margin-bottom: 1em;'>
    <div style='text-align: center; font-size: 14px; color: gray;'>
        🚀 This dashboard was designed & built by <b>Shri</b> for NASA NEO Insights Project 🌠
    </div>
""", unsafe_allow_html=True)

