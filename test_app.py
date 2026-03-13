import time
from pywinauto.application import Application
from pywinauto import timings
from logger_setup import setup_logger
from screenshot_helper import capture_screenshot

logger = setup_logger()

def run_test():
    window = None

    try:
        # Launch Notepad
        logger.info("Launching Notepad")
        Application(backend="uia").start("notepad.exe")
        time.sleep(2)  # wait a little for it to appear

        # Connect to Notepad
        logger.info("Connecting to Notepad")
        app = Application(backend="uia").connect(title_re=".*Notepad")
        window = app.window(title_re=".*Notepad")

        # Wait for window to be ready
        logger.info("Waiting for window")
        try:
            window.wait("visible enabled ready", timeout=10)
        except timings.TimeoutError as e:
            logger.error(f"Window not ready in 10s: {e}")
            capture_screenshot(window)
            raise

        # Locate the Document editor
        logger.info("Locating document editor")
        editor = window.child_window(control_type="InvalidControl")

        # Type text
        logger.info("Typing text into Document control")
        editor.type_keys("Hello automated testing!", with_spaces=True)
        logger.info("Typing completed")

    except Exception as e:
        logger.error(f"Test failed: {e}")
        if window:
            capture_screenshot(window)
        raise


if __name__ == "__main__":
    run_test()