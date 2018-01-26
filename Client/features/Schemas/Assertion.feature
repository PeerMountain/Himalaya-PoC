Feature: Assertion Message
    @wip
    Scenario Outline: Generate object container requirements
        # Object
        Given following private key as sender_key
        """
        -----BEGIN RSA PRIVATE KEY-----
        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
        -----END RSA PRIVATE KEY-----
        """
        Then we set our identity with private key [sender_key]
            
        Given user_attachment is object <object>
        
        When we calculate SHA256 hash of [user_attachment] as object_hash
        Then we check [object_hash] and <expected_object_hash> should be equal

        Given container_key is random string form example <container_key>
        When we encrypt <object> using AES with key [container_key] as object_container
        Then we check [object_container] and <expected_object_container> should be equal

        When we calculate SHA256 hash of [object_container] as container_hash
        Then we check [container_hash] and <expected_container_hash> should be equal

        # Meta data
        Given meta_type is integer <meta_type>
            And meta_value is string <meta_value>
            And random 40 bytes salt for example <meta_salt> as meta_salt
        When we compose meta_base with following keys
        """
            'metaType': {meta_type},
            'metaValue': {meta_value},
        """
            And we pack [meta_base] with message pack as packed_meta_base
            And we calculate HMAC-SHA256 of [packed_meta_base] with [meta_salt] as salted_meta_hash
        Then we check [salted_meta_hash] and <expected_salted_meta_hash> should be equal
            And we compose assertion_meta with following keys 
            """
                'metaType': {meta_type},
                'metaValue': {meta_value},
                'metaSalt': {meta_salt},
            """
        
        # Assertions
        Given one or more [assertion_meta]
            And [salted_meta_hash] for each one
        Then we compose a list of [assertion_meta] as meta_list
            And we compose a list of [salted_meta_hash] as salted_meta_hash_list

        Given valid_until is datetime <valid_until>
        When we format [valid_until] with iso formated string as valid_until_formated
        Then we check [valid_until_formated] and <expected_valid_until> should be equal

        Given retain_until is datetime <retain_until>
        When we format [retain_until] with iso formated string as retain_until_formated
        Then we check [retain_until_formated] and <expected_retain_until> should be equal

        Given teleferic bootstrap node URI http://127.0.0.1:8000/teleferic
            And timestamped signature of [user_attachment] as object_sign
        Then we compose assertion with following keys
            """
                'validUntil': {valid_until_formated},
                'retainUntil': {retain_until_formated},
                'containerHash': {container_hash},
                'containerKey': {container_key},
                'objectHash': {object_hash},
                'objectSign': {object_sign},
                'metas': {meta_list},
            """

        Given one or more [assertion]
        Then we compose a list of [assertion] as assertion_list
        
        #Message body
        Given sender_address is the address of [sender_key]
        Then we compose message_body with following keys
        """
            'subjectAddr': {sender_address},
            'assertions': {assertion_list},
        """

        When we pack [message_body] with message pack as packed_message_body
        Then we calculate SHA256 hash of pack [packed_message_body] as body_hash
        
        Given random 40 bytes salt as dossier_salt
        Then we calculate HMAC-SHA256 of [packed_message_body] with [dossier_salt] as dossier_hash

        #Message content
        Given body_type is integer 0
            And message_key is string <message_key>
            And timestamped signature of [packed_message_body] as message_body_signature
        When we compose message_content with following keys
        """
            'bodyType': {body_type},
            'dossierSalt': {dossier_salt},
            'messageBody': {packed_message_body},
            'signature': {message_body_signature},
        """
            And we pack [message_content] with message pack as packed_message_content
        Then we encrypt [packed_message_content] using AES with key [message_key] as encrypted_message_content
            And we calculate SHA256 hash of pack [encrypted_message_content] as message_hash
        
        #Message envelope
        Given following public key as reader_key
        """
        -----BEGIN PUBLIC KEY-----
        MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzqetl2Xeljv2kbW0mn4s
        BWeLPdsI213yHWZ45DAYEe/7ldMeXpDvkaVH9JTauDoGhwmopsS5zOVVs5+IC/9U
        PNViD7fYCpTvsu1qnbyKJJNPbTxvzPelArvOTfprmnFCDW7YZcpPoqPtibZXIpkk
        cFFNRCCZDjMgVfd0TUVW1l7UVeG32a0a68JK9k5mTbcqoZdWZT+zK2JwMsrMAxno
        EqxvrjpnZLpKsHQ8JMZQ98akaUVLzYnDBd7uVoHHdnumE/oW/dnAf5xJE8AgLkGq
        qhEC5BY/EF6BpkqYzeGLY1lJ+lqsyAySu91GGlAF/vVsCxGHBICuIQwdNvVOUTLr
        HTZjIy3A00bzSmL/cYCmGdXt5PDik4d1J6pu+UEWp1rQOSB9l+G8qogMo7m7OTmc
        pxODbgZwrw+yk0FGlSAdPMJ3eIuEHbh6CmRY2lmJ6Todc7nzF8FX/CyysJ1AO1i/
        q/Kjy4N4NcIDHysGZ10H/TzEKmOvujuNQUQXLoj3KaXSh3HLBSw/IYdQxEK1+t0Z
        KwrXpBYHNo/E87T37qLxq6s0Qlgvb2lsX6mDkYMqQSuCTpLxRt9L1poGhkE4UJY/
        KJh/Xj1XAh66VpZ6iuUjFNUPkvmG9VfRGdtdhlIZJdrx72VLbuwd+XuoVa1i9ZYa
        UWdRIWVqQqAjpzWwn9qlXJMCAwEAAQ==
        -----END PUBLIC KEY-----
        """
        And reader_address is the address of [reader_key]
        When we encrypt [message_key] usign RSA with key [reader_key] as encrypted_message_key
        Then we compose acl_rule with following keys
        """
            'reader': {reader_address},
            'key': {encrypted_message_key},
        """

        Given one or more [acl_rule]
        Then we compose a list of [acl_rule] as acl_rule_list

        Given timestamped signature of [container_hash] as container_sign
        Then we compose object_data with following keys
        """
            'containerHash': [container_hash],
            'objectHash': [object_hash],
            'containerSig': [container_sign],
            'objectContainer': [object_container],
            'metaHashes': [salted_meta_hash_list],
        """

        Given one or more [object_data]
        Then we compose a list of [object_data] as objects_data_list

        Given timestamped signature of [message_hash] as message_sign
            And message_type is string ASSERTION
        Then we compose message_envelope with following keys
        """
            'sender': [sender_address],
            'messageType': {message_type},
            'ACL': {acl_rule_list},
            'objects': {objects_data_list},
            'messageHash': {message_hash},
            'messageSig': {message_sign},
            'dossierHash': {dossier_hash},
            'bodyHash': {body_hash},
            'message': {encrypted_message_content},
        """

        #Send message
        Given following graphql query as gql_query
        """
        mutation (
            $sender: Address!
            $messageType: MessageType!
            $messageHash: SHA256!
            $bodyHash: SHA256!
            $messageSig: Sign!
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
                    messageSig: $messageSig
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
        When we send [gql_query] with variables [message_envelope] to bootstrap node
        Then server should response success


    # Retrieve the message from Teleferic
    # and check all the hashes.
    Given sent message hash as assertion_message_hash
        And following private key as reader_sk
        """
        -----BEGIN RSA PRIVATE KEY-----
        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
        -----END RSA PRIVATE KEY-----
        """
        And we set our identity with private key [reader_sk]

    Given we retrieve message with hash [assertion_message_hash]
        And we get key from ACL for our address as encrypted_key
        And we decrypt [encrypted_key] with our identity as message_key
        And we get the encrypted message content as encrypted_message
        And we extract value messageHash from [envelope] as expected_message_hash
    When we calculate SHA256 hash of [encrypted_message] as message_hash
    Then we check [message_hash] and [expected_message_hash] should be equal

    Given we extract value objects from [envelope] as objects
    Given we extract first value from [objects] as object
        And we extract value objectContainer from [object] as encrypted_object

    Given we decrypt [encrypted_message] with AES module [message_key] as packed_message
    When we unpack [packed_message] with message pack as message
    Given we extract value dossierSalt from [message] as dossier_salt
        And we extract value dossierHash from [envelope] as expected_dossier_hash
        And we extract value messageBody from [message] as packed_body
    When we calculate HMAC-SHA256 of [packed_body] with [dossier_salt] as dossier_hash
    Then we check [dossier_hash] and [expected_dossier_hash] should be equal

    When we unpack [packed_body] with message pack as message_body
    Given we extract assertions from [message_body] as assertions
        And we extract first value from [assertions] as assertion
        And we extract value containerHash from [assertion] as expected_container_hash
    When we calculate SHA256 hash of [encrypted_object] as container_hash
    Then we check [container_hash] and [expected_container_hash] should be equal

    Given we extract value containerKey from [assertion] as container_key
        And we decrypt [encrypted_object] with AES module [container_key] as encoded_object
    # When we base64 decode [encoded_object] as object
    # object is for example, the passport picture that the sender sent.
    Given we extract value objectHash from [assertion] as expected_object_hash

    When we calculate SHA256 hash of [encoded_object] as object_hash
    Then we check [object_hash] and [expected_object_hash] should be equal

    Given we extract value metaHashes from [object] as meta_hash_list
    Given we extract first value from [meta_hash_list] as expected_meta_hash
        And we extract value metas from [assertion] as meta_list
        And we extract first value from [meta_list] as meta
        And we extract value metaSalt from [meta] as meta_salt
        And we extract value metaType from [meta] as meta_type
        And we extract value metaValue from [meta] as meta_value
    When we compose meta with following keys
        """
            'metaType': {meta_type},
            'metaValue': {meta_value},
        """
        And we pack [meta] with message pack as packed_meta
        And we calculate HMAC-SHA256 of [packed_meta] with [meta_salt] as meta_hash
    Then we check [meta_hash] and [expected_meta_hash] should be equal



    Examples:
        | object           | expected_object_hash                         | container_key | expected_object_container | meta_type | meta_value | meta_salt                                                                                                               | expected_salted_meta_hash                    | valid_until | expected_valid_until | retain_until | expected_retain_until | expected_container_hash                      | message_key |
        | 010203           | t56he3xcqP6czNjNum6PjtCzyUj59wntD0fS/Uf8uoI= | sarasa1       | +jEzC80Y9Pul7g98F6gZAg==  | 1         | Pepe       | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | bBiKfN62xmZnCGsM6Hqmfw0+BpsVc0SYxdWFhcndGi4= | 2018-05-10  | 2018-05-10T00:00:00  | 2018-05-20   | 2018-05-20T00:00:00   | D5mrut86IyMo2kNA5hqwf3UiZN1XM7N4KZc/q51aVPU= | sarasa1234  |
        | 010203           | t56he3xcqP6czNjNum6PjtCzyUj59wntD0fS/Uf8uoI= | sarasa0       | B2KGRIBbF6UKpAFjvsF79A==  | 2         | Juan       | d3:11:19:a2:86:14:91:74:c7:d1:2c:10:04:59:a0:db:e5:75:e5:2c:1c:7e:9e:df:07:7c:90:8e:a0:aa:01:0b:ae:7f:b7:13:32:d3:d2:dc | sPhFVzSRrH5M4XeJImz21kogpwrkXePynS2XwFxJKsY= | 2018-06-10  | 2018-06-10T00:00:00  | 2018-06-20   | 2018-06-20T00:00:00   | LKGjgDBL2hMXQ/+ax59Sl/4WjccOk8YalVVrT7EE/JU= | sarasa1235  |
        | 010203040506     | P1wLX5wybnlopT/lIdtUbxaNUYSUmNUSHDothe6nQGA= | sarasa3       | ensTiWrrO78XQAffe8t3SQ==  | 1         | Pedro      | 80:9a:a9:b7:c4:d7:0c:4a:59:45:4e:b3:d5:7e:cc:b4:58:83:cf:e4:f5:5c:1e:68:2a:d1:0e:0d:45:c6:b4:cc:71:5d:b6:0d:62:45:25:26 | HgIIyadfDofShEHKpoJ1K9CRzvplqnQtg4eJmdsUyhE= | 2018-07-10  | 2018-07-10T00:00:00  | 2018-07-20   | 2018-07-20T00:00:00   | EmDPxxrI8yahbGnP/wxqUZw4rX6WqXXzreN6fgDibnM= | sarasa1236  |
        # | 0102030405060708 | RLiURq/ipbxA10ohl74XCBAE+PldgbhEZlJhTNUykMU= | sarasa4       | i4PpgB6LbuB7CWeUKG3cEg==  | 2        | hector     | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | tOii8FZ24idxCk1h5v7afmlWNGsyBA39yhoh+5nm59g= | 2018-08-10  | 2018-08-10T00:00:00  | 2018-08-20   | 2018-08-20T00:00:00   | ujf0XjAjWnqqYeU9pXXuvmrql+L99c6q4ETpQSKsFc0= | sarasa1237  |
    
