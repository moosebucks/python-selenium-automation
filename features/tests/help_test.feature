# Created by BCC at 12/29/2024
Feature: Test for help page
  # Enter feature description here

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for returns
    Then Verify Help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Promotions page opened

    Scenario: User can select Help topic Target Circle
    Given Open Help page for returns
    Then Verify Help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help Circle page opened

