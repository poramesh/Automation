from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver, 10)  
    
    def click(self, by_locator):
        self.driver.implicitly_wait(10)
        click_element = self.wait.until(EC.element_to_be_clickable(by_locator))
        click_element.click()

    def send_text(self, by_locator, text):
        input_element = self.wait.until(EC.visibility_of_element_located(by_locator))
        input_element.clear()
        input_element.send_keys(text)
    
    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text
    
    