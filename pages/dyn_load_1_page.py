from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicLoadingPage:
    # URL
    url = 'https://the-internet.herokuapp.com/dynamic_loading/1'

    # Locators
    page_text = (By.XPATH, "//div[@class='example']/h4")
    dynamic_element = (By.ID, "finish")
    button = (By.XPATH, "//div[@id='start']/button")

    # Initializer

    def __init__(self, driver):
        self.driver = driver

    # Interaction Methods

    def load(self):
        self.driver.get(self.url)

    def phrase(self):
        return self.driver.find_element(*self.page_text).text

    def element_not_visible(self):
        if self.driver.find_element(*self.dynamic_element).is_displayed():
            return False
        else:
            return True

    def click_start_button(self):
        self.driver.find_element(*self.button).click()

    def wait_until_visible(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))

    def element_text(self):
        print("Displayed message: ", self.driver.find_element(*self.dynamic_element).text)
        return self.driver.find_element(*self.dynamic_element).text
