Feature: Invite and Register users

  Scenario Outline: Persona generate an Invitation
  In order to invite new Persona to Himalaya
  Registered Persona needs to generate and send an Invitation
    Given registred Identity stored in <identity>
    And Teleferic has pubkey <telefericPubkey>
    And bootstrap url is "<bootstrapNode>"
    And bootstrap PM-Address is "<bootstrapAddr>"
    And offering PM-Address is "<offeringAddr>"
    And service announcement message is "<serviceAnnouncementMessage>"
    And service offering ID is "<serviceOfferingID>"
    And invitation name is "<inviteName>"
    And invitation key is "<inviteKey>"
    And dossier salt is "<dossierSalt>"
    And message hash is "<messageHash>"
    And dossier hash is "<dossierHash>"
    And body hash is "<bodyHash>"
    And message sign is "<messageSign>"
    And message type is "REGISTRATION", and is stored in <messageType> 
    And message body type is "0", and is stored in <bodyType>
    When I encrypt "<inviteName>" using AES-256 with <inviteKey> and store it on <encryptedInviteName>
    And I compose invitation message with <encryptedInviteName>, <bootstrapNode>, <offeringAddr>, <serviceAnnouncementMessage>, <serviceOfferingID> and <inviteName>. And I store it in <messageBody>
    And I compose message content with <dossierSalt>, <bodyType> and <messageBody>. And I store it in <messageContent>
    And I encrypt <messageContent> as JSON string using AES with "<AESKey>" as passphrase and store it in <encryptedMessage>
    And I sign <encryptedMessage> using RSA-SHA256 with <identity> and store it on <messageSignature>
    And I send <encryptedMessage> and <messageSignature> as public message to Teleferic
    Then the query response should be "<result>"

  Examples:
    | messageSign | bodyHash | messageHash | dossierHash | dossierSalt                               | serviceOfferingID | bootstrapNode | bootstrapAddr | offeringAddr | serviceAnnouncementMessage | inviteName                         | inviteKey                       | AESKey        | result  |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | 1            | 1                          | Good                               | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | success |
    | valid       | valid    | valid       | valid       | wPe5JMeAavdsI2X3rhScmhQr1nWQ3XEJyfsL953U  | 1                 | 1             | 1             | 1            | 1                          | Bad inviteKey                      | yYc4lrQr3junX5yJFag16Vw89lThV9A | Peer Mountain | success |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nb   | 1                 | 1             | 1             | 1            | 1                          | Short dossierSalt                  | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | DJAC4NCrVFcMQ34zMShKwFXAi3I3hN4KbWdVs5nbP | 1                 | 1             | 1             | 1            | 1                          | Long dossierSalt                   | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | qY6vh0hd93IJJXXQmyyU2WJKESD6aTayLkF9AYIV  | 1                 | 1             | 1             | 1            | 1                          | Bad AESKey                         | yYc4lrQr3junX5yJFah16Vw89lThV9A | Teleferic     | failure |
    | invalid     | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | 1            | 1                          | Invalid Sign                       | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | invalid  | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | 1            | 1                          | Invalid bodyHash                   | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | invalid     | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | 1            | 1                          | Invalid messageHash                | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | invalid     | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | 1            | 1                          | Invalid dossierHash                | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | None              | 1             | 1             | 1            | 1                          | Invalid serviceOfferingID          | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | None          | 1             | 1            | 1                          | Invalid bootstrapNode              | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | None          | 1            | 1                          | Invalid bootstrapAddr              | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | None         | 1                          | Invalid offeringAddr               | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
    | valid       | valid    | valid       | valid       | DJANCrVFcMQ34zMShKwFXAi3I33hN4KbWdVs5nbP  | 1                 | 1             | 1             | 1            | None                       | Invalid serviceAnnouncementMessage | yYc4lrQr3junX5yJFah16Vw89lThV9A | Peer Mountain | failure |
