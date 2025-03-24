##Overview

This project uses Selenium WebDriver with Behave (Cucumber-style BDD framework for Python) to automate web application testing.

##Prerequisites

-Ensure you have the following installed:
-Python 3.8+
-pip (Python package manager)
-Selenium WebDriver
-Behave (BDD framework for Python)


##Installation

Clone the repository and install dependencies:
git clone https://github.com/yourusername/selenium-cucumber-python.git
cd selenium-cucumber-emirates
pip install -r requirements.txt


##Project Structure

```selenium-cucumber-python/
│── features/            
│   ├── search_flight.feature     
│── pages/                # Page Object Model (POM) classes
│   ├── base_page.py  
│   ├── search_page.py   
│   ├── search_results.py 
│──steps
│   ├──search_flight_steps.py
│── requirements.txt      # Python dependencies
│── README.md ``` 

##Running Tests

behave feature/search_flight.feature
