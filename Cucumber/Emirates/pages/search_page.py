from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time
from datetime import date, timedelta


class SearchPage(BasePage):
    today = date.today()
    future_date = today + timedelta(days=10)
    today_digit = today.day
    future_digit = future_date.day

    ACCEPT_COOKIES = (By.XPATH,"//*[@id='onetrust-accept-btn-handler']")
    FROM_LOCATION = (By.XPATH,"//label[text() = 'Departure airport']/following-sibling::input")
    FROM_LOCATION_DROPDOWN = (By.XPATH, "//div[@class = 'js-origin-dropdown']/div/section/ol/li[1]")
    TO_LOCATION = (By.XPATH,"//label[text() = 'Arrival airport']/following-sibling::input")
    TO_LOCATION_DROPDOWN = (By.XPATH,"//div[@class='destination-dropdown']/div/section/ol/li[1]")
    CONTINUE_BUTTON = (By.XPATH,"//*[@id='search-flight-control']/section/div[4]/div[1]/div[4]/button/span")
    ONE_WAY_BUTTON = (By.XPATH,"//label[text()='One way']")
    DEPARTURE_DATE = (By.XPATH,"//label[text() = 'Departing']/following-sibling::input")
    DEPARTURE_SELECT = (By.XPATH,f"//div[@class='ek-datepicker__column']/table/tbody/tr/td/button[text()='{today_digit}']")
    SEARCH_BUTTON = (By.XPATH,"//*[@id='search-flight-control']/section/div[4]/div[2]/div[3]/form/button")



    def cookies(self):
        try:
            self.click(self.ACCEPT_COOKIES)
        except:
            print("No cookie found")

    def departure(self, city):
        try:
            self.send_text(self.FROM_LOCATION,city)
            self.click(self.FROM_LOCATION_DROPDOWN)
        except Exception as e:
            print(e)
            print("departure error")
    
    def arrival(self, city):
        try:
            self.send_text(self.TO_LOCATION, city)
            self.click(self.TO_LOCATION_DROPDOWN)
        except:
            print("arrival error")

    def continue_button(self):
        try:
            self.click(self.CONTINUE_BUTTON)
        except:
            print("continue button error")
    
    def one_way(self):
        try:
            self.click(self.ONE_WAY_BUTTON)
        except:
            print("one way error")

    def departure_date(self):
        try:
            self.click(self.DEPARTURE_DATE)
            print(self.DEPARTURE_SELECT)
            time.sleep(2)
            self.click(self.DEPARTURE_SELECT)
        except Exception as e:
            print("departure date error")
            print(e)
    
    def search_button(self):
        try:
            self.click(self.SEARCH_BUTTON)
            time.sleep(10)
        except:
            print("search button error")
    