Feature: Invitation Message
    Scenario Outline: Generate and send an invitation message

      # Based on registred test identity
      Given following private key as sender_key
      """
      -----BEGIN RSA PRIVATE KEY-----
      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
      -----END RSA PRIVATE KEY-----
      """

      # Generate invite name
      Given passphrase is string <passphrase>
        And secret_invite_name is string <invite_name>
        And invite_nonce is string <invite_nonce>
      When we encrypt [secret_invite_name] using AES with key [passphrase] and nonce [invite_nonce] as encrypted_invite_name 
      Then we check [encrypted_invite_name] and <expected_encrypted_invite_name> should be equal
      
      # Get bootstrap node address
      Given following graphql query as gql_query
        """
        query{
          teleferic{
            persona{
              address
            }
          }
        }
        """
        When we send [gql_query] to bootstrap node <bootstrap_node> and store the response as address_query_response
        Then [address_query_response] response should be success

      # Generate invite message body
      Given property data.teleferic.persona.address from [address_query_response] as teleferic_address
        And teleferic_bootstrap is url <bootstrap_node>
        And offering_address is address <offering_address>
        And service_announcement_message_hash is string <service_announcement_message>
        And service_identifier is integer <service_offering_id>
      When we compose message_body with following keys
      """
        bootstrapAddr: [teleferic_address],
        bootstrapNode: [teleferic_bootstrap],
        inviteName: [encrypted_invite_name],
        offeringAddr: [offering_address],
        serviceAnnouncementMessage: [service_announcement_message_hash],
        serviceOfferingID: [service_identifier],
      """
      When we pack [message_body] with message pack as packed_message_body
        And we encode [packed_message_body] with base64 as encoded_packed_message_body
      Then we calculate SHA256 hash of pack [encoded_packed_message_body] as body_hash

      # Get signed timestamp from teleferic node
      Given teleferic_bootstrap is URI <bootstrap_node>
        And following graphql query as gql_query
        """
        query{
          teleferic{
            signedTimestamp
          }
        }
        """
        When we send [gql_query] to bootstrap node <bootstrap_node> and store the response as signed_timestamp_query_response
        Then [signed_timestamp_query_response] response should be success
        
        Given property data.teleferic.signedTimestamp from [signed_timestamp_query_response] as encoded_teleferic_signed_timestamp
        When we decode [encoded_teleferic_signed_timestamp] with base64 as packed_teleferic_signed_timestamp
          And we unpack [packed_teleferic_signed_timestamp] with message pack as teleferic_signed_timestamp

      # Generate message body signature
      When we compose signable_object with following keys
      """
        messageHash: [body_hash],
        timestamp: [encoded_teleferic_signed_timestamp],
      """
        And we pack [signable_object] with message pack as packed_signable_object
    And we sign [packed_signable_object] using PKCS1 v1.5 with key [sender_key] as message_body_base_signature
      Then we compose signable_object with following keys
      """
        signature: [message_body_base_signature],
        timestamp: [encoded_teleferic_signed_timestamp],
      """
      When we pack [signable_object] with message pack as packed_signable_object
        And we encode [packed_signable_object] with base64 as message_body_signature

      # Message content
      Given body_type is integer 0
        #Public message
        And message_key is string Peer Mountain
        And random 40 bytes salt as dossier_salt
      When we encode [dossier_salt] with base64 as encoded_dossier_salt
        And we compose message_content with following keys
        """
          'bodyType': [body_type],
          'dossierSalt': [encoded_dossier_salt],
          'messageBody': [encoded_packed_message_body],
          'signature': [message_body_signature],
        """
        And we pack [message_content] with message pack as packed_message_content
    Then we calculate SHA256 hash of pack [encrypted_message_content] as message_hash
        And we calculate HMAC-SHA256 of [packed_message_content] with [dossier_salt] as dossier_hash

      # Generate message signature
      When we compose signable_object with following keys
      """
        messageHash: [message_hash],
        timestamp: [encoded_teleferic_signed_timestamp],
      """
        And we pack [signable_object] with message pack as packed_signable_object
        And we sign [packed_signable_object] using RSA with key [sender_key] as message_base_signature
      Then we compose signable_object with following keys
      """
        signature: [message_base_signature],
        timestamp: [encoded_teleferic_signed_timestamp],
      """
      When we pack [signable_object] with message pack as packed_signable_object
        And we encode [packed_signable_object] with base64 as message_signature

      # Send message

      Given message_type is string REGISTRATION
        And sender_address as the address of [sender_key]
        And following graphql query as gql_query
        """
        mutation (
            $sender: Address!
            $messageType: MessageType!
            $messageHash: SHA256!
            $bodyHash: SHA256!
            $messageSign: Sign!
            $message: AESEncryptedBlob!
            $dossierHash: HMACSHA256!
            ){
            sendMessage(
                envelope: {
                    sender: $sender
                    messageType: $messageType
                    messageHash: $messageHash
                    bodyHash: $bodyHash
                    messageSign: $messageSign
                    message: $message
                    dossierHash: $dossierHash
                }
            ) {
                messageHash
            }
        }
        """
      When we compose message_envelope with following keys
        """
            'sender': [sender_address],
            'messageType': [message_type],
            'messageHash': [message_hash],
            'messageSign': [message_signature],
            'dossierHash': [dossier_hash],
            'bodyHash': [body_hash],
            'message': [message_content],
        """
        And we send [gql_query] with variables [message_envelope] to bootstrap node <bootstrap_node> and store the response as send_message_mutation_response
      Then [send_message_mutation_response] response should be success

      Given property data.sendMessage.messageHash from [send_message_mutation_response] as invite_message_hash
      #Then we can make a registration
      
    Examples:
    | invite_name | invite_nonce | passphrase                       | expected_encrypted_invite_name | bootstrap_node                                 | offering_address                                                           | service_announcement_message                 | service_offering_id |
    | Invite 1    | someNonce | 72x35FDOXugkxivh7qYlqPU91jVgy607 | OnhsB48KkRAguMJd5RklLQ==       | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                   |
    | InvitE 2    | someOtherNonce | 4fKuFNOQdisWzhdup3dWRiGIV74kAdag | fkx5vRvAYbM/JBI8KpzXWw==       | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                   |
    | InViTe 3    | YetAnotherNonce | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | gq2UnfPHYJwOZYkanb1HVA==       | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                   |
