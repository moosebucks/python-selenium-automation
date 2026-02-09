# Created by moussadiakite at 1/18/26
Feature: Verify user can sign in

#  Scenario: User can sign in
#    Given Open Target main page
#    When Click on account button
#    And From right side navigation menu, click Sign In
#    Then Verify Sign In page

  Scenario: User can't sign in with invalid credentials
    Given Open Target sign in page
    When Enter correct email and click Continue
    And Enter incorrect password
    And Click Sign in with password
    Then Verify that an error message is shown
