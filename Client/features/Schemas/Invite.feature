Feature: Invitation Message
    Scenario Outline: Generate and send an invitation message

      # Generate invite name
      Given secret passphrase <passphrase>
      And secret invite name <secretInviteName>
      When I encrypt using AES module and given passphrase
      Then the resulting encrypted inviteName should be <inviteName>

      # Generate invite message body
      Given a bootstrap node url <bootstrapNode>
      And bootstrap addrress <bootstrapAddr>
      And offering registred Persona address <offeringAddr> (Rigth now only teleferic Persona is registred)
      And service announcement message SHA256 hash identifier encoded on Base64 <serviceAnnouncementMessage> (not defined yet)
      And service identifier <serviceOfferingID>
      And encrypted invite name <inviteName>
      When I compose invite message body sorting attributes alphabetically
      And format message body with Message Pack
      And encode resulting message body pack with Base64 
      Then resulting messageBody should be equal to <messageBody>

      # Parse invite message body
      Given message body content <messageBody>
      When I decode message body with Base64
      And parse resulting message body with Message Pack
      Then bootstrapNode attribute should be <bootstrapNode>
      And bootstrapAddr attribute should be <bootstrapAddr>
      And offeringAddr attribute should be <offeringAddr>
      And serviceAnnouncementMessage attribute should be <serviceAnnouncementMessage>
      And serviceOfferingID attribute should be <serviceOfferingID>
      And inviteName attribute should be <inviteName>

      # Compose invitation message content
      Given 40 bytes random salt <dossierSalt>
      And we encode dossierSalt with base64 as encodedDossierSalt
      And message body type <bodyType> equal to 0 (Invitation)
      And message body content <messageBody>
      When I compose invite message content sorting attributes alphabetically
      And format message content with Message Pack
      And encrypt resulting message content pack using AES module with public passphrase "Peer Mountain"
      Then resulting message should be <message>

      # Calculate message hash
      Given message <message>
      When I compute SHA256 hash of message content
      And encode resulting message hash with Base64  
      Then resulting message content hash messageHash should be <messageHash>

      # Calculate message body hash
      Given message body content <messageBody>
      When I compute SHA256 hash of message body
      And encode resulting message body hash with Base64  
      Then resulting message body hash bodyHash should be <bodyHash>

      # Calculate dossier hash
      Given message body content <messageBody>
      And 40 bytes random salt <dossierSalt>
      When I compute HMAC-SHA256 hash of message body with given 40 bytes decoded salt
      And encode resulting message body hmac-hash with Base64  
      Then resulting dossierHash should be <dossierHash>

      # Generate message signature with 4096_a.private key
      Given following private key <privkey>
      """
      -----BEGIN RSA PRIVATE KEY-----
      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
      -----END RSA PRIVATE KEY-----
      """
      And messageHash <messageHash>
      And teleferic signed timestamp telefericSignedTimestamp
      And compose signable object
      """
      {
        messageHash: <messageHash>,
        timestamp: <telefericSignedTimestamp>
      }
      """
      When I format signable object with Message Pack 
      And generate RSA signature <signature> using <privkey> of formated signable object
      And compose signature object
      """
      {
        signature: <signature>,
        timestamp: <telefericSignedTimestamp>
      }
      """
      And format signature object with Message Pack
      And encode resulted signature with Base64 into messageSign

      # Send message
      Given a bootstrap node url <bootstrapNode>
      And sender address <sender>
      And messageType <messageType>
      And message hash <messageHash>
      And body hash <bodyHash>
      And message <message>
      And dossier hash <dossierHash>
      And following mutation
      """
      mutation (
        $sender: Address!
        $messageType: MessageType!
        $messageHash: SHA256!
        $bodyHash: SHA256!
        $messageSign: Sign!
        $message: AESEncryptedBlob!
        $dossierHash: HMACSHA256!
      ){
        sendMessage(
          envelope: {
            sender: $sender
            messageType: $messageType
            messageHash: $messageHash
            bodyHash: $bodyHash
            messageSign: $messageSign
            message: $message
            dossierHash: $dossierHash
          }
        ) {
          messageHash
        }
      }
      """
      When I compose variable object
      """
      {
        "sender": "<sender>",
        "messageType": "<messageType>",
        "messageHash": "<messageHash>",
        "bodyHash": "<bodyHash>",
        "message": "<message>",
        "dossierHash": "<dossierHash>"
      }
      """
      And send mutation with variables to bootstrap node <bootstrapNode>
      Then response should be success
      And response should have messageHash property equal to <messageHash>

    Examples:
    | secretInviteName | passphrase                       | inviteName                | messageBody                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | dossierSalt                                                                                                                                 | messageHash                                  | bodyHash                                     | dossierHash                                  | bootstrapNode                                  | bootstrapAddr                                                              | offeringAddr                                                               | serviceAnnouncementMessage                   | serviceOfferingID | sender                                                              | messageType  |
    | Invite 1         | 72x35FDOXugkxivh7qYlqPU91jVgy607 | OnhsB48KkRAguMJd5RklLQ==  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | QgO46Himh8a5fLBmZ1ypIPEMs3fyxblPItByiSJtoZr4VfJdWQxwudTF1fkVI4AkiX8MoKVRffDK+HyA3QPwoRNIZjKf7SjSlNRJ6NOXYy/3gieNLSXGTrs0gIcHle/AAd/n0XkExJxkyI5xyu1/T5XjZcjAaWo73gzzfDYEdfyK9dZyXgpkcML0JloNY5V53DdWi2yolt+wl8COidDP6GwuMHwKa8TwmjPQOveqISXuZhi6gSpW/e3OFk5tcOUo2Lshx+Dj1FSybpyqR7Ocx4Ohfcej7tjhKkgpmuziZX8u7Np/b4aUnzDRZ/h7s1JDnq4nhfVxJARY1v9H0syTVQkZl2aOXRk3bhtqnnqN/LQCA5fGVF47ItZ8ntrAroJL18Ulz+A5WJYyyvKDsHtqfqpAcZf15VTg95h+/8mCwhvO7uw/rdwsngXZdzUfZbYs1WQnoYH/UolcLAfSQ/4DyDOy9xExe3nF70hlFz8i33dzHSjJj9CQzmrCfKQZS0qwNySfHmP2M6srg5theCEFEkO0KF+gtM+JXccB4gCZbZarRXcJ6DtYrz2I8SAcZ2J2QdQYzU9Bj9HNKdUA4CT0zxvm6KuOGfEnpdZ9M3U05SR9YHyUGLMR2chSnivpreMMnT/ndlJpt4/HVu43BbRb2HQaj4x8rFKagtdve0+wNPPAugl35sBxxwzJjEvAl0EK6e7eH+jhHSDAH6xGneOBmY2cJlNpwNKa+Rk4RaRVzyp52tuzZe/Qh9eapTx/SiQaSIdUAjc2sWzYtIPzu9FwO1cWT/vTlnNA8tYtBClFD7w= | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | Wdp+7M5N7A9bvFt4crRwBLk8UtJL3QXDL1dtUZgkhTY= | 7KVD1TLkGsCVap3Lcm2i3kH8y06xkz2A6LlVwhURXFk= | Num4y3dDxO2dpBvnbyo0JVk/WeXvzm3pSDvLL2F0h9w= | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | ibnGrLfuSbgcpWcxtraDUx3TEuXPWhG3DGHFkiUc52B1huCRYDREpfHoaJpVcjT8gDW | REGISTRATION |
    # | InvitE 2         | 4fKuFNOQdisWzhdup3dWRiGIV74kAdag | fkx5vRvAYbM/JBI8KpzXWw==  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | QgO46Himh8a5fLBmZ1ypIDakRUSvEcFXLyG2NFEDlFQI61hW2EQucs3TeleiwKQY6p+ANdHFZ6doUmvWiXV/kRidryUT4lBIrteOiD5w3FoB3+fReQTEnGTIjnHK7X9PleNlyMBpajveDPN8NgR1/Ir11nJeCmRwwvQmWg1jlXncN1aLbKiW37CXwI6J0M/obC4wfAprxPCaM9A696ohJe5mGLqBKlb97c4WTm1w5SjYuyHH4OPUVLJunKpHs5zHg6F9x6Pu2OEqSCma7OJlfy7s2n9vhpSfMNFn+HuzUkOerieF9XEkBFjW/0fSzJNVCRmXZo5dGTduG2qeeo38tAIDl8ZUXjsi1nye2sCugkvXxSXP4DlYljLK8oOwe2p+qkBxl/XlVOD3mH7/yYLCG1nMgY0N7a7S1EHGrCJrrxyfavuU9IR79j8AK3mm6ruBM7L3ETF7ecXvSGUXPyLfd3MdKMmP0JDOasJ8pBlLSrA3JJ8eY/YzqyuDm2F4IQUSQ7QoX6C0z4ldxwHiAJltlqtFdwnoO1ivPYjxIBxnYnZB1BjNT0GP0c0p1QDgJPTPG+boq44Z8Sel1n0zdTTlJH1gfJQYsxHZyFKeK+mt4wydP+d2Umm3j8dW7jcFtFvYdBqPjHysUpqC1297T7A088C6CXfmwHHHDMmMS8CXQQrp7t4f6OEdIMAfrEad44GZjZwmU2nA0pr5GThFpFXPKnna27Nl79CH15qlPH9KJBpIh1QCNzaxbNi0g/O70XA7VxZP+9OWc0Dy1i0EKUUPvA== | d3:11:19:a2:86:14:91:74:c7:d1:2c:10:04:59:a0:db:e5:75:e5:2c:1c:7e:9e:df:07:7c:90:8e:a0:aa:01:0b:ae:7f:b7:13:32:d3:d2:dc | zUvhDLqc08w9+vF4rmW56gxHApAI6dyzBpR49Q0NO6w= | ZyizIyWExijKo774EGVyIQVfEhggnTc+JaaXSHcZs0w= | lqVE9Uep/Izpyrnpf6TtKMMVzr69TeT1zbmPpVYiIrU= | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | ibnGrLfuSbgcpWcxtraDUx3TEuXPWhG3DGHFkiUc52B1huCRYDREpfHoaJpVcjT8gDW | REGISTRATION |
    # | InViTe 3         | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | gq2UnfPHYJwOZYkanb1HVA==  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | QgO46Himh8a5fLBmZ1ypIJLj+cMXKyyxXYb2n50dlNCvUPj2wJMjycLK/dGG3tFgYnqpa9zDgBySkMCKjiksoxHvBbDEau2usXXdcaPKGGUB3+fReQTEnGTIjnHK7X9PleNlyMBpajveDPN8NgR1/Ir11nJeCmRwwvQmWg1jlXncN1aLbKiW37CXwI6J0M/obC4wfAprxPCaM9A696ohJe5mGLqBKlb97c4WTm1w5SjYuyHH4OPUVLJunKpHs5zHg6F9x6Pu2OEqSCma7OJlfy7s2n9vhpSfMNFn+HuzUkOerieF9XEkBFjW/0fSzJNVCRmXZo5dGTduG2qeeo38tAIDl8ZUXjsi1nye2sCugkvXxSXP4DlYljLK8oOwe2p+qkBxl/XlVOD3mH7/yYLCG1xeDm0hmb210ttiNUqqo3BQ30DfCBb9aJjJo6sd4f2ZM7L3ETF7ecXvSGUXPyLfd3MdKMmP0JDOasJ8pBlLSrA3JJ8eY/YzqyuDm2F4IQUSQ7QoX6C0z4ldxwHiAJltlqtFdwnoO1ivPYjxIBxnYnZB1BjNT0GP0c0p1QDgJPTPG+boq44Z8Sel1n0zdTTlJH1gfJQYsxHZyFKeK+mt4wydP+d2Umm3j8dW7jcFtFvYdBqPjHysUpqC1297T7A088C6CXfmwHHHDMmMS8CXQQrp7t4f6OEdIMAfrEad44GZjZwmU2nA0pr5GThFpFXPKnna27Nl79CH15qlPH9KJBpIh1QCNzaxbNi0g/O70XA7VxZP+9OWc0Dy1i0EKUUPvA== | 80:9a:a9:b7:c4:d7:0c:4a:59:45:4e:b3:d5:7e:cc:b4:58:83:cf:e4:f5:5c:1e:68:2a:d1:0e:0d:45:c6:b4:cc:71:5d:b6:0d:62:45:25:26 | UWKHIY4TbQfg8Ftkue2C8f7/zIOPx4CpXKI4dQiwu6Y= | q5RLDwUnwyUTmFr7ekU9JYNi6pOILUnVV+zEhI1MqiM= | pXzoj0FiaWFZjwTcJtf9+ekgZNer2gJGOWUgKt1U8O0= | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | ibnGrLfuSbgcpWcxtraDUx3TEuXPWhG3DGHFkiUc52B1huCRYDREpfHoaJpVcjT8gDW | REGISTRATION |
