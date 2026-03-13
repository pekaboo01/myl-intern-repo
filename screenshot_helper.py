from datetime import datetime
from logger_setup import setup_logger

logger = setup_logger()

# Captures window and saves it as an image
def capture_screenshot(window):
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    try:
        img = window.capture_as_image()
        img.save(filename)
        logger.info(f"Screenshot saved: {filename}")
    except Exception as e:
        logger.error(f"Screenshot failed: {e}")