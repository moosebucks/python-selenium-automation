# Created by BCC at 12/8/2024
Feature: Test for Target Circle page
  # Enter feature description here

  Scenario: User can see correct amount of header links on Circle page
  Given Open Target main page
  When Click on Target Circle header
  Then Verify atleast 10 benefit cells are shown
    # Enter steps here




  Scenario: User can add product in cart
  Given Open Target main page
  When Search for mug
  And Click Add to cart button
  And Stored product name
  And Click Add to cart button from side navigation
  And Open cart page
  Then Verify cart has 1 items
  Then Verify cart has correct product