import sqlite3
import pandas as pd
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Setup theme
ctk.set_appearance_mode("System")  # for example use "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")

# Main App
app = ctk.CTk()
app.title("🖥 PC Usage Tracker Dashboard")
app.geometry("900x800")

# --- Fetch Usage Data ---
def fetch_data():
    conn = sqlite3.connect("usage_data.db")
    df = pd.read_sql_query("SELECT app_name, SUM(duration) as total_duration FROM usage GROUP BY app_name", conn)
    conn.close()
    return df

# --- Update Table and Chart ---
def update_view():
    # Clear table frame
    for widget in table_frame.winfo_children():
        widget.destroy()

    df = fetch_data()
    total_time = 0

    header = ctk.CTkLabel(table_frame, text=f"{'App Name':<30}{'Time Used':>15}", font=ctk.CTkFont(size=14, weight="bold"))
    header.pack(anchor="w", padx=15, pady=4)

    for index, row in df.iterrows():
        app_name = row["app_name"]
        duration = int(row["total_duration"])
        total_time += duration
        mins, secs = divmod(duration, 60)
        line = f"{app_name:<30}{mins}m {secs}s"
        label = ctk.CTkLabel(table_frame, text=line, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", padx=10)

    total_label.configure(text=f"Total Usage Time: {total_time // 60}m {total_time % 60}s")

    plot_chart(df)

# --- Plot Chart in Frame ---
def plot_chart(df):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(6.5, 3), dpi=100)
    ax = fig.add_subplot(111)

    apps = df["app_name"]
    durations = df["total_duration"] // 60  # convert to minutes

    ax.bar(apps, durations, color="#1f77b4")
    ax.set_title("Time Spent per Application (in minutes)", fontsize=12)
    ax.set_xlabel("Applications")
    ax.set_ylabel("Minutes")
    ax.tick_params(axis='x', rotation=45)

    chart = FigureCanvasTkAgg(fig, master=chart_frame)
    chart.draw()
    chart.get_tk_widget().pack(fill='both', expand=True)

# --- GUI Elements ---

# Title
title = ctk.CTkLabel(app, text="📊 PC Usage Tracker Dashboard", font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=20)

# Table frame
table_frame = ctk.CTkScrollableFrame(app, width=650, height=180)
table_frame.pack(pady=10)

# Total usage label
total_label = ctk.CTkLabel(app, text="Total Usage Time: --", font=ctk.CTkFont(size=14, weight="bold"))
total_label.pack(pady=5)

# Refresh button
refresh_btn = ctk.CTkButton(app, text="🔄 Refresh", command=update_view)
refresh_btn.pack(pady=5)

# Chart Frame
chart_frame = ctk.CTkFrame(app, width=650, height=150, corner_radius=20)
chart_frame.pack(pady=10, fill="both", expand=True)

# Load view
update_view()

# Run App
app.mainloop()
