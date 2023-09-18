from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    element1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    element1.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 150)", "")
    button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
