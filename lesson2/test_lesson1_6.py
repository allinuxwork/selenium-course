from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
    browser = webdriver.Firefox()
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    fields = browser.find_elements(By.TAG_NAME, "input")
    for field in fields:
        if field.get_attribute("required"):
            field.send_keys("Pasha")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sleep(5)
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


test()
