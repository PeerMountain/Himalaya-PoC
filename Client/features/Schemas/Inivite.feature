Feature: Generate and persist valid invitation message
  
  @wip
  Scenario Outline: Generate invite name
    Given secret 32 bytes passphrase <passphrase>
    And secret invite name <inviteName>
    When I encrypt using AES module and given passphrase
    Then the resulting encrypted invite name should be <result>

  Examples:
  | inviteName | passphrase                       | result |
  | Invite 1   | 72x35FDOXugkxivh7qYlqPU91jVgy607 | OnhsB48KkRAguMJd5RklLQ== |
  | InvitE 2   | 4fKuFNOQdisWzhdup3dWRiGIV74kAdag | fkx5vRvAYbM/JBI8KpzXWw== |
  | InViTe 3   | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | gq2UnfPHYJwOZYkanb1HVA== |