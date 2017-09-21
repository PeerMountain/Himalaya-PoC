Feature: Query Version

  Scenario: Get current buildnumber
    Given we have version query
    When we require current version
    Then response data is equal to current version