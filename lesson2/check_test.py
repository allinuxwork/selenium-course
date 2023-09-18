from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# go to main page
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(link)

    # count the number to send as a result
    def calc(x):
        res = math.log(abs(12 * math.sin(int(x))))
        res_rnd = res
        return str(res_rnd)

    # extract the number from the page
    x_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap[id='input_value']")
    x = x_element.text
    y = calc(x)
    # print(type(x), type(y), x, y)

    # send result to the field
    result = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    result.clear()
    result.send_keys(y)

    # mark checkbox "I'm the robot"
    checkbox = browser.find_element(
        By.CSS_SELECTOR, "input#robotCheckbox.form-check-input"
    )
    checkbox.click()

    # mark radio button "Robots rule"
    radio = browser.find_element(By.CSS_SELECTOR, "input#robotsRule.form-check-input")
    radio.click()

    # submit the form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
