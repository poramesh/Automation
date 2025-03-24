## Overview

This project utilizes Selenium WebDriver with Behave (a Cucumber-style BDD framework for Python) to automate testing of the Emirates webpage, which is a dynamic web application.
Since the webpage content updates dynamically, this framework makes use of XPath axes to accurately locate and interact with elements that might shift or change. By leveraging advanced XPath techniques, the tests ensure robustness and reliability in element selection, even when the webpage structure evolves.

Additionally, the framework follows the Page Object Model (POM) design pattern to improve:
Maintainability – Any UI changes require updates only in one place.
Reusability – The same page objects can be used across multiple tests.
Readability – Tests are structured clearly, making it easy for developers and testers to understand.

## Prerequisites

- Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Selenium WebDriver
- Behave (BDD framework for Python)


## Installation
```
Clone the repository and install dependencies:
git clone https://github.com/yourusername/selenium-cucumber-emirates.git
cd selenium-cucumber-emirates
pip install -r requirements.txt
```

## Project Structure

```
selenium-cucumber-python/
│── features/            
│   ├── search_flight.feature     
│── pages/                # Page Object Model (POM) classes
│   ├── base_page.py  
│   ├── search_page.py   
│   ├── search_results.py 
│──steps
│   ├──search_flight_steps.py
│── requirements.txt      # Python dependencies
│── README.md 
```

## Running Tests
```
behave feature/search_flight.feature
```
