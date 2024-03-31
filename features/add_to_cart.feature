Feature: Add to cart

  Background: Open home page
    Given I am on the home page

  Scenario: Add to cart
    When I enter "troy" in the search filed
    And I click the search magnifying button
    And I click size button
    And I click color button
    And I click Add to cart button
    Then Cart has "1" item in it