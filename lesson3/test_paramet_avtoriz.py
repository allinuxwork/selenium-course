import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# from login_page import *


# Test data
user = " "
password = " "


# Fixture to open and close browser + login
@pytest.fixture(scope="function")
def browser():
    print("Start")
    browser = webdriver.Firefox()
    browser.get("https://stepik.org/catalog?auth=login")
    browser.implicitly_wait(7)
    # Find and fill in email and password fields
    email_field = browser.find_element(By.ID, "id_login_email")
    email_field.send_keys(user)

    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys(password)

    # Find login button on popup
    login_button_on_popup = browser.find_element(
        By.CSS_SELECTOR, ".sign-form__btn.button_with-loader"
    )
    login_button_on_popup.click()
    time.sleep(4)
    print("User logged in")
    yield browser
    browser.quit()
    print("Finish")


@pytest.mark.parametrize(
    "link",
    [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ],
)
def test_open_link_login_calculate_check_result(browser, link):
    browser.get(link)
    print(f"{link} link opened")

    time.sleep(4)
    """"CALCULATE"""
    # Find input field and fill in by answer
    answer_field = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)
    print(answer)
    print("Answer is calculated")
    # Find submit button and click
    submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()
    print("Answer is submitted")

    # Find message filed and check result message
    message_field = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    message = message_field.text
    print(f"{link} shows {message}")
    correct_message = "Correct!"
    print("*******************************************")
    print(correct_message)
    assert message == correct_message, message


# The owls are not what they seem! OvO
