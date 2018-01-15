from TelefericClient.Identity import Identity
from TelefericClient.Schema.Register import Register

identity = Identity(open("keys/4096_a.private").read())

invite_message_hash = "ypiI7utRFTqFCRDiR6bAAZfp1RcYphBOfN47YD81tLk="

register = Register(
    identity,
    'http://localhost:8000/teleferic/'
)
register.compose(
    inviteMsgID=invite_message_hash, 
    inviteKey= '72x35FDOXuTkxivh7qYlqPU91jVgy607', 
    inviteName= 'Invite 1',
    nickname= '4096_a'
)
result = register.send()
print(result)