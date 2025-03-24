## Overview

This project uses Selenium WebDriver with Behave (Cucumber-style BDD framework for Python) to automate web application testing. It follows the Page Object Model (POM) design pattern to enhance maintainability, reusability, and readability of test scripts.

*Selenium WebDriver* is a powerful browser automation tool that allows testers to simulate real user interactions with web applications, such as clicking buttons, entering text, and navigating between pages.

*Behave* follows a Gherkin syntax (Given-When-Then) that allows test cases to be written in a human-readable format. This makes it easier for teams (QA, developers, and business stakeholders) to collaborate on test cases.

*POM* is a design pattern that helps organize test scripts by separating test logic from UI interactions. Each webpage is represented as a Python class, 

## Prerequisites

- Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Selenium WebDriver
- Behave (BDD framework for Python)


## Installation

Clone the repository and install dependencies:
git clone https://github.com/yourusername/selenium-cucumber-emirates.git
cd selenium-cucumber-emirates
pip install -r requirements.txt


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

behave feature/search_flight.feature
