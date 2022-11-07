import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.ID, "treasure")
    x_val = x_elem.get_attribute("valuex")
    y = calc(x_val)

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

