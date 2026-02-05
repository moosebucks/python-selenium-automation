# Created by moussadiakite at 2/3/26
Feature: Test for app

  Scenario: User can open Terms and conditions
    Given Open Target sign in page
    When Store original window
    And Click on Terms and Conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window



#  Scenario: User is able to open Privacy Policy
#    Given Open Target App page
#    And Store original window
#    When Click Privacy Policy link
#    And Switch to new window
#    Then Verify Privacy Policy page opened
#    And Close current page
#    And Return to original window
