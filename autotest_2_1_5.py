import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.ID, "input_value")
    x = x_elem.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robotbox = browser.find_element(By.ID, "robotCheckbox")
    robotbox.click()

    robotrule = browser.find_element(By.ID, "robotsRule")
    robotrule.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    a = input("Press any key: ")
    browser.quit()

