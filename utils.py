import win32gui

def get_active_window_title():
    window  = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)
print(get_active_window_title())