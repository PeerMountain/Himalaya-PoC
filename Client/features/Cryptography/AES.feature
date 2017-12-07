Feature: AES module
  Read more about PKCS7 padding on https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7

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