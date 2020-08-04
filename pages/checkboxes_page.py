from selenium.webdriver.common.by import By

class CheckboxesPage:
    # URL
    url = 'https://the-internet.herokuapp.com/checkboxes'

    # Locators
    checkboxes_locator = (By.XPATH, "//input[@type='checkbox']")

    # Initializer

    def __init__(self, driver):
        self.driver = driver

    # Interaction Methods

    def load(self):
        self.driver.get(self.url)

    def maximize(self):
        self.driver.maximize_window()

    def checkboxes(self):
        return self.driver.find_elements(*self.checkboxes_locator)

    def number_checkboxes(self):
        checkboxes_number = len(self.driver.find_elements(*self.checkboxes_locator))
        return checkboxes_number

    def checkbox_selected(self, number):
        checkboxes = self.driver.find_elements(*self.checkboxes_locator)
        return checkboxes[number].is_selected()

    def click_checkbox(self, number):
        checkboxes = self.driver.find_elements(*self.checkboxes_locator)
        checkboxes[number].click()