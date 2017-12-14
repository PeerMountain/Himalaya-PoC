Feature: AES module
  Read more about PKCS7 padding on https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7

  @wip(stef)
  Scenario Outline: PKCS7 padding
    Given a text <text>
    When I made PKCS7 padding of the text to <bytes> bytes
    Then the hexa result should be <result>

  Examples:
  | text                                    | bytes | result |
  |                                         | 32    |  |
  |                                         | 16    |  |
  | x                                       | 32    | 781f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f |
  | x                                       | 16    | 780f0f0f0f0f0f0f0f0f0f0f0f0f0f0f  |
  | More than 32 byte password padding test | 32    | 4d6f7265207468616e20333220627974652070617373776f72642070616464696e67207465737419191919191919191919191919191919191919191919191919 |
  | More than 16 byte password padding test | 16    | 4d6f7265207468616e20313620627974652070617373776f72642070616464696e672074657374090909090909090909 |
  | __Exactly 32 byte padding test__        | 32    | 5f5f45786163746c7920333220627974652070616464696e6720746573745f5f |
  | __16 byte test__                        | 32    | 5f5f3136206279746520746573745f5f10101010101010101010101010101010 |
  | __16 byte test__                        | 16    | 5f5f3136206279746520746573745f5f |
  | 4byt                                    | 32    | 346279741c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c |
  | _13byte test_                           | 32    | 5f31336279746520746573745f13131313131313131313131313131313131313 |
  | _13byte test_                           | 16    | 5f31336279746520746573745f030303 |

  @wip(stef)
  Scenario Outline: Base64 Encoding
    Given a text <text>
    When I encode it with Base64
    Then the result should be <result>

    Examples:
    | text                                    | result |
    |                                         |  |
    | x                                       | eA== |
    | More than 32 byte password padding test | TW9yZSB0aGFuIDMyIGJ5dGUgcGFzc3dvcmQgcGFkZGluZyB0ZXN0 |
    | __Exactly 32 byte padding test__        | X19FeGFjdGx5IDMyIGJ5dGUgcGFkZGluZyB0ZXN0X18= |
    | __16 byte test__                        | X18xNiBieXRlIHRlc3RfXw== |
    | 4byt                                    | NGJ5dA== |
    | _13byte test_                           | XzEzYnl0ZSB0ZXN0Xw== |

  @wip(stef)
  Scenario Outline: Base64 Decode
    Given a base64 encoded text <text>
    When I dencode it
    Then the result should be <result>

    Examples:
    | text                                                     | result                                  |
    |                                                          |                                         |
    | eA==                                                     | x                                       |
    | TW9yZSB0aGFuIDMyIGJ5dGUgcGFzc3dvcmQgcGFkZGluZyB0ZXN0     | More than 32 byte password padding test |
    | X19FeGFjdGx5IDMyIGJ5dGUgcGFkZGluZyB0ZXN0X18=             | __Exactly 32 byte padding test__        |
    | X18xNiBieXRlIHRlc3RfXw==                                 | __16 byte test__                        |
    | NGJ5dA==                                                 | 4byt                                    |
    | XzEzYnl0ZSB0ZXN0Xw==                                     | _13byte test_                           |

  @wip(stef)
  Scenario Outline: Encrypt steps
    Given a passphrase <key>
    And a content <content>
    When I AES encrypt the content with the key
    Then I have to call PKCS7 padding of passphrase to 32 bytes
    And I have to call PKCS7 padding of content to 16 bytes block size
    And I have to encrypt the resulted content with the resulted passphrase using AES
    And I have to encode encrypted content with Base64
    Given result shoud be <result>

    Examples:
    | key        | content          | result |
    | SecretKey  | MyPrivateContent | Us5mYNORRxDuVPP2jy8CFA== |

  Scenario Outline: Encrypt
    Given a passphrase <key>
    And a content <content>
    When I made PKCS7 padding of passphrase to 32 bytes
    And I made PKCS7 padding of content to 16 bytes block size
    And I encrypt the resulted content with the resulted passphrase using AES
    And I encode encrypted content with Base64
    Given result shoud be <result>

    Examples:
    | key        | content  | result |
    | Test 1     | Sample 2 | y3DwMCeEp5X+sdQChcor8g== |
    | Sample 2   | Test 1   | u8mKQ1ehL7GvA4DASerD9Q== |
    | Chuck 3    | Sample 3 | HSaNhsXBW+RjSuOQkiMslQ== |
    | SecretKey  | MyPrivateContent | Us5mYNORRxDuVPP2jy8CFA== |

  Scenario Outline: Decrypt
    Given a passphrase <key>
    And a content <content>
    When I made PKCS7 padding of passphrase to 32 bytes
    And I decrypt the content with the resulted passphrase using AES
    And I decode encrypted content with Base64
    And I made PKCS7 unpadding of decoded content for 16 bytes block size
    Given result shoud be <result>

    Examples:
    | key        | content                  | result  |
    | Sample 1   | 18cUXD+s/rrBDrpq2CucCw== | Chuck 2 |
    | Chuck 2    | H2gwKlBaFpYizsPzYOHMpQ== | Test 3  |
    | Test 3     | K34qHjcXtEYxZJoBlHuNrw== | Chuck 1 |