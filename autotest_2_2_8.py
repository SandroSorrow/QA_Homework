import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lastname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("ivanpetrov@umail.su")

    file_in = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_input.txt')
    file_in.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
