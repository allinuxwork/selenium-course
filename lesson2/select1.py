from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# go to main page
try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(link)

    # locators
    FRST_NMBR = "span.nowrap#num1"
    SCND_NMBR = "span.nowrap#num2"
    SELCT_MN = "select#dropdown.custom-select"
    SBMT_BTN = "button.btn.btn-default"

    # extract the numbers to be summed from the page
    slct_nm_one = browser.find_element(By.CSS_SELECTOR, FRST_NMBR)
    slct_nm_two = browser.find_element(By.CSS_SELECTOR, SCND_NMBR)
    str_sum_of_two = str(int(slct_nm_one.text) + int(slct_nm_two.text))
    print(str_sum_of_two)

    # to find counted number in drop down menu
    select = Select(browser.find_element(By.CSS_SELECTOR, SELCT_MN))
    select.select_by_value(str_sum_of_two)

    # submit the form with counted number
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
