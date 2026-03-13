import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from logger_setup import setup_logger

logger = setup_logger()

# Retry logic to connect to edge via devtools
def connect_webview(max_retries=5, delay=2, debug_address="127.0.0.1:9222"):
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", debug_address)

    for attempt in range(1, max_retries + 1):
        try:
            driver = webdriver.Edge(options=options)
            logger.info(f"[WebView] Connected on attempt {attempt}")
            return driver
        except WebDriverException as e:
            logger.warning(f"[WebView] Retry {attempt} failed: {e}")
            time.sleep(delay)

    raise Exception(f"[WebView] Could not connect after {max_retries} attempts")