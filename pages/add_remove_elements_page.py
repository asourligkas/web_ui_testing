from selenium.webdriver.common.by import By

class AddRemoveElementsPage:
    # URL
    url = 'https://the-internet.herokuapp.com/add_remove_elements/'

    # Locators
    add_button = (By.XPATH, "//button[text()='Add Element']")
    delete_buttons = (By.XPATH, "//button[text()='Delete']")

    # Initializer

    def __init__(self, driver):
        self.driver = driver

    # Interaction Methods

    def load(self):
        self.driver.get(self.url)

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def number_of_delete_buttons(self):
        number_delete_buttons = len(self.driver.find_elements(*self.delete_buttons))
        return number_delete_buttons

    def delete_last_element(self):
        delete_buttons_list = self.driver.find_elements(*self.delete_buttons)
        delete_buttons_list[-1].click()