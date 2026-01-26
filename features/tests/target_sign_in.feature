# Created by moussadiakite at 1/18/26
Feature: Verify user can sign in

  Scenario: User can sign in
    Given Open Target main page
    When Click on account button
    And Click Sign In button
    Then Verify Sign In page