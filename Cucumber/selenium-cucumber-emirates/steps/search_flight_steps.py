from selenium import webdriver
from behave import given, when, then
from pages.search_results import ResultsPage
from pages.search_page import SearchPage


@given("I am on Emirates homepage")
def home_page(context):
    print("am i here?")
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.emirates.com/uk/english/")
    context.driver.maximize_window()
    context.search_page = SearchPage(context.driver)

   
@when("I accept cookies")
def cookies_accept(context):
    context.search_page.cookies()


@when("I enter London as the departure city") 
def departure_location(context):
    context.search_page.departure('London')


@when("I enter Bengaluru as the destination city")
def destination_location(context):
    context.search_page.arrival('Bengaluru')


@when("I select a continue button")
def click_on_continue_button(context):
    context.search_page.continue_button()


@when("I select a one-way trip")
def select_one_way_trip(context):
    context.search_page.one_way()


@when("I select current date as the departure date")
def select_departure_date(context):
    context.search_page.departure_date()


@when("I click the search button")
def click_search_button(context):
    context.search_page.search_button()
    context.search_results = ResultsPage(context.driver, "london","Bengaluru")


@then("The search results should be displayed")
def search_page(context):
    context.search_results.get_result_message()

