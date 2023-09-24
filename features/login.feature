Feature: Login into the app

  Background:
    Given I am on the login page

    @success
  Scenario: Successfully login into the app
    When I enter my username "standard_user"
    And I enter my password "secret_sauce"
    And I click the login button
    Then I am logged into the app


    @fail
  Scenario Outline: Unsuccessful login into the app
    When I enter my username "<username>"
    And I enter my password "<password>"
    And I click the login button
    Then I receive the error message "Epic sadface: Username and password do not match any user in this service"
    Examples:
     | username | password |
     | standard_user|fail_pass|
     |fail_user     |secret_sauce|
     |fail_user     |fail_pass   |

