Feature: Register

  Scenario: Registration modal works
    Given random new user as the persona 
    Given I visit "/"
    When I click the link with text "register"
    Then I should see "create a new account"

  Scenario: Register new user
    Given random new user as the persona
    Given I visit "/"
    When I click the link with text "register"
    When I fill in "user" with "$fullname"
    When I fill in "email_reg" with "$email"
    When I fill in "passwd_reg" with "$password"
    When I fill in "passwd2_reg" with "$password"
    When I press "create account"
    Then I should be logged in
  
  Scenario: Login as user
  	Given "Mary" as the persona
    Given I visit "/"
    Given I am logged in as the current persona
    Then I should see "Mary_1"
 
  Scenario: Logout as user
    Given "Mary" as the persona
    Given I visit "/"
    Given I am logged in as the current persona
    When I click the link with text "logout"
    Then I should not be logged in

  Scenario: A user deletes themself
    Given random new user as the persona
    Given I visit "/"
    Given I am logged in as the current persona
    When I click the link with text "preferences"
    When I click the link with text "delete"
    When I fill in "#delete_user" with "$username"
    When I fill in "#delete_password" with "$password"
    When I check "confirm"
    When I press "delete account"
    Then I should not be logged in

  Scenario: Two users register with the same name
  Scenario: Two users register with the same email address
  Scenario: A user uses the wrong password when confirming password in registration
  Scenario: A user uses the wrong password when logging in
  Scenario: A user forgets their password when logging in
  Scenario: A user resets their password