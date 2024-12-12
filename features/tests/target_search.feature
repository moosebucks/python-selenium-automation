# Created by BCC at 11/24/2024
Feature:Test for search
  # Enter feature description here

  Scenario: User can search for a product
  Given Open Target main page
  When Search for tea
  Then Verify search results shown for tea


Scenario: User can search for a product
  Given Open Target main page
  When Search for ball
  Then Verify search results shown for ball

 Scenario Outline: User can search for a product
  Given Open Target main page
  When Search for <product>
  Then Verify search results shown for <product>
  Examples:
   |product   |
   |coffee    |
   |ball      |
   |water     |


