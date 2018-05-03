import base64

from TelefericClient.Identity import Identity
from TelefericClient.Schema.Invite import Invite

identity = Identity(open("keys/4096_registred.private").read())

invite = Invite(
    identity,
    'http://localhost:8000/teleferic/',
)

invite.compose(
    bootstrapAddr='8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL',
    bootstrapNode='http://localhost:8000/teleferic/',
    inviteName='Invite 1',
    offeringAddr='8MSd91xr6jSV5pS29RkV7dLeE3hDgLHJGrsyXpdSf4iitj6c75tVSNESywBzYzFEeyu5D1zyrL',
    serviceAnnouncementMessage='L+ViP+UFnhc6ObWfhugqNZfE+SZkqoS46I4Qbw+NbOY=',
    serviceOfferingID='1',
    inviteKey='72x35FDOXuTkxivh7qYlqPU91jVgy607',
    inviteNonce=b'testnoncedonotrepeatinprodplease'
)

result = invite.send()
print(result)
print(f"base64 encoded nonce used: {base64.b64encode(invite.nonce)}")
#We need printed messageHash and nonce to perform the registration
