1. What are the key principles of maintainable E2E test code?

The key principles of maintainable E2E test code include readability, reusability, separation of concerns, robustness, and proper verification. A test should be easy to read so anyone can understand what it does. Actions that are repeated in multiple tests, such as launching an application or typing text, should be reusable. The test logic should be separated from the UI interaction code to make it easier to maintain. The test should handle errors gracefully, providing logs and screenshots for debugging. Finally, a maintainable test should verify the expected outcome, such as checking that text was correctly typed into Notepad.

2. How does the Page Object Model (POM) improve test readability?

The Page Object Model improves readability by moving all the UI interaction logic into a separate class. In my refactored Notepad test, the NotepadPage class contains the methods for launching Notepad, connecting to its window, locating the editor, typing text, and capturing screenshots. This allows the test file to focus only on the scenario, calling high-level methods like launch() and type_text(), without worrying about the low-level Pywinauto details. As a result, the test reads almost like plain English and is much easier to understand.

3. Why should repetitive actions (like login steps) be moved to reusable helpers?

Repetitive actions should be moved to reusable helpers to avoid duplicating code and to make maintenance simpler. In my test, actions like launching Notepad and typing text are encapsulated in the NotepadPage POM. If the way Notepad is launched or typed into changes in the future, I only need to update the POM class instead of every test. This also keeps the test file focused on the actual scenario being tested rather than the mechanics of interacting with the UI.

4. How can a well-structured test suite speed up debugging and test writing?

A well-structured test suite speeds up debugging and test writing because it separates the test logic from UI interaction. When a test fails, it is easier to identify whether the failure is caused by the test itself or by changes in the application. Reusable methods reduce the amount of new code that needs to be written for additional tests, and logging with screenshots helps quickly identify issues. This structure makes tests easier to maintain, quicker to write, and less prone to errors.

5. Which file did I refactor and what changed?

I selected the file test_app.py for refactoring, Originally, it contained everything in one file: launching Notepad, connecting to the window, waiting, locating the editor, typing text with retries, logging, and screenshot capture. The test was functional but not structured for maintainability or reuse:

import time
from pywinauto.application import Application
from pywinauto import timings
from logger_setup import setup_logger
from screenshot_helper import capture_screenshot

logger = setup_logger()

timings.Timings.window_find_timeout = 20

def run_test():
window = None

    try:

        # Launching notepad
        logger.info("Launching Notepad")
        Application(backend="uia").start("notepad.exe")
        time.sleep(2) # Wait for notepad to appear

        # Connect to notepad
        logger.info("Connecting to Notepad")
        app = Application(backend="uia").connect(title_re=".*Notepad")
        window = app.window(title_re=".*Notepad")

        # Wait for window to be ready
        logger.info("Waiting for window")
        window.wait("visible enabled ready", timeout=30)

        # Locating the notepad editor
        logger.info("Locating document editor")
        editor = window.child_window(control_type="Document")
        editor.wait("visible", timeout=10)

        logger.info("Typing text...")
        for attempt in range(3):

            try:
                editor.type_keys("Hello automated testing!", with_spaces=True)
                break
            except Exception:
                logger.warning("Retry typing text")
                time.sleep(2)

        logger.info("Typing completed")

    except Exception as e:
        logger.error(f"Test failed: {e}")
        if window:
            capture_screenshot(window)

        raise

if **name** == "**main**":
run_test()

After refactoring, I created two new files:

_notepad_page.py_ - This file implements the Page Object Model for Notepad. It contains a NotepadPage class with methods to launch Notepad, connect to its window, locate the editor, type text, and capture screenshots. This file isolates all UI-specific code from the test logic.

# notepad_page.py

import time
from pywinauto.application import Application
from logger_setup import setup_logger
from screenshot_helper import capture_screenshot

logger = setup_logger()

class NotepadPage:
def **init**(self, app_path="notepad.exe"):
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

_test_notepad_typing.py_ - This file contains the actual test scenario. It imports the NotepadPage class and calls its methods to launch Notepad, type text, and verify that the text was correctly typed. It also includes a try/except block to log errors and capture screenshots in case of failure.

from notepad_page import NotepadPage
from logger_setup import setup_logger
import time

logger = setup_logger()

def run_notepad_test():
notepad = NotepadPage()
try:
notepad.launch()
time.sleep(1)  
 notepad.type_text("Refactored with POM for Maintainability!")
time.sleep(1)

        # verifies if the text are entered correctly
        typed_text = notepad.editor.window_text()
        assert "Refactored with POM for Maintainability!" in typed_text, "Text not typed correctly"

        logger.info("Text verified successfully!")

    except Exception as e:
        logger.error(f"Test failed: {e}")
        notepad.capture_screenshot()
        raise

if **name** == "**main**":
run_notepad_test()

With this refactoring, the test file is short, readable, and focused on the scenario, while the POM handles all the UI logic.
The test also includes verification that the expected text appears in the editor, making it a complete E2E test. In addition, the design makes it easy to reuse Notepad actions in other tests and keeps the code maintainable.
