Feature: Query Teleferic identity information

  Scenario: Get teleferic pubkey
    Given pubkey of Teleferic
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
    When send pubkey query of teleferic
    Then we will have equal pubkey

  Scenario: Get teleferic nickname
    Given nickname is "Teleferic"
    When send nickname query of teleferic
    Then we will have equal nickname

  Scenario: Get teleferic address
    Given address is "8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL"
    When send address query of teleferic
    Then we will have equal address

  Scenario: Get and verify Teleferig signed timestamp
    Given pubkey of Teleferic
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
    And current timestamp as initial_timestamp
    When we send signed timestap query of teleferic
    Then we will have timestamp between initial_timestamp and current timestamp
    And we will have valid signature according Teleferic pubkey