from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)

    fbutton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    fbutton.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    sbutton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sbutton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
