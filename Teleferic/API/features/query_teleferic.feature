Feature: Query Teleferic identity information

  Scenario: Get teleferic pubkey
    Given Teleferic has pubkey 
    """
    -----BEGIN PUBLIC KEY-----
    MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvibs6QJ23DtU01mLVo6F
    B9eyj12FpPHvgFvQ39zdRFnZ3jxqvFxENWBFrBV4x11enh4U3djBg2QhYuiEVYlf
    Tto9NEGQtRz5g5kaM3yiZMVXIkyVmdXvU0cSsQqQP00lt2tm4zdClxVvwt3oN2Kn
    xLH6aO/ENw64fp4rqSq8zJcjYNBGdVjFSNkWj7wxeOrGgUockIDxGmlfcbF/YRxL
    PrJbEerx6ClkRwPVlgof8Lvs2uaEcPuO0POC3R3+sMVE4d627tAl6KR2eW/98Rdn
    I2bQYcUzK9L9/X3lU28L5sUJQBqtsoEcEbOYxylAEkBm9jPn71fV2245oKbs6YBm
    hRNx+lnw9DugLrB4T2Yzu+3JNR5FNXD+SkW8Ay1vcPmAeMEAsvHoXNUxVJzd5hwD
    FIMrDuUuiP7jF+PNh4SGaUgUIgbk36rrgMP8z0xrnbENh9/uHhBSahRHb7a3DAwY
    dwMdk5AZm3lGWL9+I+YPFEHpSY6zy3y9ZNxcpq2LDvERMMW6NqHue8tPII6utT6N
    1ExGn2O6pi7RQEs7ZvK4Mpeys5ZSsfcnFbRMrNVbYBq+btUYw1/FP/P/YGJ7CQHl
    ID6ytYdrODPBftAv4e1avmqCit+7MZyJME2zxG71kBJa59qcvQXf3AoZxfj0tnHG
    onmwCjRva9XmguDORNL460sCAwEAAQ==
    -----END PUBLIC KEY-----
    """
    When I query the pubkey of Teleferic
    And decode teleferic pubkey with Base64
    Then the pubkey should match
  
  Scenario: Get teleferic pubkey
    Given Teleferic has pubkey 
    """
    -----BEGIN PUBLIC KEY-----
    MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvibs6QJ23DtU01mLVo6F
    B9eyj12FpPHvgFvQ39zdRFnZ3jxqvFxENWBFrBV4x11enh4U3djBg2QhYuiEVYlf
    Tto9NEGQtRz5g5kaM3yiZMVXIkyVmdXvU0cSsQqQP00lt2tm4zdClxVvwt3oN2Kn
    xLH6aO/ENw64fp4rqSq8zJcjYNBGdVjFSNkWj7wxeOrGgUockIDxGmlfcbF/YRxL
    PrJbEerx6ClkRwPVlgof8Lvs2uaEcPuO0POC3R3+sMVE4d627tAl6KR2eW/98Rdn
    I2bQYcUzK9L9/X3lU28L5sUJQBqtsoEcEbOYxylAEkBm9jPn71fV2245oKbs6YBm
    hRNx+lnw9DugLrB4T2YzU+3JNR5FNXD+SkW8Ay1vcPmAeMEAsvHoXNUxVJzd5hwD
    FIMrDuUuiP7jF+PNh4SGaUgUIgbk36rrgMP8z0xrnbENh9/uHhBSahRHb7a3DAwY
    dwMdk5AZm3lGWL9+I+YPFEHpSY6zy3y9ZNxcpq2LDvERMMW6NqHue8tPII6utT6N
    1ExGn2O6pi7RQEs7ZvK4Mpeys5ZSsfcnFbRMrNVbYBq+btUYw1/FP/P/YGJ7CQHl
    ID6ytYdrODPBftAv4e1avmqCit+7MZyJME2zxG71kBJa59qcvQXf3AoZxfj0tnHG
    onmwCjRva9XmguDORNL460sCAwEAAQ==
    -----END PUBLIC KEY-----
    """
    When I query the pubkey of Teleferic
    And decode teleferic pubkey with Base64
    Then the pubkey not should match

  Scenario: Get teleferic nickname
    Given Teleferic nickname is "Teleferic"
    When I query the nickname of Teleferic
    Then the nickname should match
  
  Scenario Outline: Get teleferic nickname
    Given Teleferic nickname is "<nickname>"
    When I query the nickname of Teleferic
    Then the nickname not should match
  
    Examples:
      | nickname  |
      | teleferic |
      | teleferiC |
      | tEleferic |
      | teleferic  |

  Scenario: Get teleferic address
    Given Teleferic address is "iZUTgbvR4iaNYzPgJFodTtT7xJxhyusyoyChCvsbXLH4rRgv3sgm2R2ksh8yRPnhumH"
    When I query the address of Teleferic
    Then the addresses should match

  Scenario Outline: Get teleferic address
    Given Teleferic address is "<address>"
    When I query the address of Teleferic
    Then the addresses not should match

    Examples:
      | address |
      | iZUTgbvR4iaNYZPgJFodTtT7xJxhyusyoyChCvsbXLH4rRgv3sgm2R2ksh8yRPnhumH |
      | iZUTgbvR4iaNYzPgJFodTtT7xJxhyusyoyChCVsbXLH4rRgv3sgm2R2ksh8yRPnhumH |
      | iZUTgbvR4iaNYzPgJFodTtT7xJxhyusyoyChCvsbXLH4rRgv3sgm2R3ksh8yRPnhumH |

  Scenario: Get and verify Teleferig signed timestamp
    Given Teleferic has pubkey <pubKey>
    And the current timestamp is <initial_timestamp>
    When I query a signed timestap of Teleferic
    And I decode signed timestap with Base64
    And I unpack signed timestap with MessagePack
    Then the timestamp will be between <initial_timestamp> and current timestamp
    And the message should have a valid signature according to Teleferic pubkey