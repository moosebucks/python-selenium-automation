# Created by BCC at 11/24/2024
Feature:Test for search
  # Enter feature description here

  Scenario: User can search for a product
  Given Open Target main page
  When Search for tea
  Then Verify search results shown
    # Enter steps here