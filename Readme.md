# 🖥️ PC Usage Insight Tracker

Track, analyze, and visualize how you spend time on your PC — in real-time.  
This project logs active application usage on your Windows machine and displays it via a sleek, modern dashboard built using Dash and Plotly.

---

## 🔍 What This Project Do

- Tracks the currently active window (Chrome, VSCode, etc.)
- Logs start time, end time, and total usage duration in a SQLite database
- Provides a modern dashboard with:
  - App-wise usage summary
  - Interactive bar chart
  - Total usage time
  - Refresh capability

---

## 📁 Project Structure

```bash
PC_usage_tracker/
├── Tracker.py           # Main tracking logic
├── db.py                # SQLite DB logic (create table, insert data)
├── utils.py             # Utility for getting active window title
├── usage_data.db        # SQLite database (auto-created)
├── app.py               # Dash web dashboard with Plotly charts
├── requirements.txt     # List of dependencies
└── README.md            


## 🚀 How to Run PC Usage Insight Tracker

1. Python Tracker.py

✅ Keep this terminal running in the background — it records which application is currently active and logs data into usage_data.db.

2. Python dashboard.py

Reads from usage_data.db → SELECT app_name, SUM(duration) GROUP BY app_name

Converts durations from seconds → minutes

Feeds the data into a Data bar chart

Displays summary and visual chart in browser


## 🔍 The reason to build this project

🧠 Personal Time Awareness: I wanted a tool to track how I really spend time on my PC — not just websites, but all desktop apps like code editors, browsers, tools, etc.

🔧 Hands-On Systems Project: This was a perfect way to apply OS, DBMS, and Python concepts in a real-world use case by building my own system-level activity logger.

📊 Dash + Plotly Visualization: Unlike traditional console-based trackers, I built a modern dashboard using Dash that makes the insights interactive and visually compelling.

🚫 No Third-Party Dependency: Unlike apps like RescueTime, this project is local-first, privacy-safe, lightweight, and doesn’t rely on cloud APIs or tracking services.