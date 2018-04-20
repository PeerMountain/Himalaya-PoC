Feature: Invitation Message
    Scenario Outline: Generate and send an invitation message

      # Message hash of the genesis invite
      Given genesis_invite_message_hash is string XY+IUYG2tojWCPSQz7dVhcSoEDOTZdGsPlfDIDsYIKg=

      # The content of PEM private key file of a new identity
      Given new private key as sender_key
        And nickname is string <nickname>

      # Get bootstrap node public key
      Given teleferic_bootstrap is URI <bootstrap_node>
        And following graphql query as gql_query
        """
        query{
          teleferic{
            persona{
              pubkey
            }
          }
        }
        """
      When we send [gql_query] to bootstrap node <bootstrap_node> and store the response as pubkey_query_response
      Then [pubkey_query_response] response should be success
      
      Given property data.teleferic.persona.pubkey from [pubkey_query_response] as encoded_teleferic_public_key
      When we decode [encoded_teleferic_public_key] with base64 as teleferic_public_key

      # Generate invite key proof
      Given secret_invite_key is string <passphrase>
        And secret_invite_nonce is string <invite_nonce>
      When we compose decryption_data with keys
      """
        'key': [passphrase],
        'nonce': [invite_nonce],
      """
        And we pack [decryption_data] with message pack as packed_decryption_data

      When we encrypt [packed_decryption_data] using RSA with key [teleferic_public_key] as proof_invite_key

      # Generate invite name proof
      Given secret_invite_name is string <invite_name>
      When we encrypt [secret_invite_name] using RSA with key [teleferic_public_key] as proof_invite_name
      
      # Generate registry message body
      Given sender_public_key as the public key of [sender_key]
      When we compose message_body with following keys
      """
        inviteMsgID: [genesis_invite_message_hash],
        keyProof: [proof_invite_key],
        inviteName: [proof_invite_name],
        publicKey: [sender_public_key],
        publicNickname: [nickname],
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
      Given body_type is integer 1
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
      Then we encrypt [packed_message_content] using AES with key [message_key] as encrypted_message_content
        And we calculate SHA256 hash of pack [encrypted_message_content] as message_hash
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
            'message': [encrypted_message_content],
        """
        And we send [gql_query] with variables [message_envelope] to bootstrap node <bootstrap_node> and store the response as send_message_mutation_response
      Then [send_message_mutation_response] response should be <expected_reponse>

    Examples:
    | nickname | invite_name | invite_nonce |passphrase                       | bootstrap_node                                 | expected_reponse |
    | sample_1 | Invite 1    | nonce1 | 72x35FDOXuTkxivh7qYlqPU91jVgy607 | https://teleferic-dev.dxmarkets.com/teleferic/ | success          |
    | sample_2 | Invite 1    | nonceI | 72x35FDOXuTkxivh7qYlqPU91jVgy607 | https://teleferic-dev.dxmarkets.com/teleferic/ | success          |
    # Nickname collision
    | sample_2 | Invite 1    | nonce2 | 72x35FDOXuTkxivh7qYlqPU91jVgy607 | https://teleferic-dev.dxmarkets.com/teleferic/ | failure          |
    # Invalid name
    | sample_3 | Invite 2    | nonce2 | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | https://teleferic-dev.dxmarkets.com/teleferic/ | failure          |
    # Invalid key 
    | sample_4 | Invite 1    | nonce3 | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3R | https://teleferic-dev.dxmarkets.com/teleferic/ | failure          |
