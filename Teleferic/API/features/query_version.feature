Feature: Query Version

  Scenario: Get current buildnumber
    Given Teleferic current version is <current_version>
    When I query the current version of Teleferic
    Then the current version should match