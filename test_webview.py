import time
import subprocess
from logger_setup import setup_logger
from webview_retry import connect_webview 

logger = setup_logger()

def run_webview_test():
    # 1Launch Edge with remote debugging
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = r"C:\EdgeDebugProfile"

    logger.info("Launching Edge with remote debugging")
    edge_process = subprocess.Popen([
        edge_path,
        "--remote-debugging-port=9222",
        f"--user-data-dir={user_data_dir}",
        "--no-first-run"
    ])
    time.sleep(3)  # Give Edge time to start

    # Connect to WebView using the separate retry module
    logger.info("Connecting to WebView")
    driver = connect_webview(max_retries=5)

    # Example WebView action
    logger.info("Navigating to https://example.com")
    driver.get("https://example.com")
    logger.info(f"Page title: {driver.title}")

    logger.info("Test completed")

if __name__ == "__main__":
    run_webview_test()