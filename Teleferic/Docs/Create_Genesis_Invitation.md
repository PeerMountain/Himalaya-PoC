# Create an Identity
```python
from API.models import Invitation
from Test.identity_tools import Identity
import base58
import json

identity = Identity()

passphrase = '1'.encode('utf8')

invitation_data =  identity.generate_invitation(passphrase=passphrase)
invitation = Invitation(key=invitation_data['key'], content=invitation_data['content'])
invitation.save()

token =  base58.b58encode(bytes(invitation.__str__().encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(passphrase)).encode('utf8')))

message_content = {
  'token': token
}

sign = identity.sign(json.dumps(message_content, ensure_ascii=False))