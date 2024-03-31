Feature: Whats New Page

  Background: Open Whats New page
    Given I am on the Whats New page

  @newpage
  Scenario: Check that the URL is correct
    Then The URL of the page is "https://magento.softwaretestingboard.com/what-is-new.html"