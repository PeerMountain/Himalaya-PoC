# Genesis Invite
```bash
docker exec -ti himalaya_teleferic_1 python manage.py shell
```
Run next code
```python
from API.models import Invitation
from Playground.identity_tools import Identity
import base58

passphrase = '1'

genesis_identity = Identity()
invitation_data =  genesis_identity.generate_invitation(passphrase=passphrase)
invitation = Invitation(
  key=invitation_data['key'], 
  content=invitation_data['content'],
  sender=genesis_identity.address
)
invitation.save()

token =  base58.b58encode(bytes(invitation.__str__().encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(passphrase.encode('utf8'))).encode('utf8')))

print('Token:', token)
exit()
```
