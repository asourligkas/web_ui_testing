from pages.dyn_load_1_page import DynamicLoadingPage

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