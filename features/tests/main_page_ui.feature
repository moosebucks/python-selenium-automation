# Created by BCC at 12/7/2024
Feature: Test for main page UI
  # Enter feature description here

  Scenario: User can see correct amount of header links
  Given Open Target main page
  Then Verify atleast 1 header link is shown