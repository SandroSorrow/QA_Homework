import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTest(unittest.TestCase):
    def test_registration1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        firstname = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        firstname.send_keys("Ivan")
        lastname = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        lastname.send_keys("Petrov")
        email = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        email.send_keys("ivanpetrov@umail.su")
        phone = self.browser.find_element(By.CSS_SELECTOR, '.second_block input.first')
        phone.send_keys("+7(123)456-78-90")
        address = self.browser.find_element(By.CSS_SELECTOR, '.second_block input.second')
        address.send_keys("Russia, Smolensk, Lenin str., 12, 25")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.CSS_SELECTOR, ".bg-light .container h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "unlucky_2")

        self.browser.quit()

    def test_registration2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

        firstname = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        firstname.send_keys("Ivan")
        lastname = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        lastname.send_keys("Petrov")
        email = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        email.send_keys("ivanpetrov@umail.su")
        phone = self.browser.find_element(By.CSS_SELECTOR, '.second_block input.first')
        phone.send_keys("+7(123)456-78-90")
        address = self.browser.find_element(By.CSS_SELECTOR, '.second_block input.second')
        address.send_keys("Russia, Smolensk, Lenin str., 12, 25")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.CSS_SELECTOR, ".bg-light .container h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "unlucky_2")

        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

