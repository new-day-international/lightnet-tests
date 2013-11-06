Feature: Register

  Scenario: Registration modal works
	Given I visit "http://localdev.lightnetb.org/"
	When I click the link with text "register"
	Then I should see "create a new account"

  Scenario: Register new user
	Given I visit "http://localdev.lightnetb.org/"
	Given random new user as the persona 
	When I click the link with text "register"
	When I fill in "user" with "$fullname"
	When I fill in "email_reg" with "$email"
	When I fill in "passwd_reg" with "$password"
	When I fill in "passwd2_reg" with "$password"
	When I press "create account"
	Then I should see "$username"

  Scenario: Login as user
  	Given "Frank" as the persona
	Given I visit lightnet
	Given I am logged in as the current persona
	Then I should see "Frank_1"
 
  @wip
  Scenario: Logout as user
    Given "Frank" as the persona
    Given I visit lightnet
    Given I am logged in as the current persona
    When I click the link with text "logout"
    Then I should not see "$username"