from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPage(BasePage):
    def __init__(self, driver, departure, arrival):
        super().__init__(driver) 
        self.departure = departure
        self.arrival = arrival
   
    SEARCH_RESULT_TEXT = (By.XPATH, "//h2[@class = 'lowest-fare-block__heading-text-fromto']") 

    def get_result_message(self):
        flight_results = self.get_text(self.SEARCH_RESULT_TEXT)
        print("the keywords on the results is -",flight_results)
        return flight_results
