Feature: Persona registration

  Scenario Outline: Valid Persona registration
    Given <Persona> identity
    And service info of "<service>"
    And invitation name is "<invitation_name>"
    And invitation key is "<invitation_key>"
    And dossier salt is "<dossier_salt>"
    And valid genesis invitation message
    When I compose valid registration message to <service>
    And I send registration message
    Then response should be <result>

  Examples:
    | Persona | service   | invitation_name | invitation_key | dossier_salt                             | result  |
    | Test_1  | service_1 | sample_1        | key_sample_1   | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP | success |
    | Test_1  | service_1 | sample_1        | key_sample_1   | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP | failure |
    | Test_2  | service_1 | sample_31       | key_sample_31  | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP | success |

  Scenario Outline: Invalid Persona registration
    Given <Persona> identity
    And service info of "<service>"
    And invitation name is "<invitation_name>"
    And invitation key is "<invitation_key>"
    And dossier salt is "<dossier_salt>"
    And valid genesis invitation message
    When I change <attribute> with <value>
    And I compose valid registration message to <service>
    And I send registration message
    Then response should be failure

  Examples:
    | attribute      | value  | Persona | service   | invitation_name | invitation_key | dossier_salt                             | result  |
    | inviteName     | wq234  | Test_1  | service_1 | sample_1        | key_sample_1   | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP | success |
    | dossierSalt    | eq1231 | Test_1  | service_1 | sample_1        | key_sample_1   | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP | failure |