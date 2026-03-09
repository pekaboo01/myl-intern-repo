from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time

# Connect to Notepad
app = Application(backend="uia").connect(title_re=".*Notepad")
win = app.top_window()

# Type the text
win.child_window(control_type="Document").type_keys(
    "Hello Focus Bear! Automated test.", with_spaces=True, pause=0.05
)

# Save the file
file_path = r"C:\intern\myl-intern-repo\test_output_ui.txt"
send_keys("%(FA)")   # Alt+F → Save As
time.sleep(1)
send_keys(file_path)
send_keys("{ENTER}")