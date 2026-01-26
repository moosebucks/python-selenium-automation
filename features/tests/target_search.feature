# Created by moussadiakite at 1/13/26
Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown


#  Scenario Outline: User can search for a tea on Target
#    Given Open Target main page
#    When Search for <product>
#    Then Search results for <product> are shown
#    Examples:
#    |product  |
#    |mug      |
#    |cap      |
#    |ball     |
#
#
#    Scenario: Verify user can add item to cart
#      Given Open Target main page
#      When Search for tea
#      And Click on add to cart button
#      And Click on add to cart button from the side navigation
#      Then Verify product in cart
#
#
