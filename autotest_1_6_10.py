import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
    lastname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
    email.send_keys("ivanpetrov@umail.su")
    phone = browser.find_element(By.CSS_SELECTOR, '.second_block input.first')
    phone.send_keys("+7(123)456-78-90")
    address = browser.find_element(By.CSS_SELECTOR, '.second_block input.second')
    address.send_keys("Russia, Smolensk, Lenin str., 12, 25")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
