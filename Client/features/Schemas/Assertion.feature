Feature: Assertion Message
    @wip
    Scenario Outline: Generate object container requirements
        Given user attaches base64 encoded object <object>
        
        When we calculate SHA256 hash of <object> as object_SHA256
        Then we check [object_SHA256] and <expected_object_SHA256> are equal

        When we encrypt <object> using AES with key <container_key> as encrypted_object
        Then we check [encrypted_object] and <expected_encrypted_object> are equal

        When we calculate SHA256 hash of [encrypted_object] as encrypted_object_SHA256
        Then we check [encrypted_object_SHA256] and <expected_encrypted_object_SHA256> are equal

        Given following private key as private_key
        """
        -----BEGIN RSA PRIVATE KEY-----
        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
        -----END RSA PRIVATE KEY-----
        """
            And following private key as reader_key
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
            # And teleferic bootstrap node URI https://teleferic-dev.dxmarkets.com/teleferic/
            And teleferic bootstrap node URI http://localhost:8000/teleferic/
            And teleferic signed timestamp as teleferic_signed_timestamp
            And we set our identity with private key [private_key]
            And we create identity reader_identity with private key [reader_key]
        When we XAdES-T sign [object_SHA256] as object_SHA256_signature
            And we XAdES-T sign [encrypted_object_SHA256] as encrypted_object_SHA256_signature

        Given compose meta_list as literal
        """
        [
            {
                "metaKey": 1,
                "metaValue": "Pepe"
            },
            {
                "metaKey": 2,
                "metaValue": "Sarasa"
            }
        ]
        """
            And we pack every element in [meta_list] with Message Pack as meta_list
            And we calculate a 40 byte salt for each element in [meta_list] as meta_salts
            And we calculate salted hash for each element in [meta_list] with salts [meta_salts] as salted_meta_hashes
        Then we include salts [meta_salts] in meta list [meta_list] as meta_list

        Given valid_until is datetime 2018-05-10
            And retain_until is datetime 2018-05-20
            And context var container_key is <container_key>

        Then we compose assertion with keys
        """
            'containerHash': {encrypted_object_SHA256},
            'containerKey': {container_key},
            'objectHash': {object_SHA256},
            'metas': {meta_list},
        """
        When we set assertions as list
            And we append [assertion] to [assertions]
            And we compose assertion message body assertion_message_body with assertions [assertions] and body type 0
            And we compose message content message_content with [assertion_message_body] and message type ASSERTION
            And we set containers as list
            And we compose container with keys
            """
                'objectContainer': {encrypted_object},
                'containerSig': {encrypted_object_SHA256_signature},
                'saltedMetaHashes': {salted_meta_hashes},
                'objectHash': {object_SHA256},
                'containerHash': {encrypted_object_SHA256},
            """
            And we append [container] to [containers]
            And we set readers as list
            And we append [reader_identity] to [readers]
            And we compose message with [message_content], passphrase sarasa1234, readers [readers] and containers [containers]
        
        Then we send [message] to teleferic with container key [container_key] and save response as teleferic_response
            And response [teleferic_response] is OK

    Examples:
        | object           | expected_object_SHA256                       | container_key | expected_encrypted_object | expected_encrypted_object_SHA256             |
        | utvu8A==         | RbUuANM6CTG3WUNkNPsc7ia9iY87HKc0LoQZsT/KEvs= | sarasa1       | IgzAp08p7dHnaccZ9wbwXg==  | 9li9ozDxnPexSW4vQK1fcGCMx9Fp4TMXu0pCwd5sRJ0= |
        | 0WqSAQ==         | InccYmBaAj+sTJJ3VWOPqqoJ6xcu9wa78Sm1Atg0V4Q= | sarasa0       | 8qJA0KN/Ky9zb+lbQGvP1A==  | 4TAJ7dyIUMpvpaDDnHjchJuVdn64P5DjSJn/hFgtj+c= |
        | 0WqSAQAAAQmS     | 0MUuYJ4X2qLrEmzYMTcg3TrBoIbR/MEZiQqBnk/reTk= | sarasa3       | 6HlIZ3oDyBkWVjuU/9uFvw==  | fjcK0da8qwdIgfLiJqihQ7PlUc4SH1nDt2GWV9pkHdk= |
        | 0WqSAQAAAQmS/hGe | VZIM0Ny3VGaAeJ9jro5ql/9ccTNGMKFLbdICeFe4Z5M= | sarasa4       | G4QvaTvqRfSzui4bQ7XlXg==  | jYeVTtpgqJscV7EIsDDnmRFbViGQOcai1qaPHQuMc9w= |