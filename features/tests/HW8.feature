# Created by BCC at 12/26/2024
Feature: # Enter feature name here
  # Enter feature description here

  Scenario:User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
# Enter scenario name here
    # Enter steps here