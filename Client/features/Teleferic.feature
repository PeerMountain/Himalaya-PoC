Feature: Query bootstap node information
  In obtain informetion from Teleferic node
  As a client

  @wip
  Scenario: Get Teleferic public key
    Given following query
    '''
    query{
      teleferic{
        persona{
          pubkey
        }
      }
    }
    '''
    And bootstrap node url http://teleferic.local:8000/teleferic
    When I send query to bootstrap node
    And get property data.teleferic.persona.pubkey from query response
    And decode property with Base64
    Then decoded property should be
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
  
  @wip
  Scenario: Get Teleferic Address
    Given following query
    '''
    query{
      teleferic{
        persona{
          address
        }
      }
    }
    '''
    And bootstrap node url http://teleferic.local:8000/teleferic
    When I send query to bootstrap node
    And get property data.teleferic.persona.address from query response
    Then property value should be iZUTgbvR4iaNYzPgJFodTtT7xJxhyusyoyChCvsbXLH4rRgv3sgm2R2ksh8yRPnhumH
  
  @wip
  Scenario: Get Teleferic signed timestamp
    Given bootstrap node url http://teleferic.local:8000/teleferic
    And bootstrap node pubkey <bootstrapNodePubkey>
    And following query
    '''
    query{
      teleferic{
        signedTimestamp
      }
    }
    ''' 
    When I send query to bootstrap node
    And get property data.teleferic.signedTimestamp from query response
    And decode property with Base64
    And unpack property with Message Pack
    Then result should have signature property
    And result should have timestamp property
    And signature should be valid for timestamp
  
  

  