from TelefericClient.Identity import Identity
from TelefericClient.Schema.Register import Register

identity = Identity(open("keys/4096_c.private").read())

invite_message_hash = "QkaoapEUS9M91iPI++wAMrfhKN+avvqpylj5uZ1bXhs="

register = Register(
    identity,
    'http://localhost:8000/teleferic/',
)
register.compose(
    inviteMsgID=invite_message_hash, 
    inviteKey= '72x35FDOXuTkxivh7qYlqPU91jVgy607', 
    inviteNonce=b'testnoncedonotrepeatinprodplease',
    inviteName= 'Invite 1',
    nickname= '4096_c'
)
result = register.send()
print(result)
