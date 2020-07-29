import pytest
from pages.dyn_load_1_page import DynamicLoadingPage
from selenium.webdriver import Chrome

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

def test_dynamicLoading1(browser):
    phrase = "Example 1: Element on page that is hidden"
    element_text = "Hello World!"

    page = DynamicLoadingPage(browser)
    page.load()
    assert phrase == page.phrase()
    assert page.element_not_visible()
    page.click_start_button()
    page.wait_until_visible()
    assert not page.element_not_visible()
    assert element_text == page.element_text()