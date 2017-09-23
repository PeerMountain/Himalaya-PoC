# Genesis Invite
```bash
docker exec -ti himalaya_teleferic_1 python manage.py shell
```
Run next code
```python
from API.models import Invitation
from identity_tools import Identity
import base58
import random

passphrase = base58.b58encode(bytes(str(random.random()).encode('utf8')))

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
#NfG35M4SGP3uvW3C9wCNTq7z1TvSsNRB2ajCmDiNuuSEvCi63
exit()
```
Or load sample data to get same result
```bash
docker exec -ti himalaya_teleferic_1 python manage.py loaddata API/genesis_data.json
```