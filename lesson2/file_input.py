from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# go to main page
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(link)

    # locators
    FRST_NM = "input[type='text'][name='firstname']"
    LST_NM = "input[type='text'][name='lastname']"
    EML = "input[type='text'][name='email']"
    CHS_FL_BTN = "[type='file']"
    SBMT_BTN = "button[type='submit'].btn.btn-primary"

    # send first name to the field
    result = browser.find_element(By.CSS_SELECTOR, FRST_NM)
    result.clear()
    result.send_keys("Ivan")

    # send last name to the field
    result = browser.find_element(By.CSS_SELECTOR, LST_NM)
    result.clear()
    result.send_keys("Ivanov")

    # send email to the field
    result = browser.find_element(By.CSS_SELECTOR, EML)
    result.clear()
    result.send_keys("ddd@ddd.com")

    # upload file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_input.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, CHS_FL_BTN)
    element.send_keys(file_path)

    # submit the form
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
