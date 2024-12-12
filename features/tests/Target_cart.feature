# Created by BCC at 11/24/2024
Feature: Test for empty cart
  # Enter feature description here

  Scenario: User has an empty cart
  Given Open Target main page
  When Click on Cart icon
  Then Verify “Your cart is empty” message is shown


  Scenario: User can add product in cart
  Given Open Target main page
  When Search for mug
  And Click Add to cart button
  And Click Add to cart button from side navigation
  And Open cart page
  Then Verify cart has 1 items
  Then Verify cart has correct product

    # Enter steps here