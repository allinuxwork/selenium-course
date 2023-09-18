from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest


def test_b12(self):

    link = "http://suninjuly.github.io/registration1.html"

    try:
        browser = webdriver.Firefox()
        browser.get(link)

        input1 = browser.find_element(
            By.XPATH, "//*[@class='first_block']//input[contains(@class, 'first')]"
        )
        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.XPATH, "//*[@class='first_block']//input[contains(@class, 'second')]"
        )
        input2.send_keys("Petrov")
        input3 = browser.find_element(
            By.XPATH, "//*[@class='first_block']//input[contains(@class, 'third')]"
        )
        input3.send_keys("Smolensk")
        """input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")"""
        button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла


test_b12("self")
