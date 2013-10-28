Feature: Follow User

  Background: With two different users
    Given a user named "Fred_Carpenter_1"
      And a user named "Myers_Carpenter_1"
      And a link to "http://example.com" posted by "Fred_Carpenter_1" titled "A test link"

  Scenario: following a user
    Given we are logged in as "Myers_Carpenter_1"
     When visiting a link post for "http://example.com"
      And click on the link "Fred_Carpenter_1"
    
