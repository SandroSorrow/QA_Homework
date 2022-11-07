import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem_num1 = browser.find_element(By.ID, "num1")
    num1 = int(elem_num1.text)
    elem_num2 = browser.find_element(By.ID, "num2")
    num2 = int(elem_num2.text)

    summ = num1 + num2
    answ = str(summ)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answ)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    a = input("Press any key: ")
    browser.quit()