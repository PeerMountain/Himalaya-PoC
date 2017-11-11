Feature: Identity module

  Scenario: Address generation 1
    Given the following pubkey
    """
    -----BEGIN PUBLIC KEY-----
    MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAz614m40n+FfHIzLNFKaR
    14ownMR6JAmtZ2UV5XUCfhrQxStGnVkwIKxOsg3ZgCsjbHRfMx2NDlubk7jmj7qh
    Jy5YRuAViWke6dnJ6CbE6W2ErUXwlqbpWwFRaeLof/4Hb+PhwpXYBzBBERAk8rrC
    /yN8kYqvMUBd1mi6w+8StLkqvg5MRnx/g5/yF+lvGOeHfRMox2MtUD7IM6Z5Z4ym
    axNe3faOCl8oBTKypLezlM+phQ0Uk4uMejA6YoSFv+f5pf4JJnx6DMzSWSvo4GPX
    /OYKTfmSn8XNT5eCYmhwzF3vRTw+AffR4JHLTk23ER4uJpaw99Iiqo4yDbJNYgro
    dXMvGhYh6OoFDovFXUbcFzP52dg5hmoMYn9eZLwBKIAMcSMPNxJks38kZmr/hHCc
    9NLZbHRkoJ9dn2nRwD4YxRuV03cIsL+KDbn0u3uTH9aExkxEQ44IHsAnHlV5NxDb
    JHF0xMcFYoJOouKDFaD4FUcYtdQ2VheuFOEfM9aVutOKnTacmLHnkHmg6wH/5GhP
    zAWYWD376SyKKPqNcKFomvONIkNKiCX9HBtIUZl68skpihdocPWEkOPCwcAhZNmp
    P6YsepN15X/tAf67x/ssZ7ktACa2Kc9rSVA4NxWBvmxrnQ5UlVPzfSqWlcDtVVnP
    +xZeGuS3KJx307sqM0lCYf0CAwEAAQ==
    -----END PUBLIC KEY-----
    """
    When compute SHA256 hash of pubkey
    And compute RIPEMD160 of resulting SHA256
    And prefix resulting RIPEMD160 with [1, 0] bytes to generate the base address
    And apply SHA256 two times over resulting RIPEMD160 to generate the checksum
    And append last 4 bytes of resulting checksum at the end of base address to generate the address
    Then the addres should be iZn2hyWChp6hkHEobZNdE9vmruR3MNVQZVFoBMc6PHEvKmaQM1jKoEC1uDF5Qf7deXN

  Scenario: Address generation 2
    Given the following pubkey
    """
    -----BEGIN PUBLIC KEY-----
    MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmbuljbgw5JfS9GICTGSK
    IPAPez9hFsdu/0tKCgJDMcSqqaG3gmk7XhPjqGUzdslTt2WAViYXxQGcKUAXqtn3
    6Yl+gfwWjV2oRK9fsGNuZ0rcU9nJK2/QYpvT51AThrHgOmhPzGB2aMDwRNJHf05L
    Xf+C0rC5J9mIXRFxeom1CKloCAd5TdiWoSAzTBIixTeQJEIDzXma93N9HcfZfMMp
    ftFdzgmAD4JaOPCY+6RD/FluOGbgoueL88xNma50e6GXB4/XUv5Z6ZyEZ3VhI23X
    EZg3JkWslUdpBmjRb6rS0RQGwlcPTIZwCa6Ln1fHM35fHE42B3UCUCu66MVs/rzZ
    maP4i7o5xJ+V52EbEcnNhwBGnQLPK2RoH73usz10H5u3vE9tPh4+iOmMy6tkKaqE
    rMxbDbEqpJln8fzxsJ7kK5UY9QZnWpRayVNsqw5QHF5TENKzXpJVauvvn8SuCY16
    ie7IYfrCnC4ijlYUDOWOJldFXWWNwE88kC3AVwkGFGpHtxiOU/X2gn+ipFzFdvhC
    0S0rlp9KZ++MHWCm+p58oQaSiVax3EGj3YsbE/4LfNSzhgjAewJ9rbsGqFXpK4Zr
    yqMxnRNpuyMqsmtluZGP7Rh0rm+GYBqln2n0Zgxh+s8XEBBepUWx8HOOITDD89Un
    wBYg4BdfLzgK9AP5Kpv2VO8CAwEAAQ==
    -----END PUBLIC KEY-----
    """
    When compute SHA256 hash of pubkey
    And compute RIPEMD160 of resulting SHA256
    And prefix resulting RIPEMD160 with [1, 0] bytes to generate the base address
    And apply SHA256 two times over resulting RIPEMD160 to generate the checksum
    And append last 4 bytes of resulting checksum at the end of base address to generate the address
    Then the addres should be iYYKMxZzf31xixNbF8NhjwNHp6nk4M8YKj1msbbgXFoWW78LsgKQNCGhxrbZTQ8NZL6
