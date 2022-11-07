import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name.lower() == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_ufo(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)
    textarea = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
    textarea.send_keys(calc())
    submit = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    submit.click()
    smart_hint = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    assert smart_hint.text == "Correct!", f"FAILED! '{smart_hint.text}'"


def calc():
    return math.log(int(time.time()))
