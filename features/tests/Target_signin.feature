# Created by BCC at 11/24/2024
Feature: Test for signing in
  # Enter feature description here

  Scenario: User is taken to sign in page
  Given Open Target main page
  When Click Sign In
  When From right side navigation menu, click Sign In
  Then Verify Sign In form opened


    # Enter steps here