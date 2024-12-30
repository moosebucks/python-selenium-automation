# Created by BCC at 12/30/2024
Feature: Sign in test
  # Enter feature description here

  Scenario: User gets message after incorrect credentials
    Given Open sign in page
    When Enters incorrect email and password combination
    And Clicks login button
    Then Verify that “We can't find your account” message is shown


    # Enter steps here