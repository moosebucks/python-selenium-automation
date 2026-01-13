# Created by moussadiakite at 1/13/26
Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

  Scenario: User can enter cart
    Given Open Target main page
    When Click on cart icon
    Then Verify "cart is empty” message is shown

  Scenario: User can sign in
  Given Open Target main page
  When Click on account button
  And Click Sign In button
  Then Verify Sign In page



#
