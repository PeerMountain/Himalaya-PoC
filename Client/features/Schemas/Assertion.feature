Feature: Assertion Message
    Scenario Outline: Generate object container requirements
        Given user attaches base64 encoded object <object>
        
        When we calculate SHA256 hash of <object> as <object_SHA256>
        Then we check <object_SHA256> and <expected_object_SHA256> are equal

        When we encrypt <object> using AES with key <container_key> as <encrypted_object>
        Then we check <encrypted_object> and <expected_encrypted_object> are equal

        When we calculate SHA256 hash of <encrypted_object> as <encrypted_object_SHA256>
        Then we check <encrypted_object_SHA256> and <expected_encrypted_object_SHA256> are equal

        Given following private key <private_key>
        """
        -----BEGIN RSA PRIVATE KEY-----
        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
        -----END RSA PRIVATE KEY-----
        """
            And teleferic signed timestamp <teleferic_signed_timestamp>
            And compose <object_signature_dict>
            """
            {
            objectHash: <object_SHA256>,
            timestamp: <teleferic_signed_timestamp>
            }
            """
        When I format <object_signature_dict> with Message Pack as <packed_object_signature_dict>
            And generate RSA signature <object_signature> using <private_key> of formated signable object <packed_object_signature_dict>

        Then we check <object_signature> and <expected_object_signature> are equal

        Given compose <meta_list>
        """
        [
            {
                2: {
                    "metaValue": "Pepe Sarasa",
                },
            },
            {
                3: {
                    "metaValue": "\x12\x23\x41\xfe\x11\x9e"
                }
            }
        ]
        """
            And we calculate salt for each meta
            And we calculate salted hash for each meta as salted_meta_hashes

        Given <valid_until> is unix timestamp for 2018-05-10
            And <retain_until> is unix timestamp for 2018-05-20

        Given we compose assertion message body <assertion_message_body> with <valid_until>, <retain_until>, <encrypted_object_SHA256>, <container_key>, <encrypted_object_SHA256>, <object_signature>, <meta_list>


   Examples:
        | object | expectedObjectSHA256 | containerKey | expectedEncryptedObject | expectedEncryptedObjectSHA256 |
        | utvu8A== | RbUuANM6CTG3WUNkNPsc7ia9iY87HKc0LoQZsT/KEvs= | sarasa1 | IgzAp08p7dHnaccZ9wbwXg== | li9ozDxnPexSW4vQK1fcGCMx9Fp4TMXu0pCwd5sRJ0= |
        | 0WqSAQ== | InccYmBaAj+sTJJ3VWOPqqoJ6xcu9wa78Sm1Atg0V4Q= | sarasa0 | RRqInN+GYjl7hHl4iKW7hg== | QHJ87QgHpkyxweV9ctRu2fl9ih0jxwtya9viIKrr1Eg= |
        | 0WqSAQAAAQmS | 0MUuYJ4X2qLrEmzYMTcg3TrBoIbR/MEZiQqBnk/reTk= | sarasa3 | 6HlIZ3oDyBkWVjuU/9uFvw== | fjcK0da8qwdIgfLiJqihQ7PlUc4SH1nDt2GWV9pkHdk= |
        | 0WqSAQAAAQmS/hGe | VZIM0Ny3VGaAeJ9jro5ql/9ccTNGMKFLbdICeFe4Z5M= | sarasa4 | G4QvaTvqRfSzui4bQ7XlXg== | jYeVTtpgqJscV7EIsDDnmRFbViGQOcai1qaPHQuMc9w= |

    
