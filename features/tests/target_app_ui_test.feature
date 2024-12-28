# Created by BCC at 12/25/2024
Feature: Test for Target app page

  Scenario: User is able to open Privacy Policy
    Given Open Target main page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window
    # Enter steps here