Feature: Invitation message
  
  Scenario Outline: Generate invite name
    Given secret 32 bytes passphrase <passphrase>
    And secret invite name <inviteName>
    When I encrypt using AES module and given passphrase
    Then the resulting encrypted invite name should be <result>

  Examples:
  | inviteName | passphrase                       | result                   |
  | Invite 1   | 72x35FDOXugkxivh7qYlqPU91jVgy607 | OnhsB48KkRAguMJd5RklLQ== |
  | InvitE 2   | 4fKuFNOQdisWzhdup3dWRiGIV74kAdag | fkx5vRvAYbM/JBI8KpzXWw== |
  | InViTe 3   | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | gq2UnfPHYJwOZYkanb1HVA== |

  Scenario Outline: Generate invite message body
    Given a bootstrap node url <bootstrapNode>
    And bootstrap addrress <bootstrapAddr>
    And offering registred Persona address <offeringAddr> (Rigth now only teleferic Persona is registred)
    And service announcement message SHA256 hash identifier encoded on Base64 <serviceAnnouncementMessage> (not defined yet)
    And service identifier <serviceOfferingID>
    And encrypted invite name <inviteName>
    When I compose invite message body sorting attributes alphabetically
    And format message body with Message Pack
    And encode resulting pack with Base64 
    Then resulting message body should be equal to <result>
  
  Examples:
  | bootstrapNode                                  | bootstrapAddr                                                              | offeringAddr                                                               | serviceAnnouncementMessage                   | serviceOfferingID | inviteName               | result |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | OnhsB48KkRAguMJd5RklLQ== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | fkx5vRvAYbM/JBI8KpzXWw== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | gq2UnfPHYJwOZYkanb1HVA== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |

  @wip
  Scenario Outline: Parse invite message body
    Given message body <result>
    When I decode message boy with Base64
    And parse resulting content with Message Pack
    Then bootstrapNode attribute should be <bootstrapNode>
    And bootstrapAddr attribute should be <bootstrapAddr>
    And offeringAddr attribute should be <offeringAddr>
    And serviceAnnouncementMessage attribute should be <serviceAnnouncementMessage>
    And serviceOfferingID attribute should be <serviceOfferingID>
    And inviteName attribute should be <inviteName>
  
  Examples:
  | bootstrapNode                                  | bootstrapAddr                                                              | offeringAddr                                                               | serviceAnnouncementMessage                   | serviceOfferingID | inviteName               | result |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | OnhsB48KkRAguMJd5RklLQ== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | fkx5vRvAYbM/JBI8KpzXWw== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | gq2UnfPHYJwOZYkanb1HVA== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |