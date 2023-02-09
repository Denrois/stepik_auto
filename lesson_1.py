import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviced_obj = Service('*****')
driver = webdriver.Chrome(service=serviced_obj)
driver.get('http://suninjuly.github.io/simple_form_find_task.html')
driver.find_element(By.CSS_SELECTOR, '[name="first_name"]').send_keys('Ivan')
driver.find_element(By.CSS_SELECTOR, '[name="last_name"]').send_keys('Petrov')
driver.find_element(By.CSS_SELECTOR, '.city').send_keys('Smolensk')
driver.find_element(By.CSS_SELECTOR, '#country').send_keys('Russia')
driver.find_element(By.CSS_SELECTOR, '.btn').click()
time.sleep(5)