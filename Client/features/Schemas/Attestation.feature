Feature: Attestation Message

  Scenario: Test Message Analysis in Attestation

    # First, we create an Assertion
    # keys/4096_a.private 
    Given Sender Identity with following private key as idn_sender
    """
    -----BEGIN RSA PRIVATE KEY-----
    MIIJJwIBAAKCAgEAv3H3EmVjgI/N7LWiTmqnMi3ie6RJBgWYOJ9jsZQK/Vifl9ov
    Vd7iw/fCJf0S1IUBI2rbjpzwRvWrYOs3u9g0EAlXi1B9u1kR1OqPaD2YjRvzkzX6
    dAbb7Bcu2Ityz4PyyN1Qxr9yzoamfwgSWc6P9IpBUy4wtRWTwslHkga9uDQ1zPce
    COuEIpn20AZ2bc56GhzBF3WBZBUscCJlUxmdh88bTLQwhnBVVHsaouWJvlcLb41+
    q7P8eIZR4fX1NUuUpmnPQ4TKbUawXx1r/AG8YkpxbB2WG3hwppVuJEI/biZGvZOa
    ZzqqbHDEcQkzHGxmqjG+CPc4zr9oKhgzpkiFtTDvMug5zDqcRdvavUedfY98Fe+S
    DnlCOisacStJWJH9HiCkvqRZkr2qIxm962YsDklllHgh4L6qZ3wdQYRIQPr/P1D0
    Ew/S6Fm8kexEyO10hc3IoEGnYWhnWIl2dzFIWX/cY9rPE1cBok6Y6Y6Wef8zQy97
    0/TuSiL7xjZKH7ocog/rd4ElFyC67rcSECBEKxKWzb4kNGMCAVGVoXyPcJXq35oK
    KyAyqHLJQzoYjOW6zZzA1U+v6V5YPxpvBgTsQbrN5ldLdEbyF9Ef8FAt8pX8hMo8
    OV5TBicnW9Q8zjr9RJ4t638ePS8g+xGSnLe6xha0TMay29a0wpgNcqER0KECAwEA
    AQKCAgBakLQ8DKCsodrdvvMgO44Ky/AXY5lz8tOW/bfwusMUJIejE4FPExidcihz
    RixRQvZN5fAloBJ+zxsax0tfXqEKcRDsA9Dm/vTTj3715iWzo2Rv4Joxp0kEf9cW
    c6mFh7sj0Ka0zr6l+sbq00uzFme9XGYYzoIWODXlcMidyPiZGoHVC5Y2zAt/Puym
    blg6C/JxRecGjPz/9pBGH89lJ3oBVDVq7NcD0kJbq7znEMU/uPfc9sfUvFmUPp6f
    0XYFl1KkAuwc2cXVOhqXdFiwJ7YRnXvYlIp9RlWsSIaJOpm9JvhSGHBzoyoaEKKt
    gpeeO525p7xpi2JhU+UX/Mj6QdaWFi5tPbBjnMOhHFtLAZlFWToWfCoqo8mYTax9
    oIu7ZPFoVyT3j6EL4XcBnv2t13VEQZnWYVwjqgGfmTrA/BBZau9f4UZ6tCW7XBD+
    haWIXQUm4jaRJaXM312Bi3blflLNMvJCkynKdGmYJy4TXF0M2eDWLSgSMrMSOnts
    XPJSGriB5ykQ1/RnYmUia4YMOUB8qKVq3+jjQqD+xTBczSyPIqZxnWKrnzJMixCA
    VP00dAN+Y/vGgUtpscpKXNw7/0inIWPbS2/X1N6wz4JvQOIKKV+vPUOeUEpEKbjp
    VBlalJ9DVLFxIgV12Qsmj/YtiAEPrllSmenRbPibamzQndk+LQKCAQEA3/RPU1cL
    gOXGy/MncbzRCNFkJegID273LaJJKyRdnZZjoNu/r+4oJdxFGOgNHKRvAmHJmkm3
    rVe6NZUo40sVLX6eW/Pgp1IiamYlTKI/Kfomdy1IP6aK9CsiwXLxkjGGfCDFYMPb
    GS6FBIP029OLRtCWuDimNus/J89uKBws+1pYDmy17liitHc5FzF4HPWsHgTmezJX
    Sn52SDSwAWD6e2uDQdmvficcvsIx/nCaVSfr+4WEiNEjBR5GrTjQhYiktDD5tKGD
    FZ1A3D1RqDdnYh+OK3zaqzUFcAiepmyBvmHzgotcH966zrwxIDV1wNSBLTOWEP13
    oRaVpdFEKfM+vwKCAQEA2tbPPBcVu5O3v5U3UMBwINfD2CRbqWmZ2JgXxlUWbeZ7
    iozRxB4qWwHBUUqvaviGsDhItsRG15gS/V6NWMjfta6U+oe5PGW5+MfunMcG474/
    eHMaaCeCrKmHXQMxJ/Nt6Az9dv5urhLSoyauAzEsaS8wbvyRYFS7jMji8IWht10X
    VXBSia46+pDgCWKB597ARwjcinaByFvDusB8+ZjlGqykMT7qpQ9FmrPDxpz2MjXN
    WJU5kKl1LY3MAnC81pJ8iHu9st0LTfaaJf9XKX4LjNQEA4lx+Q9I2/BIftYqAS2r
    QtnC5MFBvAho6SiGSwcivXu37g+ZaanD/OSv6tAonwKCAQBuy+ie25aWW5dheVeP
    XpGwIh/A3S13rTdefUZjsKcb+rYpc+4+tL1qFbKdotgxzmwZKpXZ3hSgDqHSNow2
    /wNoMZdY+KuxO+JI72YOpspHEzoKhf2Td+qQ5/JW8G3xHM1jBbeAqwTvTWODm2D9
    jIgALdwTIfuhefsRz/64m0/pvoWIBWJwm6tLSxyUi+XXtfdEFrqMQpiLA0uzZ1WY
    KQljHAqg/nhjGiiPe3XOYpkH/isykZjDM2x28MaYll4bYkHR39T591npzJW1ICUQ
    6vAbzG7Ctw9b2mxpQ+pxfYcm0EDv2dBm+ANFmjdXrvslvjx2R2o715piuNCqa4Ck
    nHHzAoIBAGkghj9Mq7EHnl7XlNIjD/qHDFr55Fq3EyP8tHcfiv3SmgiN63s2Loy3
    hCHEKg7OQw3GjA/YrFuHf5/d2zMKlIVXz9OmfbLo/3TmvtbruYCQdTcsvEPKrzi4
    3AEvtl6Fz4eJLf4K7iqLekrMGw4HglkpRTAb/s5zBgH0wyheWbiXbM0rf0sKuuSB
    0k5P1y4HUQEO3btagLA6fQVq0N6qt2ygAORzYA9ZDcvqjaMM5ixqsjHaxeObtGHk
    21tUwzKk/lQmdZPGIlcanySfzERve6b0dtUoIutNj2ewv3LG+TjFsp8Ts09nE2f7
    9kIDqLfEPskd9NbVAZLD7hW/2k6IHusCggEAGJ+yCXFNS7SIyaEKfiAzxF/wk3o+
    WQVuQTTGl5MXDOP89DWL5QcQ4iKGozxNVAuqpomMRIfbCcL7tQs8xQR4GZKuO3tB
    G5I5kVxHZtlpfKFjOnoWrYIGwxqOgl5G49fjh3S+XjE06NMIA1NbJP/LYApl74om
    FMivbSThe2qYPVkhpWiNwWHd33BWGcTQhki1WEVYViNtdKGfeG51+Z0BjjLmUlUL
    hB9NWBLSM3NE7WWvS0iMAEafhJXFbYstJtyp5JgQdGiC/HmQGQuhjjnT1V7l7cAH
    yPQaqaVa1aXjJsS1A6vjmA1qXrmJeAAYW3zwo+Jp/3hjZH5qm30xdUkJng==
    -----END RSA PRIVATE KEY-----
    """

      And Reader Identity with following private key as idn_reader
      # keys/4096_b.private
      """
      -----BEGIN RSA PRIVATE KEY-----
      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
      -----END RSA PRIVATE KEY-----
      """

      And following metaType as meta_type
      """
      1
      """

      And following metaValue as meta_value
      """
      Some Value :)
      """

      And following object as object
      """
      010203
      """

      And teleferic bootstrap node URI http://localhost:8000/teleferic

    # To fully understand how the Assertion is made
    # look at Assertion.feature
    Then we compose and send an Assertion storing the messageHash as assertion_message_hash
      And we retrive the previous Assertion data as assertion_data

    # Now, we construct the Attestation
    
    # Objects
    Given Assertion objectHash as assertion_object_hash
      And Assertion metaHashes as assertion_meta_hashes
    Then we compose objects with following keys
      """
      'objectHash': {assertion_object_hash},
      'metaHashes': {assertion_meta_hashes},
      """
      And we compose a list of [objects] as objects_list

    # Get Message Key
    Given Assertion ACL as assertion_acl
      When we get the key from ACL as reader_encrypted_message_key
        And we decrypt [reader_encrypted_message_key] with RSA as assertion_reader_message_key

    # Decrypt Message Content
    Given Assertion message as assertion_encrypted_message
      When we decrypt [assertion_encrypted_message] with AES module [assertion_reader_message_key] as assertion_packed_message
        And we unpack [assertion_packed_message] with message pack as assertion_unpacked_message_content

    # Get Message Body
    Given property messageBody from [assertion_unpacked_message_content] as assertion_message_body    
      When we decode [assertion_message_body] with base64 as assertion_decoded_message_body
    Then we unpack [assertion_decoded_message_body] with message pack as assertion_message_body

    # Build salted_meta_hash
    Given Assertion metaType as assertion_meta_type
      And Assertion metaValue as assertion_meta_value
      And Assertion metaSalt as assertion_meta_salt
    When we compose salted_meta_hash_object with following keys
      """
      'metaType': {assertion_meta_type},
      'metaValue': {assertion_meta_value},
      """
      And we pack [salted_meta_hash_object] with message pack as packed_salted_meta_hash_object
      And we calculate HMAC-SHA256 of [packed_salted_meta_hash_object] with [assertion_meta_salt] as salted_meta_hash

    # Attestations
    Given Assertion bodyHash as assertion_body_hash
      And attestation_string is string TestingAttestation
      And Attestation type Message_Analysis as attestation_type
    Then we compose attestation_object_container with following keys
      """
      'objectHash': {assertion_object_hash},
      'metaHash': {salted_meta_hash},
      """

      And we compose attestation_detail with following keys
        """
        'bodyHash': {assertion_body_hash},
        'objectHash': {assertion_object_hash},
        'metaType': {assertion_meta_type},
        'metaValue': {assertion_meta_value},
        'metaSalt': {assertion_meta_salt},
        'attest': {attestation_string},
        """
      When we pack [attestation_detail] with message pack as packed_attestation_detail

      Then we sign packed_attestation_detail as attestation_sign

      And we compose attestation_object with following keys
        """
        'attestType': {attestation_type},
        'attestSign': {attestation_sign},
        'object': {attestation_object_container},
        'detail': {packed_attestation_detail},
        """

      And we compose a list of [attestation_object] as attestation_object_list

    # Create Message
    Given Sender address as sender_address
      And message_body_type is integer 0
    Then we compose attestation_message_body with following keys
      """
      'subject': {sender_address},
      'attestations': {attestation_object_list},
      'body_type': {message_body_type},
      """
    When we pack [attestation_message_body] with message pack as attestation_packed_message_body
      And we encode [attestation_packed_message_body] with base64 as attestation_encoded_packed_message_body
    Then we calculate SHA256 hash of pack [attestation_encoded_packed_message_body] as attestation_body_hash

    # Create Message Content
    Given body_type is integer 0
      And attestation_message_key is string m3ss@g3k3y
      And signature timestamped of [attestation_body_hash] as attestation_message_body_signature
      And random 40 bytes salt as attestation_dossier_salt
    When we encode [attestation_dossier_salt] with base64 as attestation_encoded_dossier_salt
      And we compose attestation_message_content with following keys
      """
      'bodyType': {body_type},
      'dossierSalt': {attestation_encoded_dossier_salt},
      'messageBody': {attestation_encoded_packed_message_body},
      'signature': {attestation_message_body_signature},
      """
      And we pack [attestation_message_content] with message pack as attestation_packed_message_content
    Then we encrypt [attestation_packed_message_content] using AES with key [attestation_message_key] as attestation_encrypted_message_content
      And we calculate SHA256 hash of pack [attestation_encrypted_message_content] as attestation_message_hash
      And we calculate HMAC-SHA256 of [attestation_packed_message_content] with [attestation_dossier_salt] as attestation_dossier_hash

    # Create ACLs
    Given Reader address as reader_address
      And Reader public key as reader_public_key
      And Sender private key as sender_private_key
    When we encrypt [attestation_message_key] using RSA with key [reader_public_key] as encrypted_message_key_for_reader
      And we encrypt [attestation_message_key] using RSA with key [sender_private_key] as encrypted_message_key_for_sender

    Then we compose reader_acl_rule with following keys
    """
    'reader': {reader_address},
    'key': {encrypted_message_key_for_reader},
    """
      And we compose sender_acl_rule with following keys
      """
      'reader': {sender_address},
      'key': {encrypted_message_key_for_sender},
      """

    Given [reader_acl_rule] and [sender_acl_rule] acl rules
    Then we compose a list of acl rules as acl_rule_list
    
    # Create Message Envelope
    Given signature timestamped of [attestation_message_hash] as attestation_message_sign
      And attestation_message_type is string ATTESTATION
    Then we compose attestation_message_envelope with following keys
    """
    'sender': {sender_address},
    'messageType': {attestation_message_type},
    'ACL': {acl_rule_list},
    'objects': {objects_list},
    'messageHash': {attestation_message_hash},
    'messageSign': {attestation_message_sign},
    'dossierHash': {attestation_dossier_hash},
    'bodyHash': {attestation_body_hash},
    'message': {attestation_encrypted_message_content},
    """

    # Send Message
    Given following graphql query as gql_query
    """
    mutation (
        $sender: Address!
        $messageType: MessageType!
        $messageHash: SHA256!
        $bodyHash: SHA256!
        $messageSign: Sign!
        $message: AESEncryptedBlob!
        $dossierHash: HMACSHA256!
        $ACL: [ACLRule]
        $objects: [ObjectInput]
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
                objects: $objects
                ACL: $ACL
            }
        ) {
            messageHash
        }
    }
    """
    When we send [gql_query] with variables [attestation_message_envelope] to bootstrap node
    Then server should response success
