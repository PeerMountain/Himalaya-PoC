Feature: Invitation message
  
  Scenario Outline: Generate invite name
    Given secret 32 bytes passphrase <passphrase>
    And secret invite name <secretInviteName>
    When I encrypt using AES module and given passphrase
    Then the resulting encrypted <inviteName> should be <result>

  Examples:
  | secretInviteName | passphrase                       | result                   |
  | Invite 1         | 72x35FDOXugkxivh7qYlqPU91jVgy607 | OnhsB48KkRAguMJd5RklLQ== |
  | InvitE 2         | 4fKuFNOQdisWzhdup3dWRiGIV74kAdag | fkx5vRvAYbM/JBI8KpzXWw== |
  | InViTe 3         | T7TDUepNdU8wCL5ruLSy3gCcDomsbv3r | gq2UnfPHYJwOZYkanb1HVA== |

  Scenario Outline: Generate invite message body
    Given a bootstrap node url <bootstrapNode>
    And bootstrap addrress <bootstrapAddr>
    And offering registred Persona address <offeringAddr> (Rigth now only teleferic Persona is registred)
    And service announcement message SHA256 hash identifier encoded on Base64 <serviceAnnouncementMessage> (not defined yet)
    And service identifier <serviceOfferingID>
    And encrypted invite name <inviteName>
    When I compose invite message body sorting attributes alphabetically
    And format message body with Message Pack
    And encode resulting message body pack with Base64 
    Then resulting <messageBody> should be equal to <result>
  
  Examples:
  | bootstrapNode                                  | bootstrapAddr                                                              | offeringAddr                                                               | serviceAnnouncementMessage                   | serviceOfferingID | inviteName               | result |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | OnhsB48KkRAguMJd5RklLQ== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | fkx5vRvAYbM/JBI8KpzXWw== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | gq2UnfPHYJwOZYkanb1HVA== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |

  Scenario Outline: Parse invite message body
    Given message body content <messageBody>
    When I decode message body with Base64
    And parse resulting message body with Message Pack
    Then bootstrapNode attribute should be <bootstrapNode>
    And bootstrapAddr attribute should be <bootstrapAddr>
    And offeringAddr attribute should be <offeringAddr>
    And serviceAnnouncementMessage attribute should be <serviceAnnouncementMessage>
    And serviceOfferingID attribute should be <serviceOfferingID>
    And inviteName attribute should be <inviteName>
  
  Examples:
  | bootstrapNode                                  | bootstrapAddr                                                              | offeringAddr                                                               | serviceAnnouncementMessage                   | serviceOfferingID | inviteName               | messageBody                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | OnhsB48KkRAguMJd5RklLQ== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | fkx5vRvAYbM/JBI8KpzXWw== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  | https://teleferic-dev.dxmarkets.com/teleferic/ | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | 8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL | L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY= | 1                 | gq2UnfPHYJwOZYkanb1HVA== | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx |
  
  Scenario Outline: Compose invitation message content
    Given 40 bytes random salt <dossierSalt>
    And message body type <bodyType> equal to 0 (Invitation)
    And message body content <messageBody>
    When I compose invite message content sorting attributes alphabetically
    And format message content with Message Pack
    And encrypt resulting message content pack using AES with public passphrase "Peer Mountain"
    And encode resulting encrypted message content pack with Base64 
    Then resulting <message> should be <result>

  Examples:
  | dossierSalt                                                                                                             | messageBody                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | UWdPNDZIaW1oOGE1ZkxCbVoxeXBJTkxBSTRGYjhWL2U5cjBaaHFRNkE4Y09saWxrWWZoNXlNcjllUmdLTlhCRzRIRHdTWDRodzdrZ0lxWGRFWFBseFlYYzB5dmJXK3Y2a0ZUUE1lVDRKKzhCMytmUmVRVEVuR1RJam5ISzdYOVBsZU5seU1CcGFqdmVEUE44TmdSMS9JcjExbkplQ21Sd3d2UW1XZzFqbFhuY04xYUxiS2lXMzdDWHdJNkowTS9vYkM0d2ZBcHJ4UENhTTlBNjk2b2hKZTVtR0xxQktsYjk3YzRXVG0xdzVTall1eUhINE9QVVZMSnVuS3BIczV6SGc2Rjl4NlB1Mk9FcVNDbWE3T0psZnk3czJuOXZocFNmTU5GbitIdXpVa09lcmllRjlYRWtCRmpXLzBmU3pKTlZDUm1YWm81ZEdUZHVHMnFlZW8zOHRBSURsOFpVWGpzaTFueWUyc0N1Z2t2WHhTWFA0RGxZbGpMSzhvT3dlMnArcWtCeGwvWGxWT0QzbUg3L3lZTENHODd1N0QrdDNDeWVCZGwzTlI5bHRpelZaQ2VoZ2Y5U2lWd3NCOUpEL2dQSU03TDNFVEY3ZWNYdlNHVVhQeUxmZDNNZEtNbVAwSkRPYXNKOHBCbExTckEzSko4ZVkvWXpxeXVEbTJGNElRVVNRN1FvWDZDMHo0bGR4d0hpQUpsdGxxdEZkd25vTzFpdlBZanhJQnhuWW5aQjFCak5UMEdQMGMwcDFRRGdKUFRQRytib3E0NFo4U2VsMW4wemRUVGxKSDFnZkpRWXN4SFp5RktlSyttdDR3eWRQK2QyVW1tM2o4ZFc3amNGdEZ2WWRCcVBqSHlzVXBxQzEyOTdUN0EwODhDNkNYZm13SEhIRE1tTVM4Q1hRUXJwN3Q0ZjZPRWRJTUFmckVhZDQ0R1pqWndtVTJuQTBwcjVHVGhGcEZYUEtubmEyN05sNzlDSDE1cWxQSDlLSkJwSWgxUUNOemF4Yk5pMGcvTzcwWEE3VnhaUCs5T1djMER5MWkwRUtVVVB2QT09 |
  | d3:11:19:a2:86:14:91:74:c7:d1:2c:10:04:59:a0:db:e5:75:e5:2c:1c:7e:9e:df:07:7c:90:8e:a0:aa:01:0b:ae:7f:b7:13:32:d3:d2:dc | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | UWdPNDZIaW1oOGE1ZkxCbVoxeXBJRGFrUlVTdkVjRlhMeUcyTkZFRGxGUUk2MWhXMkVRdWNzM1RlbGVpd0tRWTZwK0FOZEhGWjZkb1VtdldpWFYva1JpZHJ5VVQ0bEJJcnRlT2lENXczRm9CMytmUmVRVEVuR1RJam5ISzdYOVBsZU5seU1CcGFqdmVEUE44TmdSMS9JcjExbkplQ21Sd3d2UW1XZzFqbFhuY04xYUxiS2lXMzdDWHdJNkowTS9vYkM0d2ZBcHJ4UENhTTlBNjk2b2hKZTVtR0xxQktsYjk3YzRXVG0xdzVTall1eUhINE9QVVZMSnVuS3BIczV6SGc2Rjl4NlB1Mk9FcVNDbWE3T0psZnk3czJuOXZocFNmTU5GbitIdXpVa09lcmllRjlYRWtCRmpXLzBmU3pKTlZDUm1YWm81ZEdUZHVHMnFlZW8zOHRBSURsOFpVWGpzaTFueWUyc0N1Z2t2WHhTWFA0RGxZbGpMSzhvT3dlMnArcWtCeGwvWGxWT0QzbUg3L3lZTENHMW5NZ1kwTjdhN1MxRUhHckNKcnJ4eWZhdnVVOUlSNzlqOEFLM21tNnJ1Qk03TDNFVEY3ZWNYdlNHVVhQeUxmZDNNZEtNbVAwSkRPYXNKOHBCbExTckEzSko4ZVkvWXpxeXVEbTJGNElRVVNRN1FvWDZDMHo0bGR4d0hpQUpsdGxxdEZkd25vTzFpdlBZanhJQnhuWW5aQjFCak5UMEdQMGMwcDFRRGdKUFRQRytib3E0NFo4U2VsMW4wemRUVGxKSDFnZkpRWXN4SFp5RktlSyttdDR3eWRQK2QyVW1tM2o4ZFc3amNGdEZ2WWRCcVBqSHlzVXBxQzEyOTdUN0EwODhDNkNYZm13SEhIRE1tTVM4Q1hRUXJwN3Q0ZjZPRWRJTUFmckVhZDQ0R1pqWndtVTJuQTBwcjVHVGhGcEZYUEtubmEyN05sNzlDSDE1cWxQSDlLSkJwSWgxUUNOemF4Yk5pMGcvTzcwWEE3VnhaUCs5T1djMER5MWkwRUtVVVB2QT09 |
  | 80:9a:a9:b7:c4:d7:0c:4a:59:45:4e:b3:d5:7e:cc:b4:58:83:cf:e4:f5:5c:1e:68:2a:d1:0e:0d:45:c6:b4:cc:71:5d:b6:0d:62:45:25:26 | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | UWdPNDZIaW1oOGE1ZkxCbVoxeXBJSkxqK2NNWEt5eXhYWWIybjUwZGxOQ3ZVUGoyd0pNanljTEsvZEdHM3RGZ1lucXBhOXpEZ0J5U2tNQ0tqaWtzb3hIdkJiREVhdTJ1c1hYZGNhUEtHR1VCMytmUmVRVEVuR1RJam5ISzdYOVBsZU5seU1CcGFqdmVEUE44TmdSMS9JcjExbkplQ21Sd3d2UW1XZzFqbFhuY04xYUxiS2lXMzdDWHdJNkowTS9vYkM0d2ZBcHJ4UENhTTlBNjk2b2hKZTVtR0xxQktsYjk3YzRXVG0xdzVTall1eUhINE9QVVZMSnVuS3BIczV6SGc2Rjl4NlB1Mk9FcVNDbWE3T0psZnk3czJuOXZocFNmTU5GbitIdXpVa09lcmllRjlYRWtCRmpXLzBmU3pKTlZDUm1YWm81ZEdUZHVHMnFlZW8zOHRBSURsOFpVWGpzaTFueWUyc0N1Z2t2WHhTWFA0RGxZbGpMSzhvT3dlMnArcWtCeGwvWGxWT0QzbUg3L3lZTENHMXhlRG0waG1iMjEwdHRpTlVxcW8zQlEzMERmQ0JiOWFKakpvNnNkNGYyWk03TDNFVEY3ZWNYdlNHVVhQeUxmZDNNZEtNbVAwSkRPYXNKOHBCbExTckEzSko4ZVkvWXpxeXVEbTJGNElRVVNRN1FvWDZDMHo0bGR4d0hpQUpsdGxxdEZkd25vTzFpdlBZanhJQnhuWW5aQjFCak5UMEdQMGMwcDFRRGdKUFRQRytib3E0NFo4U2VsMW4wemRUVGxKSDFnZkpRWXN4SFp5RktlSyttdDR3eWRQK2QyVW1tM2o4ZFc3amNGdEZ2WWRCcVBqSHlzVXBxQzEyOTdUN0EwODhDNkNYZm13SEhIRE1tTVM4Q1hRUXJwN3Q0ZjZPRWRJTUFmckVhZDQ0R1pqWndtVTJuQTBwcjVHVGhGcEZYUEtubmEyN05sNzlDSDE1cWxQSDlLSkJwSWgxUUNOemF4Yk5pMGcvTzcwWEE3VnhaUCs5T1djMER5MWkwRUtVVVB2QT09 |

  @wip
  Scenario Outline: Calculate message hash
    Given message <message>
    When I compute SHA256 hash of message
    And encode resulting message hash with Base64  
    Then resulting <messageHash> should be <result>
  
  Scenario Outline: Calculate message body hash
    Given message body content <messageBody>
    When I compute SHA256 hash of message body
    And encode resulting message body hash with Base64  
    Then resulting <bodyHash> should be <result>

  Examples:
  | messageBody                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | result                                       |
  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | 7KVD1TLkGsCVap3Lcm2i3kH8y06xkz2A6LlVwhURXFk= |
  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | ZyizIyWExijKo774EGVyIQVfEhggnTc+JaaXSHcZs0w= |
  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | q5RLDwUnwyUTmFr7ekU9JYNi6pOILUnVV+zEhI1MqiM= |

  Scenario Outline: Calculate dossier hash
    Given message body content <messageBody>
    Given 40 bytes random salt <dossierSalt>
    When I compute HMAC-SHA256 hash of message body with given 40bytes salt
    And encode resulting message body hmac-hash with Base64  
    Then resulting <dossierHash> should be <result>

  Examples:
  | messageBody                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | dossierSalt                                                                                                             | result                                       |
  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhPbmhzQjQ4S2tSQWd1TUpkNVJrbExRPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | 74:26:13:2f:4d:f3:f8:3e:82:ba:f3:fe:6a:dd:46:c2:00:4c:99:e8:88:ed:0f:a9:58:85:a2:11:9e:c8:b7:46:e4:f4:f0:c3:70:30:0e:17 | Num4y3dDxO2dpBvnbyo0JVk/WeXvzm3pSDvLL2F0h9w= |
  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhma3g1dlJ2QVliTS9KQkk4S3B6WFd3PT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | d3:11:19:a2:86:14:91:74:c7:d1:2c:10:04:59:a0:db:e5:75:e5:2c:1c:7e:9e:df:07:7c:90:8e:a0:aa:01:0b:ae:7f:b7:13:32:d3:d2:dc | lqVE9Uep/Izpyrnpf6TtKMMVzr69TeT1zbmPpVYiIrU= |
  | hq1ib290c3RyYXBBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5ckytYm9vdHN0cmFwTm9kZdoALmh0dHBzOi8vdGVsZWZlcmljLWRldi5keG1hcmtldHMuY29tL3RlbGVmZXJpYy+qaW52aXRlTmFtZbhncTJVbmZQSFlKd09aWWthbmIxSFZBPT2sb2ZmZXJpbmdBZGRy2gBKOE1TZDkxeHI2alNWNXBTMjlSa1Y3ZExlRTNoRGdMSEpHcnN5WHBkU2Y0aWl0ajZjNzV0VlNORVN5d0J6WXpGRWV5dTVEMXp5cky6c2VydmljZUFubm91bmNlbWVudE1lc3NhZ2XaACxMK1ZpUCtVRm5oYzZPYldmaHVncU5aZkUrU1prcW9TNDZJNFFidytOYk9ZPbFzZXJ2aWNlT2ZmZXJpbmdJRKEx | 80:9a:a9:b7:c4:d7:0c:4a:59:45:4e:b3:d5:7e:cc:b4:58:83:cf:e4:f5:5c:1e:68:2a:d1:0e:0d:45:c6:b4:cc:71:5d:b6:0d:62:45:25:26 | pXzoj0FiaWFZjwTcJtf9+ekgZNer2gJGOWUgKt1U8O0= |
  
  Scenario Outline: Generate Message signature
    Given following private key <privkey>
    """
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
    """
    And message hash <messageHash>
    And teleferic signed timestamp <telefericSignedTimestamp>
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
    And format signable object with Message Pack
    And encode resulted signature with Base64 
    Then resulting <messageSig> should be <result>
  
  Examples:
  | messageHash                                  | telefericSignedTimestamp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | 7KVD1TLkGsCVap3Lcm2i3kH8y06xkz2A6LlVwhURXFk= | gqlzaWduYXR1cmXaAqx1WXdJa05IVWwwOVFocWZFWHlpMXQ0QkRDcDNLUzlWeXF0YVpIQjcrZm5KTGJMRXh3cjhFM1VjTWFzRFV1ZGJBK1JVcGQ4aEhGQkhBUC9aMEw3cVMzcWxzY3FzSlVvWUF3VXlUK0hIUklaeEhjbjBiRXFhK1dPYVVva2hNZEdlYWU1WUxnQnhTcWNiT0EwSGJjQ3ZVdHVBYm56QzJYRjg4S3dMdmNRRUx6UG16Q0tKUm0wME9BUGdXZmpPYjA5M25Sa0V2aXFZYWFlR2pjQmYzY1E5MUdpMVpjQytJdkJEamQ5MDcrUlBUOGt0enF4N1JoalpWVFFrQzZGU29wTk5NZ3NFeFN2T0FIWlYwR0Z0aVp1b0JrY2EraWo0MmZ0bkZXZ25aamMrd0NuK1BSanRuVVQrZkVnc2QvZExkWDNUQk9aeHBENTlWRkdSSjAyZU82YmRtaFFrK01wN0pZK2swdmtSbzRuVTVTMEM1dlZYRG85MllyNCsxWGNPZmFVbGhhR2pQZzBCdmRZSVVoRVBybmpiLzJ2MjFPWENQckQ1TGtsVWd4RmdINFJ5a1AzbktVMHBVWXUyMEtJOTRoY2JaSGM2ODhqNzBOOWZRdkpwSXJpWjJDWjdPR0VJaSs4M21iaWxSclJoR3I0MktnU2ZSOEV3c1VRa05RREVsS1dSVGdReFdxYjl1Z1dSekNLVjhlNUpWWHIxNW1lS0ZtZG8vcEdiakxCM0tKRXIvcDNrTXpWMlFKUmJhbXVpNytwa2lFQWk5bEZ2NVRMRDF0QUVZZVlqeVBZcEhPK2w0Q0p3em1lVWxpb2k1RkhaUld5aHJDTXpBNldDcnpFZWdiNnQwZjVVYjBqTW1FTG50WVNka0hlY0J6UWpLQ081aWcxL1huZjlBODA5NlBrYz2pdGltZXN0YW1wsjE1MTEzNTYxOTEuMTY2MjE3OA== | gqlzaWduYXR1cmWR2gKsakZxc0RBcGZua1lBSEhucmNsb09PRWRkZlZseFAwNno0RHV0bDJNRFF0T2h4TnBzamhnU0hpZTZsdnErS0hONThsYkVjM0ZwcGMyTG92UVhPbldZOXBsTmxPcDRDcU5QZFpDSlkxSXVSMy9MTFJIZWFYSTIzdnVZcDlvaFUrY0dqVVlSdzI5NGYzNjhJVC9MZDg1L3VuR1pVUWZRY1kwdnFSRFpGQUhVUkd2MXdyMW8zb0t4aGZNVVFjQ0JLNDBxdWsrcnZnZHJGYUJTVUM2RGFSaXNJaXBGcnc3VnNad210QzcvaFhGSVIvc1pUMjhxblJvNHhSNVF5eXNndi8wTURSTWFLRjN0MjAwSkNkZm1XWGoxM2dvZE5LTDZ3TWh1QUQyanJZYlUyQjFsZXQ0M1VZODdINmU1UmdHbXVHR09BeDg2akZLMCtZOHArRk1xQ3VLbE1aSkVzSnM2ZXo0N3NDVW9hTGlScWhrKzBtN3EwYXFSVkl1czBDcVVoU2kwRW9mUUdEMElNcFNubjBSNlZRWVFQVGd0ZjNJMElJMkk3NHFrODJyVGJoWGJuajByc0NJU3ZFRFZwUTBqVitHSk5lR3JXdXc5TjdnbVRvVG5sY2xtRDYyQUwvZVVjS2g2M0J1bTZCbWIzbDg5UElkSDFvMVpudEIwWk44WVg0RWtQdlFNRkJPQUlWeGpBUEgzY1pSMjN4WHorVnpwWHhWRUYxUDlHZXIwZFlHNkdOcUZQMll1NXMxR2l5UUZoZlpoYlhVdWpWN0JxR3BOUHhuYXExOStUM1RtVElWSnorWkhzUWg3a3RKWXFYakY1Tkt5a1h6VE5lYjhOWEFYNU1vcmlLcFRaL1lUQ3JpODEwd0FjajF1QncxTnBjaThaZFJOWVlEVnlvUWJ0cXM9qXRpbWVzdGFtcNoDzGdxbHphV2R1WVhSMWNtWGFBcXgxV1hkSmEwNUlWV3d3T1ZGb2NXWkZXSGxwTVhRMFFrUkRjRE5MVXpsV2VYRjBZVnBJUWpjclptNUtUR0pNUlhoM2NqaEZNMVZqVFdGelJGVjFaR0pCSzFKVmNHUTRhRWhHUWtoQlVDOWFNRXczY1ZNemNXeHpZM0Z6U2xWdldVRjNWWGxVSzBoSVVrbGFlRWhqYmpCaVJYRmhLMWRQWVZWdmEyaE5aRWRsWVdVMVdVeG5RbmhUY1dOaVQwRXdTR0pqUTNaVmRIVkJZbTU2UXpKWVJqZzRTM2RNZG1OUlJVeDZVRzE2UTB0S1VtMHdNRTlCVUdkWFptcFBZakE1TTI1U2EwVjJhWEZaWVdGbFIycGpRbVl6WTFFNU1VZHBNVnBqUXl0SmRrSkVhbVE1TURjclVsQlVPR3QwZW5GNE4xSm9hbHBXVkZGclF6WkdVMjl3VGs1TlozTkZlRk4yVDBGSVdsWXdSMFowYVZwMWIwSnJZMkVyYVdvME1tWjBia1pYWjI1YWFtTXJkME51SzFCU2FuUnVWVlFyWmtWbmMyUXZaRXhrV0ROVVFrOWFlSEJFTlRsV1JrZFNTakF5WlU4MlltUnRhRkZySzAxd04wcFpLMnN3ZG10U2J6UnVWVFZUTUVNMWRsWllSRzg1TWxseU5Dc3hXR05QWm1GVmJHaGhSMnBRWnpCQ2RtUlpTVlZvUlZCeWJtcGlMekoyTWpGUFdFTlFja1ExVEd0c1ZXZDRSbWRJTkZKNWExQXpia3RWTUhCVldYVXlNRXRKT1RSb1kySmFTR00yT0RocU56Qk9PV1pSZGtwd1NYSnBXakpEV2pkUFIwVkphU3M0TTIxaWFXeFNjbEpvUjNJME1rdG5VMlpTT0VWM2MxVlJhMDVSUkVWc1MxZFNWR2RSZUZkeFlqbDFaMWRTZWtOTFZqaGxOVXBXV0hJeE5XMWxTMFp0Wkc4dmNFZGlha3hDTTB0S1JYSXZjRE5yVFhwV01sRktVbUpoYlhWcE55dHdhMmxGUVdrNWJFWjJOVlJNUkRGMFFVVlpaVmxxZVZCWmNFaFBLMncwUTBwM2VtMWxWV3hwYjJrMVJraGFVbGQ1YUhKRFRYcEJObGREY25wRlpXZGlOblF3WmpWVllqQnFUVzFGVEc1MFdWTmthMGhsWTBKNlVXcExRMDgxYVdjeEwxaHVaamxCT0RBNU5sQnJZejJwZEdsdFpYTjBZVzF3c2pFMU1URXpOVFl4T1RFdU1UWTJNakUzT0E9PQ== |
  | ZyizIyWExijKo774EGVyIQVfEhggnTc+JaaXSHcZs0w= | gqlzaWduYXR1cmXaAqxFK2tsMXprM1VPU3Fra1A1am12bXgvQkF4S2wxVm15QWo2Q0xFMkxmZDlDQ2NOWGdvOUxIc1pGRlNHTkNBTWJtMDhXV256SVZBK0xHQy9SMlJ6ck1WNUYvaHVsbE1zcGh0VE5xa0ltUVJGTG1yN0tIMDNwUFNnblpDdk9rdTlRUjlsZXRpdlhDVzduVG1HYklIUHZmaFNLZlFYNWo1bFNna3FVNWNqSGdZTnU5VzliazJtbE1QTTAzS0Y3S1pJbkw3VnJSSklxWmNPcmJCbFpiK1lvL3IxNkUxRWRkd2RyRWE2TTlnRDhzZXVubC8vQitycXk0YlQ1MkVhSnBJN3NGb25RVTgxbWxteXZNbENVSTA3cjJPbzcwVHBGRU9JNFkrTzNWVXNET3dTUlNEeEJjTkMzc1UvRUMwOVY2NDFNS1diZUtjc29VaG85VEFrcDZtVU54S0QyY3RPcCsyR0tuenphOEFwbVl3Qm9hUTM2TlRYYWpjdVlRZlNiWm93NjlSdG9raE9oSVVkSDFoUXRGYjhtVnQ5dFp5clJsL2MvTElmOTdkRHdiZWRiZkFmNE40QUxuSkdvYnpHZkp2WFR6cVJyUGIzWHEyeEtTSkxtQTVpY25lUU5EeVIyc0JlakpZcUNUM2lTaWRoZzdXaTRvV1BpNGtFNTNVdjA3TC9JazloTFdPYmd1NWZtM2ljcU9SWFhXREJtWERUelVHYXRadEgxMCtPTm44V0thQ0doR1Q1Q2ZZWWRLUkd4bHpnTllxblI3TkJVNVpEUXNDemVIWGpmRE9raEw3b2dOTVAva2JXNXF5SXUwYUJuTjMwRGxaUFpnUFVJcnRFOFh2cWRYb3NJdVcza24zOER3dmhsa1owQ1cxdGJsVXZYVUx5R1lBbzh4K2ZMWW5uST2pdGltZXN0YW1wsjE1MTEzNTYyNzEuMTYyOTY0Ng== | gqlzaWduYXR1cmWR2gKsbGM1OU1zL0VQMC9sc2hqYkFFVzczMEgzbWJsTDlWWkh4U0xmSlp3Sk81ajJTMTdmcnE2YXhkN0N5a051MmhuTlJmeTJoWDlHZitSMHAwbll0N0JCbUV0NkxHdjBUYU9LaWZLWHNsaG5iNTliNTM1cEc0ZDg3SUhLU3hhR25rdTRiTmowLzRvVjNQUk12VURDWkcxZXlCOWZUSytmOE92VXI4dE1ZRlJQalF1L2hmMVQvdHNMVWZEdmlIMUdRd3cwN3o4VFRlTE5td3FZajhLdm9uVUw2S1RoOTBkKzNLRHdBSzdxN2RkNHdGZml6UkxGU2pFWUJiQkhUYUJHanJ5RjJLWndtRkQ3TC9jNkxQZDg1UUVHY21zVWs5WGIwVThEcmJISXhscnNFMkRoSGVVMHFVa3hqY2cyci9WR24vRkMyc2Nxb3NKUVRSdElTSVprRTQxV3o2TFBCS2R3VTNOMWRIaW1zaGV0Y3RTcmxKSmx1a0piNGNoVmozek5pTy9yN0VPMWQzMXU5MTNZZ0pmR2lHMUM3bERERUQzd05hSlpLL2lsYzhYcnVPWW85ZFA5YVhubi9aQm53ZEpWV0NmVFJtYkFxMHVHQVhybEJGT0Z2MHdjVTZDSmo5RzJYMUUwNk5FaHQxYUNxTHlzSHF2NXF6aVhrOXl2WmJSNXFXMzBzcHZSQmVWSUJaNE50YThsSDRwdkJZdVdNRUl6d0RoSmV1aSt4d0syaFdzUERacjZnMmYxUGd3RUZOTmlpL2ltVjUyUDlNeEo1bi8rVk9yOWZwK2NLOVBkNkgweXRiQ0gyelUwdnBkaWJUVXdFZkZsRFdGUHcrZ3dNeVNRaDdXazFIQ2hXVWkrUjlpYzF5NThvbmRSN3YxRTNuTVhWT0xGdUNtK2dwcUpQWVU9qXRpbWVzdGFtcNoDzGdxbHphV2R1WVhSMWNtWGFBcXhGSzJ0c01YcHJNMVZQVTNGcmExQTFhbTEyYlhndlFrRjRTMnd4Vm0xNVFXbzJRMHhGTWt4bVpEbERRMk5PV0dkdk9VeEljMXBHUmxOSFRrTkJUV0p0TURoWFYyNTZTVlpCSzB4SFF5OVNNbEo2Y2sxV05VWXZhSFZzYkUxemNHaDBWRTV4YTBsdFVWSkdURzF5TjB0SU1ETndVRk5uYmxwRGRrOXJkVGxSVWpsc1pYUnBkbGhEVnpkdVZHMUhZa2xJVUhabWFGTkxabEZZTldvMWJGTm5hM0ZWTldOcVNHZFpUblU1VnpsaWF6SnRiRTFRVFRBelMwWTNTMXBKYmt3M1ZuSlNTa2x4V21OUGNtSkNiRnBpSzFsdkwzSXhOa1V4UldSa2QyUnlSV0UyVFRsblJEaHpaWFZ1YkM4dlFpdHljWGswWWxRMU1rVmhTbkJKTjNOR2IyNVJWVGd4Yld4dGVYWk5iRU5WU1RBM2NqSlBiemN3VkhCR1JVOUpORmtyVHpOV1ZYTkVUM2RUVWxORWVFSmpUa016YzFVdlJVTXdPVlkyTkRGTlMxZGlaVXRqYzI5VmFHODVWRUZyY0RadFZVNTRTMFF5WTNSUGNDc3lSMHR1ZW5waE9FRndiVmwzUW05aFVUTTJUbFJZWVdwamRWbFJabE5pV205M05qbFNkRzlyYUU5b1NWVmtTREZvVVhSR1lqaHRWblE1ZEZwNWNsSnNMMk12VEVsbU9UZGtSSGRpWldSaVprRm1ORTQwUVV4dVNrZHZZbnBIWmtwMldGUjZjVkp5VUdJeldIRXllRXRUU2t4dFFUVnBZMjVsVVU1RWVWSXljMEpsYWtwWmNVTlVNMmxUYVdSb1p6ZFhhVFJ2VjFCcE5HdEZOVE5WZGpBM1RDOUphemxvVEZkUFltZDFOV1p0TTJsamNVOVNXRmhYUkVKdFdFUlVlbFZIWVhSYWRFZ3hNQ3RQVG00NFYwdGhRMGRvUjFRMVEyWlpXV1JMVWtkNGJIcG5UbGx4YmxJM1RrSlZOVnBFVVhORGVtVklXR3BtUkU5cmFFdzNiMmRPVFZBdmEySlhOWEY1U1hVd1lVSnVUak13Ukd4YVVGcG5VRlZKY25SRk9GaDJjV1JZYjNOSmRWY3phMjR6T0VSM2RtaHNhMW93UTFjeGRHSnNWWFpZVlV4NVIxbEJiemg0SzJaTVdXNXVTVDJwZEdsdFpYTjBZVzF3c2pFMU1URXpOVFl5TnpFdU1UWXlPVFkwTmc9PQ== |
  | q5RLDwUnwyUTmFr7ekU9JYNi6pOILUnVV+zEhI1MqiM= | gqlzaWduYXR1cmXaAqxISlpXNEg2QlZGMzlRWlozUXE0blJnZTI1MkpXUUx3RVhyb25TUmIwSFFoYXRlT0dQY1VHTlRGbmdOL0RMN1pwODA4NzJTL0ZpNFZheHlqTDdiaWkxR1c1dThFYi91RnE4UVZ0SWRsZ1J6ZXVLeU1IdWNCSFkwQmM3UGNsNFB5eDR4a2xIRllLTDVncnVpU2RkemNkdWNRbEVTYys5NHlDRm1XaU5LNG8xalF2ZFREZEVwNjdKekwwNnVmWWxFbWlOQVhhT0dETEZtTStZaXJZUnRhSDlzVVkrdG53aDJqWExMN3VNUTVQS2gyclYzbkxhR3JZdFEvNFJhUnloVEhxNnZ5R2xDVXltSzRIcENTZjRzT0tXY1BXQlp0U1hMc3ZLM0dMbnl1Q0YrWWJnMC9zZ0lGOVU3N1hWTTYvUDgxOTNCWUp0UlZMLzRnNjg1Y0FsbkFRL01HOTFvUVQxVk5jRHpBdm1JNEJLVERqc3BXZkZET1RwelNEdVM0SGN1SjFVdUdCWVBMYm5IeHBDdW9sYjA4bkIzd1crc3pVUkdhbC9HOENON1FPcGxPOE0wWFBMZGhIUTgvM29iZWtRZm1JekwvTXhQZVpwb05wL0lFdEJVVTA4M2NyV1owaXJ3ZHVTdkJhVWxWaTBhTGxrYmpPc2k0bFhRTzlweUh4RlBobm1VTkVwcHM5QVVCUnl6bmtXYkhFQStOMTZRVG5yTkY5ZjBmQVdNcFh6T202bHE4cnJER3h4OFphOUxOU3oyN0NaVEw5L1VOSTdjZStmOFU4NzZtUmhJN0k2RkpOclBGbkhzdG9zNWpVZkxEMVE3M2xXVHl1Yjk3OUM4WmNlNTJpeUFmS3QxbEVOMHllQlBzRFNydXNuTFdDNGhMU3YzRFo2T2s1VW83S3Y5az2pdGltZXN0YW1wsjE1MTEzNTYyODMuMjI3MDcwOA== | gqlzaWduYXR1cmWR2gKsYmoyTE5PWHJhUlVaZEN0RnNiUEdZM1FjMmxPMTQ3R3V0dmVUT0JUNmpyVHFnK2I5NWo0MGxpZWFhTktOYjNXeWlhOXZ1K3JsNDFDWXZ0a1BrbmVHbWI4QVBPYkFqbVFHZm93ZFc2dDY3OXFzK2l1WFRzVTkyNW9TYXFhN3RHL1lqSWVoR2xtSDAyVWhOYm5ud3dmcjJ6cFFtRElPRFZ2YTJJZ2RZcW8xQnhObDVObFBlek9IdGhyTlBPMUJYMUhieEc0Vzd1RmVBZVp3TzA5dkJBbk5RQzBsT0hJQzdZN2hkUnZvaXFlWVpqcGFyM3F5T2xQZWFIY2lLNSt0cUhpeFFIWER5VGNvQzRUYlEvYmJjSDhpcGNaUjZkVnVOQ1czY1QvNGdhWDhYNFhjYmN5eEwxTkV2bTlZcU1kOTJSU01WRWp1RlJPdnNGbnhuU0x1MHB1cUl0cFZsRHRvUGtxK3NUUVRYNWZPMTBNRHcwb29keE0xcXB0RWN5UUdtTWJCdE45dXc0MDNsWThMNE12OWVwRUgwQkdZclp0aCsxZUxqdFczcnB1d1hKenU0Vzd0WEt4azhqTEEzbEFudmVLZ1pZVFRCU2FJaGlTbTFvekxBY2xWeGljOEtyWGI2aVFmYjg5OXQvbkpxZmRwaXMvOEJZK1lxcFNDcjI5Z3VncTFTQkY3bEYxUTNCSzlmRitYZDk4VWUxRzRIM0pBNTlKeXZ2d0RwTUFzK2VscHFVaVRvRUVoU1BwckdIUEF6dnpvMHNsT0xOODZlWWRKcEk1MnloaEp2VS9VVjM4TDZzQnlGbmZWRFJFZFIzRGZzN1o1MTBTb2VUZkk0TjNqYWRLN1pncFErZlA5bUo0WEJtbUs2NUVMU2szMzhEeUtDT0hIM1FiejdPMU8raEU9qXRpbWVzdGFtcNoDzGdxbHphV2R1WVhSMWNtWGFBcXhJU2xwWE5FZzJRbFpHTXpsUldsb3pVWEUwYmxKblpUSTFNa3BYVVV4M1JWaHliMjVUVW1Jd1NGRm9ZWFJsVDBkUVkxVkhUbFJHYm1kT0wwUk1OMXB3T0RBNE56SlRMMFpwTkZaaGVIbHFURGRpYVdreFIxYzFkVGhGWWk5MVJuRTRVVlowU1dSc1oxSjZaWFZMZVUxSWRXTkNTRmt3UW1NM1VHTnNORkI1ZURSNGEyeElSbGxMVERWbmNuVnBVMlJrZW1Oa2RXTlJiRVZUWXlzNU5IbERSbTFYYVU1TE5HOHhhbEYyWkZSRVpFVndOamRLZWt3d05uVm1XV3hGYldsT1FWaGhUMGRFVEVadFRTdFphWEpaVW5SaFNEbHpWVmtyZEc1M2FESnFXRXhNTjNWTlVUVlFTMmd5Y2xZemJreGhSM0paZEZFdk5GSmhVbmxvVkVoeE5uWjVSMnhEVlhsdFN6UkljRU5UWmpSelQwdFhZMUJYUWxwMFUxaE1jM1pMTTBkTWJubDFRMFlyV1dKbk1DOXpaMGxHT1ZVM04xaFdUVFl2VURneE9UTkNXVXAwVWxaTUx6Um5OamcxWTBGc2JrRlJMMDFIT1RGdlVWUXhWazVqUkhwQmRtMUpORUpMVkVScWMzQlhaa1pFVDFSd2VsTkVkVk0wU0dOMVNqRlZkVWRDV1ZCTVltNUllSEJEZFc5c1lqQTRia0l6ZDFjcmMzcFZVa2RoYkM5SE9FTk9OMUZQY0d4UE9FMHdXRkJNWkdoSVVUZ3ZNMjlpWld0UlptMUpla3d2VFhoUVpWcHdiMDV3TDBsRmRFSlZWVEE0TTJOeVYxb3dhWEozWkhWVGRrSmhWV3hXYVRCaFRHeHJZbXBQYzJrMGJGaFJUemx3ZVVoNFJsQm9ibTFWVGtWd2NITTVRVlZDVW5sNmJtdFhZa2hGUVN0T01UWlJWRzV5VGtZNVpqQm1RVmROY0ZoNlQyMDJiSEU0Y25KRVIzaDRPRnBoT1V4T1Uzb3lOME5hVkV3NUwxVk9TVGRqWlN0bU9GVTROelp0VW1oSk4wazJSa3BPY2xCR2JraHpkRzl6TldwVlpreEVNVkUzTTJ4WFZIbDFZamszT1VNNFdtTmxOVEpwZVVGbVMzUXhiRVZPTUhsbFFsQnpSRk55ZFhOdVRGZEROR2hNVTNZelJGbzJUMnMxVlc4M1MzWTVhejJwZEdsdFpYTjBZVzF3c2pFMU1URXpOVFl5T0RNdU1qSTNNRGN3T0E9PQ== |
  
  @wip
  Scenario Outline: Send Message
    Given following privkey
    """
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
    """
    And derived address <sender>
    And message type "REGISTRATION" <messageType>
    And message hash <messageHash>
    And body hash <bodyHash>
    And message signature <messageSig>
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
      sender: <sender>
      messageType: <messageType>
      messageHash: <messageHash>
      bodyHash: <bodyHash>
      messageSig: <messageSig>
      message: <message>
      dossierHash: <dossierHash>
    }
    """
    And send message mutation to bootstrap node <bootstrapNode>
    Then response should be success
    And response should have cacheTXID property