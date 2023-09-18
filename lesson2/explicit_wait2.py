import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Firefox() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # неявное ожидание для всех find element
    # browser.implicitly_wait(5)
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    # button = WebDriverWait(browser, 5).until_not(
    #         EC.element_to_be_clickable((By.ID, "verify"))
    #     )
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    # answer = (
    #     browser.switch_to.alert.text.split()
    # )  # метод сплит разделяет строку на множество и сохраняет в массив
    # print(answer[-1])
    time.sleep(4)
    browser.quit()
