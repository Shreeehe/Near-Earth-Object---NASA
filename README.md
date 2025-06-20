# 🚀 NASA NEO Tracker — Streamlit Dashboard

A beautifully designed, interactive dashboard to explore Near-Earth Objects (NEOs) using NASA's public data. Built with ❤️ by **Shri**, this app allows users to filter, a nd query asteroid data from a MySQL database.

---

## 🌌 Project Structure

```bash
📁 Near-Earth-Object---NASA/
├── home.py                 # Page 1: Dashboard with filters
├── pages/
│   ├── 2_Queries.py       # Page 2: SQL Query Explorer
│   └── 3_Insights.py      # Page 3: Fun Facts & Highlights
```

---

## ⚙️ Tech Stack

* **Streamlit** — for building interactive UI
* **MySQL** — for storing NEO data
* **Pandas** — for data manipulation
* **Pymysql** — for DB connection
* **Orbitron Font** — for that outer space vibe ✨

---

## 📄 Features

### 🔎 1. Dashboard (home.py)

* Filter asteroids by:

  * Velocity
  * Diameter
  * Date Range
  * Hazardous status
  * Asteroid ID
* Displays filtered results with a header and footer

### 📋 2. SQL Query Explorer (2\_Queries.py)

* Run pre-defined and bonus SQL queries
* Explore patterns like:

  * Fastest asteroids
  * Hazardous close encounters
  * Monthly stats

### 🌠 3. Insights & Highlights (3\_Insights.py)

* "Asteroid of the Day"
* Trivia facts
* Inspirational space quotes

---

## 💾 How to Run

1. Clone this repo
2. Install dependencies:

```bash
pip install streamlit pandas pymysql streamlit-extras
```

3. Set up your MySQL database and name it `nasa_project`
4. Start the app:

```bash
streamlit run home.py
```

---

## ✨ Credits

Dashboard crafted with care by **Shri** 🐾
NEO data inspired by NASA's public API

---

## 📸 Screenshots


### 🛰️ Home Dashboard
![Home](home.PNG)

### 📋 Query Explorer
![Page 2](page%202.PNG)

### 🌌 Insights & Highlights
![Page 3](page%203.PNG)

---

## 🌐 License

MIT — free to use, remix, and expand!

---

> "Somewhere, something incredible is waiting to be known." — Carl Sagan
