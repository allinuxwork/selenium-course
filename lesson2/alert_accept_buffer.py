from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    form = browser.find_element(By.ID, "answer")
    form.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to.alert

    # Берет ответ и отображает в терминале
    answer = (
        browser.switch_to.alert.text.split()
    )  # метод сплит разделяет строку на множество и сохраняет в массив
    print(answer[-1])

finally:
    browser.quit()
