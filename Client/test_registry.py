from TelefericClient.Identity import Identity
from TelefericClient.Schema.Register import Register

identity = Identity()

invite_message_hash = "c2npU+GslWdBfysO4YevAg/B6DPr66+mVAXuLFoy7e8="

register = Register(
    identity,
    'http://localhost:8000/teleferic/',
)
register.compose(
    inviteMsgID=invite_message_hash, 
    inviteKey= '72x35FDOXuTkxivh', 
    inviteName= 'Invite 1',
    nickname= 'sarasa3'
)
result = register.send()
print(result)
