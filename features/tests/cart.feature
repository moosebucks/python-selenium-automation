# Created by moussadiakite at 1/17/26
Feature: Test for cart

  Scenario: User can enter cart
    Given Open Target main page
    When Click on cart icon
    Then Verify "cart is empty” message is shown
