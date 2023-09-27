from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


class TestClass(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Firefox()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'first name')]"
        ).send_keys("Vypiem")
        input2 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'last name')]"
        ).send_keys("Za Lyubov")
        input3 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'email')]"
        ).send_keys("vypiem@gmail.com")
        input4 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'phone')]"
        ).send_keys("88005353535")
        input5 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'address')]"
        ).send_keys("World")
        time.sleep(1)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()

        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text, "WRONG"
        )

    def test_reg2(self):
        browser = webdriver.Firefox()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'your name')]"
        ).send_keys("Vypiem")
        input2 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'last name')]"
        ).send_keys("Za Lyubov")
        input3 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'email')]"
        ).send_keys("vypiem@gmail.com")
        input4 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'phone')]"
        ).send_keys("88005353535")
        input5 = browser.find_element(
            By.XPATH, "//input[contains(@placeholder,'address')]"
        ).send_keys("World")
        time.sleep(1)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        browser.quit()

        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text, "WRONG"
        )


if __name__ == "__main__":
    unittest.main()
