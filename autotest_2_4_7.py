from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, "book")))
    good_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    if good_price:
        button.click()

    value = browser.find_element(By.ID, "input_value")
    x = value.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    qa = input('Press any key: ')
    browser.quit()
