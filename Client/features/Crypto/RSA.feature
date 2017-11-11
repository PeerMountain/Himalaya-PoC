Feature: RSA Module

  Scenario Outline: Signature
    Given the following privkey
    """
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
    """
    And a content <message>
    When I calculate SHA256 of the content
    And I sign the content hash with RSA
    And I convert the signature from long to bytes
    And I encode the signature from bytes on base64
    Then the signature and <given_sign> should be equal

    Examples:
    | message  | given_sign |
    | Chuck 1  | SrZEaRP7y9Qn2xTvDxfC73PghNqQ176XemtqQN+T+0jyLE+HJaySDU5jwz513T3VUhgqWuR1eOytc18Ors6FHNbzC5qqApRPv9TN5OEjQs3lEUbQF/iQJlL6U18AWW1Gup1jk5nqly/jKCj//QHDQdwkWPVHdXDW1Ese9Kw16bJn56dzBfljDmIxXb0CgCPP4Cz3TXaN6GLS/K7XDNHuUndJIuxSQHK7Q5uSFC9iqJ9EwevUKRCBl40YdsEqhm95vS/HaqqeXk5W/EZJokT7zesVEsVW6WxFPzTCoL+PHu8Q8UX0FYhU58lbvf36oHfZIdFWRutEk0+EjUHl5GDmx2Km1C7zMt0EzMn1SplOIabAY80AL24WYiZBb9VCUClfPgNx1B7rjtArxVXkkasbse4D9iNrt3TNlJhPt44gPL3eOk6L4T5aneLJGlJMjZRpGbGRwe60f8qMD8fIcYU1s+x43YSRneAyrRgpXXWkdigZ9wkHNp/Pn6LcmjmvbjOqYIGqsY2pUzBs/PV58SzXE3E1ozRLVn3f85G3I9RHPYRbGHY34GvBuSe4qCBt7K/IBazKN2F4VC/quDpExiC4/Q2sCxwBk64Sc0FnpHNXeTZK4ss+RrtInF0tAulUIgR9OZGMSiREQAljdN+MAt5BxYFgz0nj8L/mY4pJaEr4I/0= |
    | Test 2   | DG/+01WHZdG+ZvvRWwasCrToFCvCUj03cDaOmO4pBwgJyJploZ+WLFQ+Ft2Hb0eLNpHO0wxp/saeWe3hJhr2PbKlYAKQQIIhqmxnDiXIiW5HX1Pbaqhvr3EOTTxzk1B4RlPBqI5AS/dWfnJyRMW4jC8J6RaPlAWQRwAKS1VlRhfx8gasCGcVXh1HAFjxrodH886ZcCjm/IC2m/r1UsGPXGlTMRuUFdqZ0/egv5ihS4EM3/Z9jp2gMEgYhR9qDZ1LAYCnK5TTtnPq1FGD11uyZvQdqBb9GuTFyqfyubx7piJDq+D6Ixf18SIAHajXFaCWwW6nMbYFFG4nmokRdVhHpBy31z/i/3x3MtozC6kDWyFhY/bfAXeAa8YMIGEjuyKwJsCSB2c9JRvtsgTmcJ6sfjxHjqTbRgbaIOOX+atVbT2H8zHF5U+7fIMI/gJU9GJyjLxvb+eFv4NoW/5HBnG3NhU9jyYwWUJHtJXAOSniDQj74uxUBp7LmzSfhtZhDhw6BWl18Q121zNgQJttDPVi84Fo1hRfvVOpbn1alwyBA03/gEc5ArXj0OeajEkqq6T4mdiibzqB/x0uxXgqL4H98Dnu4X0M3Ho1dwlxX1ui/DYwLPGA7Ry6HqjDCQYykkIB1AmoCas5xjdPNZxClkwMl6xR5Ouv1fJ9BPkRU5TPesw= |
    | Sample 3 | vYHOlvc3IbyPh7uFW07HuNcAG0KMK+sAEhS75AEFUhGXpZvy9Iowd7Y4G1rqFDpyqUM8wVTpySRrce16+OBaXkZ6mYnjtSxGmovnygCcs/ESFpXp1QLEfcUe+9P+8eKtM8LUta0aDcVPN1qaVoIBZyIiFWh6DizRDVe4lLO5zKFU+lJFlCUk8krPKeC5PSPGz8qeDKsj3GOLPdC2d+3ErPejYNiq96a5sO/CyfkWSZ7wVOn5CpdEnirsJ9E+fTf4CW2gAP03gmbWH2nSTidhPxhTXhBJx8vibZqqxPkoBHRzbLTa+JYK7tLI9iudFneItayqYcLt52xmfEjYcbsRWzWqAdGLGfEdzjoczVQfrZMomF7DidHbPnPxuX6wZZ931DQZe8sU5uWbxxQVscEDxwUjh06Y4flJBSG0yEkqubY9YhuCpHj5EI2PKunUJW1Gtsty0eWRbyhZYjmIG8la/Dw6A4QZ2ahPw7b918zQINEXkEF6fvJldg7SA5RoFqdWqnHyYA4+RKaLy0L+qUFoYX2JtfaZvmapkfzyoSgfGueNT4BCQx0Ll1RgqKVAjUmodGRwoRnBKt2fLo/R7WK001/cCuCkSsVoXkFGN3hmEiiMYUXLEzUzU8/SZMFYqMzL6WYRAB8QCaX2zKxzZgGXd6MERbTuv9ry1LH3s8qjdx0= |


  Scenario Outline: Signature Verification
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
    And a content <content>
    When I calculate SHA256 of the content
    And I decode signature <given_sign> with base64
    And I convert the signature from bytes to long
    Then verify the signature with calculate hash should be valid

    Examples:
    | content  | given_sign |
    | Sample 1 | sEOiXdUayGbThgXu5MDfErwbRNUL7dUyV9+bR7uSiMnLgzmOUCWNmC1i6sdQnHLAvj5hpUmiC5wpkjmTS9D1oQ/Hwy1p+xtl5bFW4H84erx2PEaPXZWpoVwt3ci3opDvxrLwvQLQBVDkJNATsL4m5vf2l/l9G5ecqAlL2MoQddOxcbcB7nvnFIvnnSLsP7fHUlDG8ypW3EyjN6f54q4BdeX6xMPsHiuW1AoxwjYnmnD45iGgkMlV7FsptOgPig2C5o2r2OKg5uopuUHBp5K+eDyv1wMmp6c8AsrIlwe/BKZx92DkVUZ5oZ1g+ilRjHJbLKYLd6mb2c27ClFND5S7UfIgNd2+ks0Ly95sorhHiEdNvRAt5nDN1Eb+0XwEXyWYTadBR0oxsI2jguHsMYdxt+ee91BP2ccKdOx+sVjs4LH4RV1aYUNZnR/TYLX6iL8txGf4SoXwyTJ7Pl+CbKAciH6PzMSQch3ZFPWqn9Am07J3Y63f422FLTlzhcBFTIqJNIOLTi09l0i35uAy1UobrXo3/DL3pHiILci2mFKrkJ6pqE+owYAj8UuuXpBTq+uMgFvUok05AuZN32eyc6kQUpiPEC2hvz6YPLPs6vpAuxiKhRZyxX6Rlu7FfT+3hyn4Eq47KCZi8Su07/ooCDyqxb0WSBfm/NPRf1lkFtAzmhc= |
    | Chuck 2  | tdAo93+YINovhc/UjLvAhlRJ67qa5jn4TYQCWTGEImHE3Yve+GAWCN+c9U8xRCUbrqN9q9WWujfJUyvIlwl8GroPlDkx51qu5uBPlN/mB3EdMXckjMt6ZmexO5nFae+0q/DZhaPnpSvp8PuM4LXTjPNb4cEjPica/xM/foAVk+tHR3zW/oTpeLPepZSLybVYu+Tos/0fxOXIPG8mBj4VJDHkYI1DkHhG3VOGgxpTgDCS/quv9AbpSqNEySyKfGRWmfRLY40MMLzxfok/CxJof1VOURmPqwPxicXCRzz0m2OrMCb51qcf9yIG2kHFk9XeYiySEbPK5RHrWtEPk7j8ttI4W7iJv1lnXtVVZ5/TFNero1fAffkZr0Ff7pbHWZjcxbTXdrkZ3Ryq9K4NzJOgUnEEhvAPAlAbnAm0j5TFkIEA5JezkH8+Zd8LLhx6SHg0O2cCatxf+AKKOnsb37fsaR8RzqaoWFKEmyr6mqBfSmVCpe7Y1jNhz6f5nw7ohcbI7w9w4s0WRqQcno6SnjcLMUsE/Q0Y18UldPlaRMguufz3yg0nwBw+h0oXOqSDu9CpOb6Ib5U8Y7H7HxDJg8mGIDfEmJDmqy9OIYrLhZ0CrBY12tln2UoL32fOaCdgUYploEpxMOPqxN4EYGhqa7cesZnheoZ+XV4c3K5oaZdC888= |
    | Test 3   | V3pgsTq6GJVu2CPJfUZBXkFHH2t2apqYtQS/xVfYpoil55NwNgLnH+7eoYd/3Uh7N+F2sKMC80C2hf+8KCGpMotz5L3SoQ+nuXgWSF2dMxRh9KUOaQFwiX4yojiJjxFAsLfDZEIIU9eECFQzyUFWVNF0cHNFg0pwjBrdjb+WPRsgXrWwOYKWQoJdZLLuXaIwcG0mjgI4V/15d6cnq5j2i9XymBA/C+7WvBG2wRTz4XU5GrBqEf4fKS4Cg7fbUYPAHNwy0gS3v98UaHgskU7EsdgJPkTGXgLP1t1zipt92mZHQktLdtiR/J+PnjknqEPRYMthGtnQMdqDUzVgj3byVLvp6WM5buaN4ZT6mDxLC84kCemLnUZMv5tdAjF3DO/UnXCA/Obft1jhFzRswUgZr0DxLNG9KrCDrietNE+328fuCujnSIGdIFHQgDidj2ilrl9lJGc1ZgJg1tjQ444ITe6Tx0tXx2BPiEqjqcB5zbpd7M61XKR2DGsFyxrqpC83sbtjI9afsmPK2Zlyh+kH0wvkWEgsVIiTVOxZbQWnG6kIXcs1obxflmccSBrTQg/GmPuV6suEM+6YhMdeAfvOOhFnH79lX4knZlHf8fdZRisTdfMeagPsX/C09nD4Np1Yag6mS5cdHwPSzxXZb1CDYLEw0Gz3EKV/thNVfTQagRc=z |

  Scenario Outline: Encrypt
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
    And a content <content>
    When I encrypt the content with RSA
    And I encode the result with base64
    Then the encoded content should be equal to <given_encrypted_content>

    Examples:
    | content  | given_encrypted_content |
    | Test 1   | NSHV4njZuQbvwiBSK/gfBMDYmuhVffWtjuz59xnIokMY73ixBzek1fnEkmnChDZYgIwFQDjuaBJ3cvQJmoAQHQSoVjjCDcIdlV0bRLqIQzKv3U5TKXGf8FtJX80myh8F0ClfCzTkBbUZQNUQJEF4VxoZ08Fh+VVtqf+YGkh4ZmqbigVQ/XLkiNU9MMb7j6qidauhcaj9vPMnPCTbA7XSc+hVVXSUjZi+hJYa16pqXUgjuewUyXJXdk49nuza6RVH4lZ0RqNlv92mNosv5MDYCjuIguwAqaYwaR7f862Gogc/tFLDW/S1fXubfwbRQsZN7nxgB/F8s9rWafjr9hLSysZ/ep2IvXbB6p3g87F4GmIjdXq5dRkD/i4J/9VrV3Oii8x9swW7asv7S7/2fJNGozUtfrL9AygYiJrWUihIDnVnJKFbZDi3UugVIoVAOZ3tJHhUd67MO//POaru5PKdNIM2fqUsHmjkA5wGGl1BouswsO1PLjDpxHQkGvpbKzE0jmW88028WNGXiutOYSJIMRHLrJbsdoBb/hBcTYPb8f66XLPBRWIdFEykQRB91R1LfS2fWTHoyW8vqUkKsvAZrPiKLqNzAKNWIn/W3gmIL66gi2a5MITRbh04fq+PmAF8f/n3xxY95rlctcbVvGiJDxEHShm6xe3cGBq6YkcPKL4= |
    | Chuck 2  | Uwq/VsoyScNbSvfzonKDb7+HuB/afGewroGn7fR+smlak6irJr58etbWAdFT56tsmpJstR+nWo9Za0t67mGut0gyyrTuFZ8xX4OktwoMsEqsxUQFX8mmJ4F2tZPaxffw35uLgbNKeda8AUfQDbmWSLBB0ZvWDLezqgaAsKT+lGZ5ogW9kPT1dWLVHS1jdqykUloWj6zopYo7f32SuoKoUAdxPKMRjLxnb8+x0zJ09WTzzRlQKCJ/wrgU+Ujoi34q3cAgUlLIYMz50SnV8hUSayxuAD83Mj7GSHm0C6mYUJl4TkbVjaLakTihke0L3w1NkJ8xwDrUzlgiV+2B8w9QAPIwBG51+YJQmfPQk5UqTMVxwHulih7DfC/OVYHZIfkbSX6e7bZfPypZz91vPgpMelmp9M219vN0CMsZYHVLP59ghfpdJNEhjwajoel2LeHlqW4pAFDjs9S7gBk2ebwQ1tqoHFNev9K57KtusRUbbaTpWHOjCJJRuYhG4ZukRv7cHvGnBwbiKaxu/Kj/Lyi1tX2+TOhvnDB2qiKuZtSciNP4MsVzfWBrgWcblpo/FTdwX2SjyHgwnNFMihXey1JO/pKSzs0pNuiJ7xA+pKKnC0XB1g9noRFh5aYWhsEDQA+fXzBnUpXxdy6ow7EPIAA8Z2N3lv5EGjLOH31mtLN8I38= |
    | Sample 3 | D7UDDcKyaDP07jwW7z43Le3musCVsDcVRjDzEXsg6/BK0kSH/mfmv97AqNDxX9eI025aw1goFJTMQ6ljWAPKaFxOWtl7iQQPzm8htyMivaPHnsXRqFckj40WquIJk1wN64cuYSYSnrqTOx1J37Y54tjlNTF1/kJykvkiVkAbUN2n0G8MmUXodBKrqsVOBCKnlYaNaxV1BKQS5CRhoVwi1cojXL+PMZ54azLpjqoFJ840nBU4OiZ6jBCtozhtnJMm7t5ari7+WNxhwjg2PRwrNMu1n7JWOEEPFUCLydQg8ambhtm8NBBSC6Tm3MOkdQCfvj5kfzQvK6QLGaMm7S8mpxtN4fQRjgYBe6aEaF4n7GrGemQ1drTkcZj3jgtK1Ci0GfbAw1UH4hfoTxse+rEugtQO+06SdzF9MoXePK3p4PbA9hs+3UeCccZPhZqPu9o/j9tXOdgPxqruKHOLBZHW680XFHzBjGud+KbgItEkrt5cNNmWLD2tBi7zsTShpOl6KNjOIHIQVZ3gS08HlmtPYHRf+3c2SZZERHmYM4oGTMYK0eWhAumS3M/aU/kaOwQXr0b1N/2tpk9kiTlasuigoSAsseIq1mu1VbehZ3WjXa9imhwqWkxRp1R8M0C7ZF95Vt2rJc1uVc8YYF7pVVkln6SVv2uG8yeEvlfiWU60bDQ= |
  
  @wip
  Scenario Outline: Decrypt
    Given the following privkey
    """
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
    """
    And a content <given_encrypted_content>
    When I decode the content with base64
    And I decrypt the result with RSA
    Then the decryped content should be equal to <given_decrypted_content>

    Examples:
    | given_decrypted_content | given_encrypted_content |
    | Test 1                  | NSHV4njZuQbvwiBSK/gfBMDYmuhVffWtjuz59xnIokMY73ixBzek1fnEkmnChDZYgIwFQDjuaBJ3cvQJmoAQHQSoVjjCDcIdlV0bRLqIQzKv3U5TKXGf8FtJX80myh8F0ClfCzTkBbUZQNUQJEF4VxoZ08Fh+VVtqf+YGkh4ZmqbigVQ/XLkiNU9MMb7j6qidauhcaj9vPMnPCTbA7XSc+hVVXSUjZi+hJYa16pqXUgjuewUyXJXdk49nuza6RVH4lZ0RqNlv92mNosv5MDYCjuIguwAqaYwaR7f862Gogc/tFLDW/S1fXubfwbRQsZN7nxgB/F8s9rWafjr9hLSysZ/ep2IvXbB6p3g87F4GmIjdXq5dRkD/i4J/9VrV3Oii8x9swW7asv7S7/2fJNGozUtfrL9AygYiJrWUihIDnVnJKFbZDi3UugVIoVAOZ3tJHhUd67MO//POaru5PKdNIM2fqUsHmjkA5wGGl1BouswsO1PLjDpxHQkGvpbKzE0jmW88028WNGXiutOYSJIMRHLrJbsdoBb/hBcTYPb8f66XLPBRWIdFEykQRB91R1LfS2fWTHoyW8vqUkKsvAZrPiKLqNzAKNWIn/W3gmIL66gi2a5MITRbh04fq+PmAF8f/n3xxY95rlctcbVvGiJDxEHShm6xe3cGBq6YkcPKL4= |
    | Sample 2                | r7Vr/nJnrg61UuNq4tWflMh+cuOoaEQwbiLSL+TQzP7DDBOtnLhQklDoffp8thIlJF/3PvP0n3zvrlpfzIrXdy20trpV5XGsYeST22ygVI6ZvDwtzC3yQR5yLHumt8NmH5l2XObLXArenq5kDDHvSqp34I2lk6bDYqp6nwta+q7WZpbme/SjRmi9/Ciwu/R1HTeHzcGsErp8xfKcEX9Vt5XNfmTfVdklwlp9g76LGGkRIUPwrUF8EcOLz35Wemp3Jl+xu3cDj/rR40dLy4/gpvRPfrdZAjRPKJSWayiGxSIGBQX/AyVDtnWHy5vaqMPdU0h8ujtTCdEihvCezUop50/gjPoxpjuju61NkO9U7e7LAujX4PDduhD4gvi4Ef4UwhDuMSMFJ6w3tL4Yen6ZA6hOIbLvuEKcaTZaPXHMwJdvxJNXriibJt6zuYP01NuW2N8JqZebY4iyvmrURsNQtiG1GbKU79kirTxuyRomyqWCGP8ytEpwbetdVN3NOTrDrfVuQi5EpIEcj7IUZ34D6EK4YNQrj/iNIcVlp0HV7PGzr5Nza5yeaq+5j/AYyeO5QDY2twLqMyUg7uxrK+s//K36INzw7kfa86g0a53TazWzjnkveRiyvXRZzU5qQ2R/1ox1p0EcaNMblevz3uAl+3gpdAdItx74ooG3wyjSLa0= |
    | Chuck 3                 | G0P6CMhyHxur0o6QSOquqt6ktyDW91l6PB/52nC+Q9SGLRDFu/tUizjvcnu4rA0jaVcvJLjkad6F+TQJRURm2wBncREoh+kcY1lcfVXHegRYYJgzV1RCniJwzPPs4Pisl0aj1NPl/otHZvpWNOP7R49olYF3Pvw9D4iC6G9LlC1iirYy3tQkGr7YuKNePPiqgBkdp9ywwhc/1nvsW+iXjKg5qBdV94sCwdROp3z3iCkPrRSHGipJT3+SrdVAsWTx9fxz+Jdhtfsb4NKJ9lPx5abzLIHu+K3TXUo6CZoqiYM1duQEZ290XIGXaba40w02NoLlXDux6XKEpGglS1aXS6RItF+bebmw7kQlTgAiZj3oRgI0BNLvAEZySYN8CCxYkdwvK2vOeyJMsxj3V4OPxHbvySScWnyGRIvvVQrl8BWSjxBxHQFe6xlEHIwIcBbuBmOCvCKyhNwhdXgesV0Z84m8rElVMWWJqTD434ABYIxCsAsOmB6oJ4ElG7y/G+6/fPTReQwd96X5qNjPfrqyDpvpwNea+rQukJetLseFpsYcPIaN2emOMMs9hpymBju5ruaBZD0bLBXwKtowfnbws+Abil3tUslJtJqXbVExpPnr4+r3fkYslvw+3ZGT593o4CYSfkgmXit41AeqoMM2osYioloSbLvboPpuv9vyTKw= |