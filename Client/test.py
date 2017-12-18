from TelefericClient.Schema.Invite import Invite
from TelefericClient.Schema.Register import Register
from TelefericClient.Identity import Identity

import base64
from Crypto.Hash import SHA256

id = Identity("""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
""")

invite = Invite(
    id,
    'https://teleferic-dev.dxmarkets.com/teleferic/'
)
print('pubkey',base64.b64encode(SHA256.new(id.pubkey).digest()))
invite.compose(
    bootstrapAddr='8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL',
    bootstrapNode='https://teleferic-dev.dxmarkets.com/teleferic/',
    inviteName='Invite 1',
    offeringAddr='8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL',
    serviceAnnouncementMessage='L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY=',
    serviceOfferingID='1',
    inviteKey='72x35FDOXuTkxivh7qYlqPU91jVgy607'
)

result = invite.send()
print(result)

new_identity = Identity("""
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
""")

invite = Invite(
    new_identity,
    'https://teleferic-dev.dxmarkets.com/teleferic/'
)
invite.compose(
    bootstrapAddr='8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL',
    bootstrapNode='https://teleferic-dev.dxmarkets.com/teleferic/',
    inviteName='Invite 1',
    offeringAddr='8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL',
    serviceAnnouncementMessage='L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY=',
    serviceOfferingID='1',
    inviteKey='72x35FDOXuTkxivh7qYlqPU91jVgy607'
)

result = invite.send()

invite_msg_hash = result['data']['sendMessage'][
        'messageHash']

register = Register(
    Identity(),
    'https://teleferic-dev.dxmarkets.com/teleferic/'
)
register.compose(
    inviteMsgID=invite_msg_hash, 
    inviteKey= '72x35FDOXuTkxivh7qYlqPU91jVgy607', 
    inviteName= 'Invite 1',
    nickname= 'Pepe'
)
result = register.send()
print(result)


register = Register(
    Identity(),
    'https://teleferic-dev.dxmarkets.com/teleferic/'
)
register.compose(
    inviteMsgID=invite_msg_hash, 
    inviteKey= '72x35FDOXuTkxivh7qYlqPU91jVgy607', 
    inviteName= 'Invite 1',
    nickname= 'Pepe2'
)
result = register.send()
print(result)

register = Register(
    Identity(),
    'https://teleferic-dev.dxmarkets.com/teleferic/'
)
register.compose(
    inviteMsgID=invite_msg_hash, 
    inviteKey= '72x35FDOXuTkxivh7qYlqPU91jVgy607', 
    inviteName= 'Invite 1',
    nickname= 'Pepe3'
)
result = register.send()
print(result)