Feature: Assertion Message
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
        Given meta_key is integer <meta_key>
            And meta_value is string <meta_value>
            And random 40 bytes salt for example <meta_salt> as meta_salt
        When we compose meta_base with following keys
        """
            'metaKey': {meta_key},
            'metaValue': {meta_value},
        """
            And we pack [meta_base] with message pack as packed_meta_base
            And we calculate HMAC-SHA256 of [packed_meta_base] with [meta_salt] as salted_meta_hash
        Then we check [salted_meta_hash] and <expected_salted_meta_hash> should be equal
            And we compose assertion_meta with following keys 
            """
                'metaKey': {meta_key},
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

        Given teleferic bootstrap node URI http://localhost:8000/teleferic/
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
        MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqc5KBvXlpj4mrDKgiCk2
        ubKBI6lqEKrcvCoXqpwL5O9sWUo9DMCREHjUg5Fxrzu2zq2DveGaCn3QnNYf+Agx
        oC3cEHpAKx5tTQ+adErO4Uy6Bkl/006oGC5Y3cTfTZuq9r6vFEGbQzNIZFd7LP72
        eCqkqva3U64JjQ7TRHsrCk4xKV7ZXiHvxAT8kl7NmXqFUyVuD4iZHKk2t1dPFbMH
        7glDbQHWKXwcP3I1vTG4HLPQxbR6JzZsxIXWkAjTaswcBQ2F7sKpecKRxXKGuj3X
        0hXt6OyljM/sqmGrzif5uwYEVIaqOPvtk2irVDIomzBtvN/zEuwr0DKYJEZdcFuq
        EKlEBDq2bcCFOuOuLfhxljfDaxRSL2QuloRab1n5gm5OgSr1hwQQ94yod8rjJ9Mc
        XLnmEMfkvx9CC6vWJ2TkfQrnAa5XMpRz1bLE/Vw8r4ENOlR+VFSxPAEPajuU5cWe
        LjtP8+Nd0BQY9oGA1yAt//2Mh7GKaYMQOcKb2M3YrE7bcIGNgz+8A7GI3k0fmYiw
        2TkYJCRR9cHHHYj2eDu1dcCBafe0rS5FdVLKQIatraWiF06IzvgpwDfespduf4pZ
        mESz6EkX9kE5So8xMLkpGZzgI+2jaqwYPniO6kAa/7XgeWjka0mKCPAAgUc6vt/2
        TonU5aVIDB6MrfFXQO5oeXECAwEAAQ==
        -----END PUBLIC KEY-----
        """
            And reader_address is the address of [reader_key] When we encrypt [message_key] usign RSA with key [reader_key] as encrypted_message_key  
        Then we compose acl_rule with following keys
        """
            'reader': {reader_address},
            'key': {encrypted_message_key},
        """

        Given one or more [acl_rule]
        Then we compose a list of [acl_rule] as acl_rule_list

        Given timestamped signature of [container_hash] as container_sign
        Then we compose container_data with following keys
        """
            'containerHash': [container_hash],
            'objectHash': [object_hash],
            'containerSig': [container_sign],
            'objectContainer': [object_container],
            'saltedMetaHashes': [salted_meta_hash_list],
        """

        Given one or more [container_data]
        Then we compose a list of [container_data] as container_data_list

        Given timestamped signature of [message_hash] as message_sign
            And message_type is string ASSERTION
        Then we compose message_envelope with following keys
        """
            'sender': [sender_address],
            'messageType': {message_type},
            'ACL': {acl_rule_list},
            'containers': {container_data_list},
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
            $containers: [ContainerInput]
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
                    containers: $containers
                    ACL: $ACL    
                }
            ) {
                messageHash
            }
        }
        """
        When we send [gql_query] with variables [message_envelope] to bootstrap node
        Then server should response success

    Examples:
        | object           | expected_object_hash                         | container_key | expected_object_container | meta_key | meta_value | meta_salt                                                                                                               | expected_salted_meta_hash                    | valid_until | expected_valid_until | retain_until | expected_retain_until | expected_container_hash                      | message_key |
        | utvu8A==         | RbUuANM6CTG3WUNkNPsc7ia9iY87HKc0LoQZsT/KEvs= | sarasa1       | IgzAp08p7dHnaccZ9wbwXg==  | 1        | Pepe       | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | iekh9yXHh9UCVKNChpGsKtCgtVQ89ZLkfWnwnS9/zTM= | 2018-05-10  | 2018-05-10T00:00:00  | 2018-05-20   | 2018-05-20T00:00:00   | 9li9ozDxnPexSW4vQK1fcGCMx9Fp4TMXu0pCwd5sRJ0= | sarasa1234  |
        | 0WqSAQ==         | InccYmBaAj+sTJJ3VWOPqqoJ6xcu9wa78Sm1Atg0V4Q= | sarasa0       | 8qJA0KN/Ky9zb+lbQGvP1A==  | 2        | Juan       | d3:11:19:a2:86:14:91:74:c7:d1:2c:10:04:59:a0:db:e5:75:e5:2c:1c:7e:9e:df:07:7c:90:8e:a0:aa:01:0b:ae:7f:b7:13:32:d3:d2:dc | n4K6Rj38wS1ufwUGwYadviLoR+OMYlzXrlCP5fZ1ts8= | 2018-06-10  | 2018-06-10T00:00:00  | 2018-06-20   | 2018-06-20T00:00:00   | 4TAJ7dyIUMpvpaDDnHjchJuVdn64P5DjSJn/hFgtj+c= | sarasa1235  |
        | 0WqSAQAAAQmS     | 0MUuYJ4X2qLrEmzYMTcg3TrBoIbR/MEZiQqBnk/reTk= | sarasa3       | 6HlIZ3oDyBkWVjuU/9uFvw==  | 1        | Pedro      | 80:9a:a9:b7:c4:d7:0c:4a:59:45:4e:b3:d5:7e:cc:b4:58:83:cf:e4:f5:5c:1e:68:2a:d1:0e:0d:45:c6:b4:cc:71:5d:b6:0d:62:45:25:26 | mmrsu+/74WuOM/siW5RrghwlM886IiyLkneW/7o2P1s= | 2018-07-10  | 2018-07-10T00:00:00  | 2018-07-20   | 2018-07-20T00:00:00   | fjcK0da8qwdIgfLiJqihQ7PlUc4SH1nDt2GWV9pkHdk= | sarasa1236  |
        | 0WqSAQAAAQmS/hGe | VZIM0Ny3VGaAeJ9jro5ql/9ccTNGMKFLbdICeFe4Z5M= | sarasa4       | G4QvaTvqRfSzui4bQ7XlXg==  | 2        | hector     | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | tOii8FZ24idxCk1h5v7afmlWNGsyBA39yhoh+5nm59g= | 2018-08-10  | 2018-08-10T00:00:00  | 2018-08-20   | 2018-08-20T00:00:00   | jYeVTtpgqJscV7EIsDDnmRFbViGQOcai1qaPHQuMc9w= | sarasa1237  |
    

    @wip
    Scenario: Decrypt a message for which we are the reader
    # a
    Given following private key as reader_private
    """
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
    """
        # A
        And following public key as reader_public
        """
        -----BEGIN PUBLIC KEY-----
        MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAv3H3EmVjgI/N7LWiTmqn
        Mi3ie6RJBgWYOJ9jsZQK/Vifl9ovVd7iw/fCJf0S1IUBI2rbjpzwRvWrYOs3u9g0
        EAlXi1B9u1kR1OqPaD2YjRvzkzX6dAbb7Bcu2Ityz4PyyN1Qxr9yzoamfwgSWc6P
        9IpBUy4wtRWTwslHkga9uDQ1zPceCOuEIpn20AZ2bc56GhzBF3WBZBUscCJlUxmd
        h88bTLQwhnBVVHsaouWJvlcLb41+q7P8eIZR4fX1NUuUpmnPQ4TKbUawXx1r/AG8
        YkpxbB2WG3hwppVuJEI/biZGvZOaZzqqbHDEcQkzHGxmqjG+CPc4zr9oKhgzpkiF
        tTDvMug5zDqcRdvavUedfY98Fe+SDnlCOisacStJWJH9HiCkvqRZkr2qIxm962Ys
        DklllHgh4L6qZ3wdQYRIQPr/P1D0Ew/S6Fm8kexEyO10hc3IoEGnYWhnWIl2dzFI
        WX/cY9rPE1cBok6Y6Y6Wef8zQy970/TuSiL7xjZKH7ocog/rd4ElFyC67rcSECBE
        KxKWzb4kNGMCAVGVoXyPcJXq35oKKyAyqHLJQzoYjOW6zZzA1U+v6V5YPxpvBgTs
        QbrN5ldLdEbyF9Ef8FAt8pX8hMo8OV5TBicnW9Q8zjr9RJ4t638ePS8g+xGSnLe6
        xha0TMay29a0wpgNcqER0KECAwEAAQ==
        -----END PUBLIC KEY-----
        """
        # B
        And following private key as sender_key
        """

        -----BEGIN RSA PRIVATE KEY-----
        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
        -----END RSA PRIVATE KEY-----
        """
        And teleferic bootstrap node URI https://teleferic-dev.dxmarkets.com/teleferic/
        And assertion by [sender_key] to [reader_public] with hash as assertion_message_hash
        And we set our identity with private key [reader_private]
    
    Given message with hash [assertion_message_hash]
        And we get key from ACL for our address as encrypted_key
        And we decrypt [encrypted_key] with our identity as message_key
        And we get the encrypted message content as encrypted_message
        And we decrypt [encrypted_message] with AES [message_key] as message
        And we extract message body from [message] as message_body
        And we extract assertions from [message_body] as assertions
    Then we break
