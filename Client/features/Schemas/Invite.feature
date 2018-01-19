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
      When I compute HMAC-SHA256 hash of message body with given 40bytes salt
      And encode resulting message body hmac-hash with Base64  
      Then resulting dossierHash should be <dossierHash>

      # Generate message signature
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
      And encode resulted signature with Base64 into messageSig

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
        $messageSig: Sign!
        $message: AESEncryptedBlob!
        $dossierHash: HMACSHA256!
      ){
        sendMessage(
          envelope: {
            sender: $sender
            messageType: $messageType
            messageHash: $messageHash
            bodyHash: $bodyHash
            messageSig: $messageSig
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
    | secretInviteName | passphrase                       | inviteName                | messageBody                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | dossierSalt                                                                                                             | messageHash                                  | bodyHash                                     | dossierHash                                  | bootstrapNode                                  | bootstrapAddr                                                              | offeringAddr                                                               | serviceAnnouncementMessage                   | serviceOfferingID | sender                                                              | messageType  |
    | Invite 1         | 72x35FDOXugkxivh7qYlqPU91jVgy607 | OnhsB48KkRAguMJd5RklLQ==  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | QgO46Himh8a5fLBmZ1ypINLAI4Fb8V/e9r0ZhqQ6A8cOlilkYfh5yMr9eRgKNXBG4HDwSX4hw7kgIqXdEXPlxYXc0yvbW+v6kFTPMeT4J+8B3+fReQTEnGTIjnHK7X9PleNlyMBpajveDPN8NgR1/Ir11nJeCmRwwvQmWg1jlXncN1aLbKiW37CXwI6J0M/obC4wfAprxPCaM9A696ohJe5mGLqBKlb97c4WTm1w5SjYuyHH4OPUVLJunKpHs5zHg6F9x6Pu2OEqSCma7OJlfy7s2n9vhpSfMNFn+HuzUkOerieF9XEkBFjW/0fSzJNVCRmXZo5dGTduG2qeeo38tAIDl8ZUXjsi1nye2sCugkvXxSXP4DlYljLK8oOwe2p+qkBxl/XlVOD3mH7/yYLCG87u7D+t3CyeBdl3NR9ltizVZCehgf9SiVwsB9JD/gPIM7L3ETF7ecXvSGUXPyLfd3MdKMmP0JDOasJ8pBlLSrA3JJ8eY/YzqyuDm2F4IQUSQ7QoX6C0z4ldxwHiAJltlqtFdwnoO1ivPYjxIBxnYnZB1BjNT0GP0c0p1QDgJPTPG+boq44Z8Sel1n0zdTTlJH1gfJQYsxHZyFKeK+mt4wydP+d2Umm3j8dW7jcFtFvYdBqPjHysUpqC1297T7A088C6CXfmwHHHDMmMS8CXQQrp7t4f6OEdIMAfrEad44GZjZwmU2nA0pr5GThFpFXPKnna27Nl79CH15qlPH9KJBpIh1QCNzaxbNi0g/O70XA7VxZP+9OWc0Dy1i0EKUUPvA== | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | L7/ByXV9C4JsHD7VPsoW1csl+Vb0AjMti0/4T0mrTnY= | 7KVD1TLkGsCVap3Lcm2i3kH8y06xkz2A6LlVwhURXFk= | Num4y3dDxO2dpBvnbyo0JVk/WeXvzm3pSDvLL2F0h9w= | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | iZn2hyWChp6hkHEobZNdE9vmruR3MNVQZVFoBMc6PHEvKmaQM1jKoEC1uDF5Qf7deXN | REGISTRATION |
    | InvitE 2         | 4fKuFNOQdisWzhdup3dWRiGIV74kAdag | fkx5vRvAYbM/JBI8KpzXWw==  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | QgO46Himh8a5fLBmZ1ypIDakRUSvEcFXLyG2NFEDlFQI61hW2EQucs3TeleiwKQY6p+ANdHFZ6doUmvWiXV/kRidryUT4lBIrteOiD5w3FoB3+fReQTEnGTIjnHK7X9PleNlyMBpajveDPN8NgR1/Ir11nJeCmRwwvQmWg1jlXncN1aLbKiW37CXwI6J0M/obC4wfAprxPCaM9A696ohJe5mGLqBKlb97c4WTm1w5SjYuyHH4OPUVLJunKpHs5zHg6F9x6Pu2OEqSCma7OJlfy7s2n9vhpSfMNFn+HuzUkOerieF9XEkBFjW/0fSzJNVCRmXZo5dGTduG2qeeo38tAIDl8ZUXjsi1nye2sCugkvXxSXP4DlYljLK8oOwe2p+qkBxl/XlVOD3mH7/yYLCG1nMgY0N7a7S1EHGrCJrrxyfavuU9IR79j8AK3mm6ruBM7L3ETF7ecXvSGUXPyLfd3MdKMmP0JDOasJ8pBlLSrA3JJ8eY/YzqyuDm2F4IQUSQ7QoX6C0z4ldxwHiAJltlqtFdwnoO1ivPYjxIBxnYnZB1BjNT0GP0c0p1QDgJPTPG+boq44Z8Sel1n0zdTTlJH1gfJQYsxHZyFKeK+mt4wydP+d2Umm3j8dW7jcFtFvYdBqPjHysUpqC1297T7A088C6CXfmwHHHDMmMS8CXQQrp7t4f6OEdIMAfrEad44GZjZwmU2nA0pr5GThFpFXPKnna27Nl79CH15qlPH9KJBpIh1QCNzaxbNi0g/O70XA7VxZP+9OWc0Dy1i0EKUUPvA== | d3:11:19:a2:86:14:91:74:c7:d1:2c:10:04:59:a0:db:e5:75:e5:2c:1c:7e:9e:df:07:7c:90:8e:a0:aa:01:0b:ae:7f:b7:13:32:d3:d2:dc | zUvhDLqc08w9+vF4rmW56gxHApAI6dyzBpR49Q0NO6w= | ZyizIyWExijKo774EGVyIQVfEhggnTc+JaaXSHcZs0w= | lqVE9Uep/Izpyrnpf6TtKMMVzr69TeT1zbmPpVYiIrU= | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | iZn2hyWChp6hkHEobZNdE9vmruR3MNVQZVFoBMc6PHEvKmaQM1jKoEC1uDF5Qf7deXN | REGISTRATION |
    | InViTe 3         | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | gq2UnfPHYJwOZYkanb1HVA==  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | QgO46Himh8a5fLBmZ1ypIJLj+cMXKyyxXYb2n50dlNCvUPj2wJMjycLK/dGG3tFgYnqpa9zDgBySkMCKjiksoxHvBbDEau2usXXdcaPKGGUB3+fReQTEnGTIjnHK7X9PleNlyMBpajveDPN8NgR1/Ir11nJeCmRwwvQmWg1jlXncN1aLbKiW37CXwI6J0M/obC4wfAprxPCaM9A696ohJe5mGLqBKlb97c4WTm1w5SjYuyHH4OPUVLJunKpHs5zHg6F9x6Pu2OEqSCma7OJlfy7s2n9vhpSfMNFn+HuzUkOerieF9XEkBFjW/0fSzJNVCRmXZo5dGTduG2qeeo38tAIDl8ZUXjsi1nye2sCugkvXxSXP4DlYljLK8oOwe2p+qkBxl/XlVOD3mH7/yYLCG1xeDm0hmb210ttiNUqqo3BQ30DfCBb9aJjJo6sd4f2ZM7L3ETF7ecXvSGUXPyLfd3MdKMmP0JDOasJ8pBlLSrA3JJ8eY/YzqyuDm2F4IQUSQ7QoX6C0z4ldxwHiAJltlqtFdwnoO1ivPYjxIBxnYnZB1BjNT0GP0c0p1QDgJPTPG+boq44Z8Sel1n0zdTTlJH1gfJQYsxHZyFKeK+mt4wydP+d2Umm3j8dW7jcFtFvYdBqPjHysUpqC1297T7A088C6CXfmwHHHDMmMS8CXQQrp7t4f6OEdIMAfrEad44GZjZwmU2nA0pr5GThFpFXPKnna27Nl79CH15qlPH9KJBpIh1QCNzaxbNi0g/O70XA7VxZP+9OWc0Dy1i0EKUUPvA== | 80:9a:a9:b7:c4:d7:0c:4a:59:45:4e:b3:d5:7e:cc:b4:58:83:cf:e4:f5:5c:1e:68:2a:d1:0e:0d:45:c6:b4:cc:71:5d:b6:0d:62:45:25:26 | UWKHIY4TbQfg8Ftkue2C8f7/zIOPx4CpXKI4dQiwu6Y= | q5RLDwUnwyUTmFr7ekU9JYNi6pOILUnVV+zEhI1MqiM= | pXzoj0FiaWFZjwTcJtf9+ekgZNer2gJGOWUgKt1U8O0= | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | iZn2hyWChp6hkHEobZNdE9vmruR3MNVQZVFoBMc6PHEvKmaQM1jKoEC1uDF5Qf7deXN | REGISTRATION |
