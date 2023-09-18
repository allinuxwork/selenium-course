from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# go to main page
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(link)

    # locators
    TRSR_BX = "//img[@src='images/chest.png' and @height='40' and @width='40' and @id='treasure']"
    RSLT_FLD = "input#answer[type='text']"
    IM_RBT_CHK_BX = "input.check-input#robotCheckbox"
    RBT_RL = "input.check-input#robotsRule"
    SBMT_BTN = "button.btn.btn-default"

    # extract the number from the page through get_attribute
    trsr_bx = browser.find_element(By.XPATH, TRSR_BX)
    srchd_wrd = trsr_bx.get_attribute("valuex")

    # count the y as product of srchd_wrd and calc(srchd_wrd)
    def calc(srchd_wrd):
        res = math.log(abs(12 * math.sin(int(srchd_wrd))))
        res_rnd = res
        return str(res_rnd)

    y = calc(srchd_wrd)

    # send result to the field
    result = browser.find_element(By.CSS_SELECTOR, RSLT_FLD)
    result.clear()
    result.send_keys(y)
    #
    # mark checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, IM_RBT_CHK_BX)
    checkbox.click()

    # mark radio button "Robots rule"
    radio = browser.find_element(By.CSS_SELECTOR, RBT_RL)
    radio.click()

    # submit the form
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
