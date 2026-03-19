# notepad_page.py
import time
from pywinauto.application import Application
from logger_setup import setup_logger
from screenshot_helper import capture_screenshot

logger = setup_logger()

class NotepadPage:
    def __init__(self, app_path="notepad.exe"):
        self.app_path = app_path
        self.app = None
        self.window = None
        self.editor = None

    def launch(self):
        # launch notepad
        logger.info("Launching Notepad")
        Application(backend="uia").start(self.app_path)
        time.sleep(2)

        # connect to notepad
        logger.info("Connecting to Notepad")
        self.app = Application(backend="uia").connect(title_re=".*Notepad")
        self.window = self.app.window(title_re=".*Notepad")

        # waits for the window to be visible
        logger.info("Waiting for window")
        self.window.wait("visible enabled ready", timeout=30)

        # locates the document editor
        self.editor = self.window.child_window(control_type="Document")

    def type_text(self, text):
        if not self.editor:
            raise RuntimeError("Editor not initialized")
        self.editor.type_keys(text, with_spaces=True)
        logger.info("Typing completed")

    def capture_screenshot(self):
        if self.window:
            capture_screenshot(self.window)