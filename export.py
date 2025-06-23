import sqlite3
import pandas as pd

def export_to_csv():
    conn = sqlite3.connect('usage_data.db')
    df = pd.read_sql_query("SELECT * FROM usage", conn)
    df.to_csv("app_usage_report.csv", index=False)
    conn.close()
    print("Exported to app_usage_report.csv")

export_to_csv()
