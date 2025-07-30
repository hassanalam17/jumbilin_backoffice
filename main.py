from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Start Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jumbilin-portal-react-bdgpajdybzdab6d6.eastus-01.azurewebsites.net/login")
driver.maximize_window()

# ✅ Login credentials
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div/input').send_keys("gkplainfield@gmail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[3]/div/div/input').send_keys("Liverpoolfc23@")
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[4]/button').click()
time.sleep(10)

# ✅ Navigate to Manage Kiosk
driver.get("https://jumbilin-portal-react-bdgpajdybzdab6d6.eastus-01.azurewebsites.net/manage-kiosk")
time.sleep(5)

# ✅ Upload Logo Image
image_path = r"C:\Users\HP\Downloads\2025-04-08T10_20_04.005Z.png"

upload_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
)
upload_input.send_keys(image_path)
time.sleep(2)

# ✅ Click "Set Up Theme" button
setup_theme_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/button'))
)
setup_theme_button.click()

# ✅ Wait and quit browser
time.sleep(5)
driver.quit()

