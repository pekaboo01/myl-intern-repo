from pywinauto import Desktop, Application
import time

# Launch Notepad (Windows 11 modern version)
app = Application(backend="uia").start("notepad.exe")
time.sleep(2)  # give it a moment to open

# Connect to Notepad 
top_win = Desktop(backend="uia").window(title_re=".*Notepad.*")
editor = top_win.child_window(control_type="Document")
time.sleep(2)

# Make sure Notepad is focused
top_win.set_focus()

# Type text
editor.type_keys("Hello, Pywinauto! Simple version works.", with_spaces=True, set_foreground=True)
time.sleep(5)

# Close Notepad 
top_win.close()