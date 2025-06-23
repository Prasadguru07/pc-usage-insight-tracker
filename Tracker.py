import time
from datetime import datetime
from utils import get_active_window_title
from db import insert_usage, create_db

create_db()

def track_usage():
    last_window = None
    start_time = datetime.now()

    while True:
        current_window = get_active_window_title()

        if current_window != last_window and last_window is not None:
            end_time = datetime.now()
            duration = int((end_time - start_time).total_seconds())
            insert_usage(last_window, str(start_time), str(end_time), duration)
            print(f"Saved: {last_window} - {duration} sec")

            # Reset
            start_time = datetime.now()

        last_window = current_window
        time.sleep(1)  # Check every second

track_usage()
