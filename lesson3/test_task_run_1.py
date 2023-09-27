import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser

    # этот код выполнится после завершения теста
    print("\nquit browser......................................")
    browser.quit()


class TestMainPage:
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        print("smoke-1")
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        print("no smoke-2")
        assert True


class TestBasket:
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        print("skip? smoke-3")
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        print("smoke-4")
        assert True


@pytest.mark.skip
class TestBookPage:
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        print("smoke-5")
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        print("no smoke-6")
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    print("beta_users smoke-7")
    assert True
