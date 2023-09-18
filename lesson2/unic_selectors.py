from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"  # passed
    # "http://suninjuly.github.io/registration2.html"  # failed
    # browser = webdriver.Firefox() eсли у вас Firefox Browser
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(link)

    # Locators
    FRST_NM = "(//input[@class='form-control first'])[1]"
    LST_NM = "(//input[@class='form-control second'])[1]"
    EML = "(//input[@class='form-control third'])[1]"
    PHN = "(//input[@class='form-control first'])[2]"
    # ADRSS = "(//input[@class='form-control second'])[2]"
    SBMT_BTN = "button.btn"
    WLCM_TXT = "h1"

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, FRST_NM)
    input1.clear()
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, LST_NM)
    input2.clear()
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, EML)
    input3.clear()
    input3.send_keys("ddd@dd.ddd")
    input4 = browser.find_element(By.XPATH, PHN)
    input4.clear()
    input4.send_keys("4074354433")
    # input5 = browser.find_element(By.XPATH, ADRSS)
    # input5.clear()
    # input5.send_keys("Moscow")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, SBMT_BTN)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    expected_text = "Congratulations! You have successfully registered!"
    welcome_text_elt = browser.find_element(By.TAG_NAME, WLCM_TXT)
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert (
        expected_text == welcome_text
    ), f'Expected "{expected_text}" but got "{welcome_text}"'

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
