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


if __name__ == "__main__":
    run_test()