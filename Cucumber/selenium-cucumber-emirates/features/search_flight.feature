Feature: Search for flights on Emirates

   Scenario: Search a flight from london to Bengaluru(One way)
      Given I am on Emirates homepage
      When I accept cookies
      And I enter London as the departure city 
      And I enter Bengaluru as the destination city
      And I select a continue button
      And I select a one-way trip
      And I select current date as the departure date
      And I click the search button
      Then The search results should be displayed



    