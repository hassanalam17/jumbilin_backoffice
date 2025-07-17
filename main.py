from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

###Login Page
driver = webdriver.Chrome()
driver.get("https://jumbilin-portal-react-bdgpajdybzdab6d6.eastus-01.azurewebsites.net/login")
email= driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div/input').send_keys("gkplainfield@gmail.com")
password= driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[3]/div/div/input').send_keys("Liverpoolfc23@")
driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[4]/button').click()
time.sleep(15)

###Sidebar menu Kiosk
wait = WebDriverWait(driver, 10)
dropdown_icon = wait.until(EC.element_to_be_clickable((
By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div/ul/li[1]')

))
dropdown_icon.click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/div/div/ul/li[1]/details/ul/li[1]').click()


input("Press Enter to quit...")
driver.quit()
