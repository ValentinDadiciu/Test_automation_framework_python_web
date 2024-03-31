Feature: Login Page

  Background: Open login page
    Given I am on the login page

  @smoke @regression
  Scenario: Check that the URL is correct
    Then The URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"

  @regression
  Scenario Outline: Login with unregistered email
    When I enter "<username>" as email
    And I enter "<password>" as password
    And I click the signin button
    Then I should see "The account sign-in was incorrect or your account is disabled temporarily." message
    Examples:
      | username             | password       |
      | vali444@gmail.com    | 12345678       |
      | vali555@gmail.com    | dsfdfg4        |
      | vali446@gmail.com    | sdfsfsfdfttg   |
      | vali777@gmail.com    | ewrewrfjy      |