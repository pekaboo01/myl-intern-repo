from pywinauto import Application

def test_notepad_launch():
    # Start Notepad
    app = Application(backend="uia").start("notepad.exe")

    # Connect to the running Notepad process (optional but safer)
    app = Application(backend="uia").connect(path="notepad.exe")

    # Grab the top window
    window = app.top_window()

    # Verify it exists
    assert window.exists()

    # Close Notepad
    window.close()