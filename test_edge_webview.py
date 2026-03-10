import time
from subprocess import Popen
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Edge with debug mode
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_file = r"C:\intern\myl-intern-repo\test.html"
user_data_dir = r"C:\intern\edge_test_profile"

Popen([edge_exe, "--remote-debugging-port=9222", f"--user-data-dir={user_data_dir}", html_file])
time.sleep(3)  # give Edge a moment to start

# Connect Selenium to running Edge
msedgedriver_path = r"C:\Users\johnm\Downloads\edgedriver_win64\msedgedriver.exe"
service = Service(msedgedriver_path)
options = webdriver.EdgeOptions()
options.debugger_address = "localhost:9222"

driver = webdriver.Edge(service=service, options=options)
print("[Selenium] Connected to Edge WebView2")

wait = WebDriverWait(driver, 10)

# Wait and click login button
login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
login_button.click()
print("[Selenium] Clicked login button")

# Handle alert
alert = wait.until(EC.alert_is_present())
print("[Selenium] Alert text:", alert.text)
alert.accept()

# Get welcome message
welcome_text = wait.until(EC.presence_of_element_located((By.ID, "welcomeMessage"))).text
print("[Selenium] WebView text:", welcome_text)

# Close browser
driver.quit()
print("[Test] Done")