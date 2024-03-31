Feature: Search

  Background: Open home page
    Given I am on the home page

  Scenario: Search works properly for existing items
    When I enter "troy" in the search filed
    And I click the search magnifying button
    Then I am redirected on the search results page
    And There are some results displayed