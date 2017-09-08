# Create an Identity

```python
from API.models import Invitation
from Test.identity_tools import Identity
import base58

passphrase = '1'.encode('utf8')

genesis_identity = Identity()
invitation_data =  genesis_identity.generate_invitation(passphrase=passphrase)
invitation = Invitation(key=invitation_data['key'], content=invitation_data['content'])
invitation.save()

token =  base58.b58encode(bytes(invitation.__str__().encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(passphrase)).encode('utf8')))

print('Token:', token)
#Token: 'HX8d'
```
# Registration

```python
from Test.identity_tools import Identity
from Crypto.PublicKey import RSA
import base58
import json
import os

privkey_file = open('Test/identity', 'rb')
privkey = RSA.importKey(privkey_file.read())
identity = Identity(privkey)

token='HX8d'

message_content = {
  'token': token
}

sign = identity.sign(json.dumps(message_content))

print('''
  mutation {
    register(
      message: {
        token: "'''+token+'''"
      }
      
      envelope: {
        sender: "'''+identity.address+'''"
        pubkey: "'''+identity.pubkey+'''"
        sign: "'''+sign+'''"
      }
    ){
      ok
    }
  }
''')
```

# Invite
```python
from Test.identity_tools import Identity
from Crypto.PublicKey import RSA
import base58
import json
import os

privkey_file = open('Test/identity', 'rb')
privkey = RSA.importKey(privkey_file.read())
identity = Identity(privkey)

passphrase='2'.encode('utf8')

invitation = identity.generate_invitation(passphrase=passphrase)

message_content = {
  'content': invitation.get('content'),
  'key': invitation.get('key')
}

sign = identity.sign(json.dumps(message_content))

print('''
  mutation invite(
    $content: String!
    $key: String!
    $sender: String!
    $sign: String! 
  ){
    invite(
      envelope: {
        sender: $sender
        sign: $sign
      }
      message: {
        content: $content
        key: $key
      }
    ) {
      ok
    }
  }
''')

print('''
  {
    "content": "'''+invitation.get('content')+'''",
    "key": "'''+invitation.get('key')+'''",
    "sender": "'''+identity.address+'''",
    "sign": "'''+sign+'''"
  }
''')

invitation_id = '2'

token =  base58.b58encode(bytes(invitation_id.encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(passphrase)).encode('utf8')))

```
