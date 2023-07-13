from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)

    basket_btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")

    time.sleep(10)

    assert basket_btn is not None, "basket button not found"

