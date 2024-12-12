# Created by BCC at 11/24/2024
Feature: Test for empty cart
  # Enter feature description here

  Scenario: User has an empty cart
  Given Open Target main page
  When Click on Cart icon
  Then Verify “Your cart is empty” message is shown

    # Enter steps here