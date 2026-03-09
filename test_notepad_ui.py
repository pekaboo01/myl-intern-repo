from pywinauto import Application

app = Application(backend="uia").start("notepad.exe")
window = app.window(title="Untitled - Notepad")

window.wait("visible")